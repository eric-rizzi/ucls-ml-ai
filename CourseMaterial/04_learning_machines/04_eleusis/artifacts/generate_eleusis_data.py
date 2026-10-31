#!/usr/bin/env python3
"""Simulate Eleusis rounds and write Weka-ready CSVs.

Each row is one card a player tried to play. The "previous" card is the last
card on the main line (rejected cards never change it).

The "alternate colors" files pool many rounds. With only one round (~60
rows), a decision tree finds fake patterns in Rank and Suit by luck, which
ruins the "the tree can't see this rule" moment. Pooling enough rows makes
the single-card features drop to a coin flip, as they should.

The mystery rule gets two files: a "raw" one with only the card and previous
card (students invent the features by hand), and a full one with relational
columns added (for J48).

Usage: python generate_eleusis_data.py OUTPUT_DIR
"""
import csv
import random
import sys
import typing

RANKS = list(range(1, 14))  # Ace = 1 ... King = 13
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
COLOR = {"Hearts": "Red", "Diamonds": "Red", "Clubs": "Black", "Spades": "Black"}

ALTERNATE_ROUNDS = 15  # rounds pooled into the alternate-colors files
PLAYS_PER_ROUND = 40  # roughly one 12-minute round with 4-5 players
MYSTERY_PLAYS = 80  # small enough for groups to read by hand

CARD_HEADER = ["Rank", "Suit", "Color", "Parity"]
PREV_HEADER = ["Prev Rank", "Prev Suit", "Prev Color", "Prev Parity"]


class Card(typing.NamedTuple):
    rank: int
    suit: str


class Play(typing.NamedTuple):
    card: Card
    prev: Card
    accepted: bool


Rule = typing.Callable[[Card, Card], bool]


def parity(rank: int) -> str:
    return "Odd" if rank % 2 else "Even"


def compare(rank: int, prev_rank: int) -> str:
    if rank > prev_rank:
        return "Higher"
    if rank < prev_rank:
        return "Lower"
    return "Same"


def yes_no(value: bool) -> str:
    return "Yes" if value else "No"


def alternate_colors(card: Card, prev: Card) -> bool:
    return COLOR[card.suit] != COLOR[prev.suit]


def mystery(card: Card, prev: Card) -> bool:
    # Same parity as the previous card, or any face card (J, Q, K).
    return parity(card.rank) == parity(prev.rank) or card.rank > 10


def describe(card: Card) -> list:
    return [card.rank, card.suit, COLOR[card.suit], parity(card.rank)]


def relational(card: Card, prev: Card) -> list[str]:
    return [
        yes_no(COLOR[card.suit] == COLOR[prev.suit]),
        yes_no(card.suit == prev.suit),
        yes_no(parity(card.rank) == parity(prev.rank)),
        compare(card.rank, prev.rank),
    ]


def simulate(rule: Rule, n_plays: int, seed: int) -> list[Play]:
    """One round with a fresh double deck."""
    rng = random.Random(seed)
    deck = [Card(rank, suit) for suit in SUITS for rank in RANKS] * 2
    rng.shuffle(deck)
    prev = deck.pop()
    plays = []
    for _ in range(n_plays):
        card = deck.pop()
        accepted = rule(card, prev)
        plays.append(Play(card, prev, accepted))
        if accepted:
            prev = card
    return plays


def write(path: str, header: list[str], rows: list[list]) -> None:
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def main(out_dir: str) -> None:
    plays = []
    for seed in range(ALTERNATE_ROUNDS):
        plays += simulate(alternate_colors, PLAYS_PER_ROUND, seed=seed)
    write(
        f"{out_dir}/eleusis_round_basic.csv",
        CARD_HEADER + ["Accepted"],
        [describe(p.card) + [yes_no(p.accepted)] for p in plays],
    )
    write(
        f"{out_dir}/eleusis_round_with_context.csv",
        CARD_HEADER + PREV_HEADER + ["Same Color as Prev", "Accepted"],
        [
            describe(p.card)
            + describe(p.prev)
            + [yes_no(COLOR[p.card.suit] == COLOR[p.prev.suit]), yes_no(p.accepted)]
            for p in plays
        ],
    )

    plays = simulate(mystery, MYSTERY_PLAYS, seed=11)
    write(
        f"{out_dir}/eleusis_mystery_raw.csv",
        CARD_HEADER + PREV_HEADER + ["Accepted"],
        [describe(p.card) + describe(p.prev) + [yes_no(p.accepted)] for p in plays],
    )
    write(
        f"{out_dir}/eleusis_mystery.csv",
        CARD_HEADER
        + PREV_HEADER
        + ["Same Color as Prev", "Same Suit as Prev", "Same Parity as Prev", "Rank vs Prev", "Accepted"],
        [
            describe(p.card) + describe(p.prev) + relational(p.card, p.prev) + [yes_no(p.accepted)]
            for p in plays
        ],
    )


if __name__ == "__main__":
    main(sys.argv[1])
