## Essential Questions

- How do scientists (and machines) discover rules they can't see?
- Why is a "no" often more informative than a "yes"?

## Lesson Plan

This lesson follows Guess Who. In Guess Who, students know every possible
answer in advance (24 faces with visible features) and the job is to split
that set efficiently. In Eleusis, players don't know what the possible rules
even are, so students have to invent hypotheses and design experiments to
test them. This jumps from classification to scientific induction.

Day 1 is the game and the "how does science work?" debrief. Day 2 takes the
game into Weka.

### Setup

- Two decks of standard playing cards per group of 4-5 students
- Index cards with secret rules for dealers (see `Dealer rules` below)

### Actual Lesson

- Review
    - Decision trees: root, node, leaf, balanced
    - Guess Who: best first question splits the set in half
    - Training set
    - Test set
    - Over-fitting
- Warm-up: 2-4-6 task (~10m)
    - Write "2, 4, 6" on the board and say it follows a secret rule
    - Students propose triples; I only answer "yes" or "no"
    - Secret rule: _any three increasing numbers_
    - Most students test triples that fit their guess ("add 2": 10, 12, 14...)
      and get "yes" every time
    - Ask before revealing: "Who tested a triple you expected to get a no?"
    - Debrief
        - **Confirmation bias**: tests you expect to pass can't tell you you're wrong
        - The informative experiment is the one that might fail
        - Where have we seen this? Unit tests in the skills assessments: "at
          least one should catch a wrong implementation"
            - A test you know will pass is a 2-4-6 triple
- Explain simplified Eleusis (~5m)
    - One dealer (god) per group writes a secret rule on an index card (or hand
      them one from `Dealer rules`)
    - God deals 10 cards to each player; god flips one starter card face up
    - On your turn, play one card to the right of the last accepted card
        - God says "yes" -> card stays on the main line
        - God says "no" -> card goes _below_ the card it tried to follow,
          and you draw 1 penalty card
    - If you think you have no legal card, say "no play" and show your hand
        - Player is right that nothing works -> Discard 2
        - Player is wrong and something works -> Draw 4
    - Rejected cards stay on the table, so everyone can study the full record
    - Round ends when someone runs out of cards
    - At the end, every player writes down the rule they think it is
    - God wins if _at least one_ player got it right but _not everyone_
        - Forces dealers to pick a rule that's hard but discoverable
- Round 1: Go! (~12m)
- Rotate who's god. Round 2 (~12m)
- Debrief
    - What was your best single card play, and why?
        - Look for students who played cards they expected to be rejected
    - Did anyone have a rule that fit everything on the table but turned out wrong?
        - **Over-fitting**; the dealer's next answer was the test set
    - Could you predict the dealer's answers before you could state the rule?
        - Prediction vs. understanding (ties back to the data and science discussion)
    - How was this different from Guess Who?
        - In Guess Who you knew all the possible answers; here you had to invent them
        - You chose which card to play = designing your own experiment
    - Where have we seen this before?
        - The "undefined machines" in the FSM unit: watch which strings get
          accepted, then guess the machine
        - "Alternate red and black" is a 2-state FSM
    - How is this unlike real science?
        - Nature doesn't pick rules to be "just hard enough"
        - Nature's answers are noisy
        - Nobody reveals the answer at the end
- Set up tomorrow
    - "Tomorrow we find out whether a decision tree can play this game."

### Homework

- Write a paragraph: describe one moment in the game where you changed your
  hypothesis, and what evidence caused it. Was it a "yes" or a "no"?
- Adv. Data Structure Wheaties 12 - 14

### Dealer rules

Print one per index card. The "no play" rule keeps any of these from getting
stuck.

- Easy
    - Alternate red and black
    - Play a different suit than the previous card
- Medium
    - Alternate odd and even ranks
    - Same suit OR same rank as the previous card
- Hard
    - After an odd card play a red card; after an even card play a black card
    - Rank must be within 3 of the previous card's rank (Ace = 1, King = 13)

### Resources

- Martin Gardner's _Scientific American_ columns on Eleusis (1959, 1977)
- Romesburg, "Simulating Scientific Inquiry with the Card Game Eleusis,"
  _Science Education_ (1979)
- Walkup & Key, ["Speed Eleusis"](https://pubs.aip.org/aapt/pte/article/58/3/160/278755/Speed-Eleusis-Variation-on-an-Old-Educational-Card),
  _The Physics Teacher_ (2020): faster variant built for intro science labs
- Zendo: a related rule-discovery game played with pyramid pieces
    - [ZendoWorld](https://ml-research.github.io/ZendoWorld/): AI researchers
      use Zendo to test whether machines can do this kind of rule discovery
- Berkeley Understanding Science "Mystery Tubes" lesson (grades 6-16): a
  hands-on black-box version of the same idea
- People to ask about using this with high schoolers (unverified)
    - John Walkup (Fresno State), co-author of "Speed Eleusis"
    - Joss Ives (UBC), blog roundup of nature-of-science games; commenters
      Andy Rundquist and Bret Benesh also teach with them
    - David Low (UNSW Canberra), used Eleusis and Zendo with first-years
        - Tips: groups of 4 or fewer, always include a reflection stage
    - Kirk Brown (Tracy High School), co-wrote an early "Mystery Tubes"
    - BoardGameGeek threads on "Zendo as a tool for teaching the scientific
      method"
