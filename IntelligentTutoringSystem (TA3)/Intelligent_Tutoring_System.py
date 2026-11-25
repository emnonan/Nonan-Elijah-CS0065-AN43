"""
TA3 Case-Based Reasoning: Intelligent Tutoring System.

The program retrieves a similar learning case, reuses its strategy, adapts the feedback, and retains the new case in a local JSON file.
"""

import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("its_retained_cases.json")

# Each case has an ID, a short problem description, student attributes, and the learning strategy that helped in that situation.
SAMPLE_CASES = [
    {
        "id": "ITS-001",
        "description": "A learner confuses multiplication and addition facts.",
        "attributes": {
            "subject": "math",
            "error_type": "conceptual",
            "mastery": 30,
        },
        "solution": "Use visual examples and explain the concept step by step.",
    },
    {
        "id": "ITS-002",
        "description": "A learner understands fractions but makes calculation errors.",
        "attributes": {
            "subject": "math",
            "error_type": "calculation",
            "mastery": 55,
        },
        "solution": "Model one worked example, then give short calculation practice.",
    },
    {
        "id": "ITS-003",
        "description": "A learner applies the wrong rule when solving equations.",
        "attributes": {
            "subject": "math",
            "error_type": "conceptual",
            "mastery": 60,
        },
        "solution": "Review the rule with a worked example and ask the learner to explain each step.",
    },
    {
        "id": "ITS-004",
        "description": "A learner makes spelling errors in English writing.",
        "attributes": {
            "subject": "english",
            "error_type": "careless",
            "mastery": 70,
        },
        "solution": "Use a short editing checklist and ask the learner to review their own work.",
    },
    {
        "id": "ITS-005",
        "description": "A learner struggles to remember science vocabulary.",
        "attributes": {
            "subject": "science",
            "error_type": "memory",
            "mastery": 40,
        },
        "solution": "Use flashcards and spaced review, with a simple example for each term.",
    },
]


def load_case_base():
    """Load retained cases, keep the built-in sample cases available."""
    cases = list(SAMPLE_CASES)

    if not DATA_FILE.exists():
        return cases

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            saved_cases = json.load(file)

        if not isinstance(saved_cases, list):
            raise ValueError("The JSON root must be a list.")

        sample_ids = {case["id"] for case in SAMPLE_CASES}
        for case in saved_cases:
            if (
                isinstance(case, dict)
                and isinstance(case.get("id"), str)
                and isinstance(case.get("attributes"), dict)
                and isinstance(case.get("solution"), str)
                and case["id"] not in sample_ids
            ):
                cases.append(case)

    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"Notice: Could not load saved cases ({error}).")
        print("The built-in sample cases will still be available.")

    return cases


def save_retained_cases(cases):
    """Save only newly retained cases, leaving built-in examples in the code."""
    sample_ids = {case["id"] for case in SAMPLE_CASES}
    retained_cases = [case for case in cases if case["id"] not in sample_ids]

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(retained_cases, file, indent=2)


def ask_choice(prompt, choices):
    """Ask until the user enters one of the permitted choices."""
    allowed = ", ".join(choices)

    while True:
        answer = input(f"{prompt} ({allowed}): ").strip().lower()
        if answer in choices:
            return answer
        print(f"Please enter one of: {allowed}.")


def ask_mastery():
    """Ask for a whole-number mastery level from 0 to 100."""
    while True:
        answer = input("Mastery level (0-100): ").strip()
        try:
            mastery = int(answer)
            if 0 <= mastery <= 100:
                return mastery
        except ValueError:
            pass
        print("Enter a whole number from 0 to 100.")


def get_new_problem():
    """Collect and return the new student's problem and attributes."""
    print("\nEnter the learner's new problem.")
    subject = ask_choice("Subject", ["math", "english", "science"])
    error_type = ask_choice(
        "Main error pattern",
        ["conceptual", "calculation", "careless", "memory"],
    )
    mastery = ask_mastery()

    description = input("Brief problem description: ").strip()
    if not description:
        description = f"Learning difficulty in {subject} ({error_type} errors)."

    return {
        "description": description,
        "attributes": {
            "subject": subject,
            "error_type": error_type,
            "mastery": mastery,
        },
    }


def similarity(new_attributes, old_attributes):
    """Calculate a transparent weighted score from 0 to 100.

    Subject contributes 40 points, error pattern 35 points, and mastery 25 points. Mastery similarity is normalized: a 0-point difference scores 1.0, while a 100-point difference scores 0.0.
    """
    subject_score = (
        1.0 if new_attributes["subject"] == old_attributes["subject"] else 0.0
    )
    error_score = (
        1.0
        if new_attributes["error_type"] == old_attributes["error_type"]
        else 0.0
    )
    mastery_score = 1.0 - (
        abs(new_attributes["mastery"] - old_attributes["mastery"]) / 100.0
    )

    weighted_score = (
        0.40 * subject_score
        + 0.35 * error_score
        + 0.25 * mastery_score
    )
    return weighted_score * 100


def retrieve_best_case(new_attributes, cases):
    """Rank cases by similarity; break ties by case ID for stable results."""
    ranked_cases = [
        (similarity(new_attributes, case["attributes"]), case)
        for case in cases
    ]
    ranked_cases.sort(key=lambda item: (-item[0], item[1]["id"]))
    return ranked_cases


def adapt_solution(retrieved_case, new_attributes):
    """Reuse the retrieved strategy and adapt it to the new learner."""
    subject = new_attributes["subject"]
    error_type = new_attributes["error_type"]
    mastery = new_attributes["mastery"]
    base_strategy = retrieved_case["solution"]

    # Keep the retrieved case's strategy as the starting point, then tailor it.
    if error_type == "conceptual":
        adaptation = "Add a simple explanation and a visual or concrete example."
    elif error_type == "calculation":
        adaptation = "Add several short practice questions and check each step."
    elif error_type == "careless":
        adaptation = "Add a brief self-check checklist before submitting work."
    else:  # memory
        adaptation = "Add flashcards and review the material again after a short delay."

    if mastery < 40:
        level_guidance = "Begin with one small step and provide close guidance."
    elif mastery < 70:
        level_guidance = "Use a worked example, then let the learner try a similar task."
    else:
        level_guidance = "Give a more challenging task and ask the learner to explain their reasoning."

    subject_guidance = {
        "math": "Use numbers or equations from the current math topic.",
        "english": "Use a short reading or writing example from the current lesson.",
        "science": "Use a familiar science example or diagram from the current topic.",
    }[subject]

    return (
        f"Start from the retrieved strategy: {base_strategy}\n"
        f"Adaptation for this learner: {adaptation}\n"
        f"Mastery adjustment: {level_guidance}\n"
        f"Subject-specific practice: {subject_guidance}"
    )


def next_case_id(cases):
    """Create the next sequential retained-case ID."""
    highest_number = 0
    for case in cases:
        case_id = case.get("id", "")
        if case_id.startswith("ITS-"):
            try:
                highest_number = max(highest_number, int(case_id[4:]))
            except ValueError:
                continue
    return f"ITS-{highest_number + 1:03d}"


def display_case_base(cases):
    """Print a concise view of every case currently in the case base."""
    print("\nUPDATED CASE BASE")
    print("-" * 72)
    for case in cases:
        attributes = case["attributes"]
        print(
            f"{case['id']} | {attributes['subject']} | "
            f"{attributes['error_type']} | mastery {attributes['mastery']}"
        )
        print(f"  Problem: {case['description']}")
        print(f"  Solution: {case['solution']}")


def process_scenario(cases):
    """Demonstrate Retrieve, Reuse, Revise, and Retain for one problem."""
    new_problem = get_new_problem()
    attributes = new_problem["attributes"]

    print("\nNEW PROBLEM")
    print("-" * 72)
    print(f"Description: {new_problem['description']}")
    print(f"Subject: {attributes['subject']}")
    print(f"Main error pattern: {attributes['error_type']}")
    print(f"Mastery: {attributes['mastery']}/100")

    # RETRIEVE: calculate and show the similarity ranking.
    ranked_cases = retrieve_best_case(attributes, cases)
    print("\nRETRIEVE: Similarity ranking")
    for score, case in ranked_cases:
        print(f"  {case['id']}: {score:.1f}%")

    best_score, best_case = ranked_cases[0]
    print(
        f"\nMost similar case: {best_case['id']} "
        f"({best_score:.1f}% similar)"
    )
    print(f"Problem: {best_case['description']}")

    # REUSE: take the solution associated with the retrieved case.
    print("\nREUSE: Retrieved case solution")
    print(best_case["solution"])

    # REVISE: adapt the retrieved strategy to the new attributes.
    final_solution = adapt_solution(best_case, attributes)
    print("\nREVISE: Adapted learning recommendation")
    print(final_solution)

    # RETAIN: store the solved problem and adapted recommendation.
    new_case = {
        "id": next_case_id(cases),
        "description": new_problem["description"],
        "attributes": attributes,
        "solution": final_solution.replace("\n", " "),
    }
    cases.append(new_case)

    try:
        save_retained_cases(cases)
        print(f"\nRETAIN: Saved new case {new_case['id']} to {DATA_FILE.name}.")
    except OSError as error:
        print(f"\nRETAIN: Could not save to JSON file ({error}).")
        print("The new case remains in the case base for this session.")

    display_case_base(cases)


def main():
    """Run the ITS application until the user chooses to stop."""
    cases = load_case_base()
    print("=" * 72)
    print("CASE-BASED REASONING: INTELLIGENT TUTORING SYSTEM")
    print("=" * 72)
    print(f"Loaded {len(cases)} case(s), including five built-in examples.")

    while True:
        process_scenario(cases)
        again = input("\nProcess another learner? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("\nSession complete.")
            break


if __name__ == "__main__":
    main()