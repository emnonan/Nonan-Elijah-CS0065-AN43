# Technical Assessment 3: Intelligent Tutoring System - Case-Based Reasoning

## Requirements

- Python 3
- PyCharm or another Python IDE
- No external packages are required

## Files

- `Intelligent_Tutoring_System.py` - the application source file.
- `its_retained_cases.json` — created beside the source file after the first successful save. It stores newly retained cases; the five sample cases remain in the Python source.

## Run in PyCharm

1. Open or create a Python project in PyCharm.
2. Add `Intelligent_Tutoring_System.py` to the project.
3. Open the file and click **Run**.
4. Enter the requested learner details in the Run console.

The program can process more than one learner in a session. At the end of each scenario, enter `y` to continue or `n` to stop.

## Entering a learner problem

Provide:

- **Subject:** `math`, `english`, or `science`
- **Main error pattern:** `conceptual`, `calculation`, `careless`, or `memory`
- **Mastery:** a whole number from 0 to 100
- **Problem description:** a short description; this can be left blank to use a generated description

The program repeats prompts when a choice or mastery value is invalid.

## CBR cycle

1. **Retrieve:** Scores every case using the new learner's attributes and displays the ranked results.
2. **Reuse:** Shows the solution from the highest-ranked case.
3. **Revise:** Adapts that retrieved strategy to the new learner's error pattern, mastery level, and subject.
4. **Retain:** Adds the new problem and adapted recommendation to the case base and saves it to `its_retained_cases.json`.

The similarity score is a weighted percentage:

| Attribute     | Weight | Scoring                                                   |
| ------------- | -----: | --------------------------------------------------------- |
| Subject       |    40% | Full attribute score for a match; otherwise zero          |
| Error pattern |    35% | Full attribute score for a match; otherwise zero          |
| Mastery       |    25% | Normalized by the difference between the two 0–100 levels |

For mastery, identical values receive full credit and a 100-point difference receives zero. If scores tie, cases are listed by ID to make the ranking stable.

Adaptation begins with the retrieved case's strategy, then adds guidance for the current error pattern and mastery level, plus a subject-specific practice suggestion.

## Saved data and recovery

Saved cases are loaded when the program starts. If the JSON file is missing, the five built-in sample cases are used. If the file is malformed or cannot be read, the program prints a notice and continues with the built-in cases. If saving fails, the new case remains available in memory for the current session, but it will not persist after the program closes.

To start over with only the built-in cases, close the program and delete `its_retained_cases.json`. The sample cases in the Python source are not changed by retention.
