## Essential Questions

- What can a learner discover if it isn't given the right features?
- How is choosing your own experiments different from learning from a fixed dataset?

## Lesson Plan

Yesterday students played Eleusis as scientists. Today they find out whether
a decision tree can do the same thing. The punchline: a tree can only discover
rules it has the features to express. The algorithm doesn't get smarter; the
features do.

### Setup

- Weka and data installed on classroom computers:
    - https://ml.cms.waikato.ac.nz/weka
    - `artifacts/eleusis*.csv`
- `science_of_learning.docx` printed out
- Yes/No Game Changer episode ready to go
    - https://www.youtube.com/watch?v=r0c1n35WySE

### Actual Lesson

- Review
    - Eleusis: hypotheses, experiments, "no" is informative
    - Confirmation bias (2-4-6)
    - Over-fitting: a rule that fits the table but fails the next card
    - Share-out: 2-3 students read their "changed my hypothesis" paragraph
        - Was the evidence a "yes" or a "no"?
- Code review
    - Spin the wheel
    - Adv. Data Structure Wheaties 9 - 14
- From the game to ML
    - What do the main line and the rejected cards below it correspond to in ML?
        - **Labeled data**: positive and negative examples
    - Who chose which examples got labeled?
        - You did, by choosing which card to play
        - **Active learning**: the learner picks which examples get labeled
        - Weka can't do that; it learns from whatever CSV it's handed
- Weka: can a decision tree play Eleusis?
    - Both `eleusis_round_*` files are the same 600 plays, pooled from 15 rounds
      played with the rule "alternate red and black"
        - Each row is one card someone tried to play; `Accepted` is the label
        - "Prev" columns describe the last card on the main line
    - Open `Weka` and select `Explorer`
    - Click `Open file...`
        - Select `.csv` as file type
        - Navigate to `eleusis_round_basic.csv`
        - Only knows about the card itself: `Rank`, `Suit`, `Color`, `Parity`
    - Select `Classify` -> `Choose` -> `trees` -> `J48`
        - Use the default `J48` settings (`-C 0.25 -M 2`)
        - Results below also hold with Guess Who's `-U -B -M 1`
    - Test options: leave `Cross-validation` at 10 folds (new!)
        - No separate test file this time, so Weka makes its own
        - Splits the data into 10 chunks, trains on 9, tests on the 1 left
          out, 10 times
        - Same idea as `Supplied test set`, just automatic
        - **Cross-validation**
    - `Start`
        - Accuracy is ~51%: a coin flip
        - **But the tree still has splits** (`Parity`, `Suit`, `Rank <= 11`)
            - Students will think it found something; it didn't
            - The tree always builds _something_. Cross-validation tells you
              whether it's real
        - Ask: why can't the tree find "alternate colors"?
            - The rule is about the _relationship_ between two cards, and the
              tree only sees one
            - Same problem as 1-grams in the n-grams lesson: no context, no
              pattern
    - Open `eleusis_round_with_context.csv`
        - Adds the previous card's features and `Same Color as Prev`
    - `Start` again
        - Tree is a single split on `Same Color as Prev`: 100%
    - Discuss
        - The algorithm didn't get smarter; the features did
        - Who picks the features? (Humans, usually: **feature engineering**)
- Mystery round
    - Open `eleusis_mystery_raw.csv` (a different secret rule)
        - Only the card and the previous card, like the main line on the table
        - View it in Excel or `Preprocess` -> `Edit...`
    - In groups: state the rule, and decide what columns you'd add to make it easy for the tree
    - Go! (~5m)
    - Open `eleusis_mystery.csv`
        - Same plays, with relational columns added (`Same Suit as Prev`,
          `Same Parity as Prev`, `Rank vs Prev`, ...)
        - Did anyone invent one of these?
    - Run `J48` and compare the tree with your hypothesis
    - Answer key: _same parity (odd/even) as the previous card, OR any face card_
        - Tree splits on `Same Parity as Prev`, then on `Rank <= 10`: 100%
        - Nice moment: "face card" shows up as a numeric threshold the tree invented
- Wrap up
    - You vs. the tree: who was the better scientist?
        - The tree was faster once it had the right features
        - You chose your own experiments and invented the features
    - Set up the science of learning discussion
        - We just compared how you learn with how a machine learns
        - The reading is about how humans learn best
- If time:
    - Watch choice bits of Game Change episode
        - Funny clip: https://www.youtube.com/watch?v=88et7YlmzTs

### Homework

- Read `science_of_learning.docx` and prepare for discussion

### Possible Extensions

- In `Preprocess`, check `Same Color as Prev`
  and click `Remove`, then rerun
    - Still 100%, but the tree goes from 2 leaves to 6-8
        - It splits on `Suit` (or `Prev Suit`), then learns "alternate
          colors" separately for each suit
    - Same accuracy, much messier tree
        - Good features make simpler models, and simpler models are easier
          to understand
- Re-play Eleusis, but have them track the data themselves for Weka
    - If really enjoyed the game the previous day, do this
