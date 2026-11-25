# Technical Assessment 4: Energy Advisor - KR, RBR, and CBR Implementation

## Overview

`Energy_Advisor.py` demonstrates Knowledge Representation (KR), Rule-Based Reasoning (RBR), and Case-Based Reasoning (CBR) for household electricity use. The RBR section evaluates preset facts in `KNOWLEDGE_BASE`. The CBR section separately asks the user to describe a new problem, compares it with stored cases, and lets the user accept or revise the suggested solution.

The program uses only the Python standard library. Its example electricity estimate uses PHP 12 per kWh, actual rates vary by provider.

## Assessment requirements and locations

### Part 1 - Knowledge Representation (KR)

- **Location:** `KNOWLEDGE_BASE` near the top of `Energy_Advisor.py`.
- Following the assessment's terminology, the dictionary contains **five facts** (top-level entries), each with **three categories** (sub-elements):
  - `household`: residents, daytime occupancy, and daytime occupants.
  - `energy`: monthly kWh, budget, and rate per kWh.
  - `appliances`: air-conditioner hours, inverter status, and temperature setting.
  - `environment`: weather, outdoor temperature, and humidity.
  - `usage_patterns`: peak-use period, fan use, and lighting habits.
- This meets the requirement for at least five facts and three categories under each fact.
- `display_knowledge_base()` prints the preset facts and explains they were set in the code rather than entered by the user.

### Part 2 - Rule-Based Reasoning (RBR)

- **Location:** `rule_check_energy_use`, `rule_reduce_aircon_hours`, `rule_use_timer`, `rule_check_budget`, `rule_check_usage_patterns`, and `rule_check_aircon_efficiency`.
- Each function checks facts and returns an action when its IF condition applies, or `None` when it does not.
- `RULES` lists the rules. `run_inference_engine(facts)` evaluates every rule and returns all applicable actions.
- `main()` prints the facts and inferred actions beneath `===== RULE BASED REASONING =====`. If no rules apply, it prints a no-actions message.

### Part 3 - Case-Based Reasoning (CBR)

- **Location:** `CASE_BASE` and the CBR functions in Part 3.
- The case base contains three previous cases. Each case has problem features (`usage`, `aircon`, and `home`) and a corresponding solution.
- `ask_new_problem()` collects the new CBR problem independently of the preset RBR facts. `ask_choice()` repeats a prompt until the answer matches one of its listed options.
- `similarity()` calculates the proportion of comparable features that match. `retrieve_most_similar()` selects the highest-scoring case; ties select the earliest case in the list. If there is no positive match, a general starting suggestion is used.
- `run_case_based_reasoning()` demonstrates the 4R cycle:
  1. **Retrieve:** select the most similar stored case.
  2. **Reuse:** propose its solution, or the general fallback if there is no match.
  3. **Revise:** `revise_solution()` allows the user to accept the proposal or enter a replacement.
  4. **Retain:** append the new problem and its final solution to the case base.
- A retained case stays in memory during the current run; it is not saved between runs.
- CBR output appears beneath `===== CASE BASED REASONING =====`.

## Run in PyCharm

1. Open `Energy_Advisor.py` in PyCharm.
2. Choose **Run** for that file.
3. Review the preset RBR facts and resulting actions.
4. Enter the listed choices when describing the new CBR problem. At the revision prompt, enter `y` to accept the proposal or `n` to provide a replacement.
