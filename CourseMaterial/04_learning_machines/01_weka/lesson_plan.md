## Essential Questions

- What does it mean for a machine to learn?
- What are the core machine learning techniques?
- How do ML algorithms compare with human intuition?

## Lesson Plan

In this lesson, students put the terminology/vocab they learned in the previous
lesson to use. In particular, they build their own "classifiers" for breast
cancer detection. They then reflect on each step of the building process and
apply the correct concept/vocab.

### Setup

- Weka installed on necessary computers
    - https://ml.cms.waikato.ac.nz/weka
    - `UserClassifier` installed via `Explorer` -> `Tools` -> `PackageManager`
- Data for Weka loaded onto necessary computers
    - `wisconsin_breast_cancer`
- `end_of_theory.docx` article printed out

### Actual Lesson

- Review
    - Supervised/reinforcement/unsupervised
    - ML as meta program that creates a program (classifiers)
    - Over-fitting
    - Human vs. Machine learning
- What is a classifier?
    - Give simple data and see if can come up with classifier
        - Dog vs. Cat
            - lbs, temperament, label
            - if > 20 lbs -> dog, elif < 10 lbs and grumpy -> dog, else -> cat
    - Draw decision tree for it
    - This is an example of a "classifier program"
    - Could easily implement this in Python with simple if/else
- Give more complex data
    - Show `cancer-training.csv` in Excel
        - Famous data set
        - Lots of measurements of various features of biopsies
    - How could we approach this?
    - Graph in different ways and try and find different splits
        - Have different graphs of data along x/y axis with clear "split" somewhere
- Today going to use Weka
    - Program for building classifiers
    - Difficult to use, so pay attention
    - Going to build a decision tree both manually and w/ ML program (called `J48`)
- Weka activity
    - Based on: https://youtu.be/bUsPNNr6pvg?si=G9FxZsKQJe1rz2FR
    - Explore `wisconsin_breast_cancer` data
        - Load it up
        - Show various graphs
        - Discuss what we see in terms of decision tree
    - Build `UserClassifier`
        - Click `Explorer`
        - Click `Open File`
            - Select `.csv` as file type
            - Navigate to `cancer-challenge.csv`
        - Open data loaded, click on `Classify`
        - Click `Choose` -> `Trees` -> `UserClassifier`
        - Select `Supplied test set` and `Set` to `cancer-test.csv`
        - Click `Start` to start building the tree
            - Make `Select Instance` a "Rectangle"
            - Draw rectangles and `Submit` whenever happy
        - Once done, click exit at the top of the screen
            - See how well you can classify the data
                - `J48` can do it with ~91% accuracy
            - Examine output classifier tree and discuss
    - Build classifier using `J48` classifier
        - Walk through output
        - Compare with the decision tree we built
        - Explain what classifier is doing
            - Iterating through data
            - Looking for cleanest "cut"
    - Look at the output: classifier
        - Just a simple Python program
- Reflection
    - What was your resulting classifier performance?
    - What does over-fitting look like?
    - Why is a test set necessary?
- Set up `end_of_theory.docx` discussion
    - You didn't understand anything about cancer as making this classifier
    - What does it mean if can do things without understanding because have good data?

### Homework

- Read `end_of_theory.docx`
    - Prepare for discussion
- Adv. Data Structure Wheaties 4 - 5

### Resources

- https://storm.cis.fordham.edu/~gweiss/data-mining/datasets.html
- https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data?resource=download
