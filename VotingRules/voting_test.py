import importlib
import random
from typing import Callable


class Preference:
    def __init__(
        self,
        voters: list[int],
        candidates: list[int],
        voting_prefs: dict[int, list[int]],
    ):
        self._voters = voters
        self._candidates = candidates
        self._voting_prefs = voting_prefs

    def voters(self):
        return self._voters

    def candidates(self):
        return self._candidates

    def get_preference(self, candidate: int, voter: int):
        return self._voting_prefs[voter].index(candidate)


def generate_sample_data() -> tuple[list[int], list[int], dict[int, list[int]]]:
    voters = [1,2,3,4,5,6,7,8,9]
    candidates = [1,2,3,4,5,6,7,8,9]

    voting_prefs = {
        1: [1, 2, 3, 4, 5, 6, 7, 8, 9],       # Voter 1 prefers candidate 1 most, then 2, etc.
        2: [9, 3, 5, 7, 1, 6, 8, 2, 4],       # Voter 2's ranked preferences
        3: [2, 5, 8, 7, 4, 6, 9, 1, 3],       # Voter 3's ranked preferences
        4: [4, 3, 1, 2, 5, 6, 7, 8, 9],       # Voter 4's ranked preferences (completed)
        5: [7, 4, 3, 2, 1, 9, 8, 6, 5],       # Voter 5's ranked preferences
        6: [5, 6, 7, 3, 2, 1, 4, 9, 8],       # Voter 6's ranked preferences
        7: [3, 7, 8, 2, 6, 5, 4, 9, 1],       # Voter 7's ranked preferences
        8: [8, 6, 1, 9, 7, 3, 4, 5, 2],       # Voter 8's ranked preferences
        9: [6, 1, 4, 9, 8, 5, 7, 3, 2]        # Voter 9's ranked preferences
    }   
    return (voters, candidates, voting_prefs)


def print_sample_data(
    voters: list[int], candidates: list[int], voting_prefs: dict[int, list[int]]
):
    print()
    print("These are the sample data:")
    print("voters:", voters)
    print("candidates:", candidates)
    print("voting_prefs: {")
    for voter, prefs in voting_prefs.items():
        print(f"    {voter}: {prefs},")
    print("}")
    print()


separator = "=============================================="


def test_dictatorship(voting_func: callable, preferences: Preference):
    print("DICTATORSHIP Function")
    if not voting_func:
        return

    dictator_agent = 3
    try:
        result = voting_func(preferences, dictator_agent)

        print("dictator agent:", dictator_agent)
        print("dictatorship result:", result)
    except Exception as exc:
        print("Could not run the dictatorship function!")
        print(f"Error type: {type(exc)}")
        print(f"Error message: {exc}")
    finally:
        print(separator)


def test_scoring_rule(voting_func: callable, preferences: Preference, tie_agent: int):
    print("SCORING_RULE Function")
    if not voting_func:
        return

    score_vector = [5,10,22,4,1,12,14,15,16]

    try:
        result = voting_func(preferences, score_vector, tie_agent)
        print("score_vector:", score_vector)
        print("tie_break_agent:", tie_agent)
        print("scoring_rule result:", result)
    except Exception as exc:
        print("Could not run the scoring_rule function!")
        print(f"Error type: {type(exc)}")
        print(f"Error message: {exc}")
    finally:
        print(separator)


def test_other_rules(
    voting_func: Callable, preferences: Preference, tie_agent: int, name: str
):
    print(f"{name} Function")
    if not voting_func:
        return

    try:
        result = voting_func(preferences, tie_agent)
        print("tie_break_agent:", tie_agent)
        print(f"{name} result:", result)
    except Exception as exc:
        print(f"Could not run the {name} function!")
        print(f"Error type: {type(exc)}")
        print(f"Error message: {exc}")
    finally:
        print(separator)


print()
print()
print()

# importing voting functions
try:
    voting_module = importlib.import_module(name="voting")
except ModuleNotFoundError:
    print("****** File 'voting.py' not found! ******")
    raise ModuleNotFoundError

voting_funcs = {}
for function in ["dictatorship", "scoring_rule", "plurality", "veto", "borda", "STV"]:
    try:
        voting_funcs[function] = getattr(voting_module, function)
    except AttributeError:
        print(f"****** The {function} function not found, skipping! ******")
        print()
        voting_funcs[function] = None


# generate sample data
voters, candidates, voting_prefs = generate_sample_data()
preference_obj = Preference(voters, candidates, voting_prefs)
tie_agent = 2


# print out sample data
print_sample_data(voters, candidates, voting_prefs)

# test voting functions
test_dictatorship(voting_funcs["dictatorship"], preference_obj)
test_scoring_rule(voting_funcs["scoring_rule"], preference_obj, tie_agent)
test_other_rules(voting_funcs["plurality"], preference_obj, tie_agent, "plurality")
test_other_rules(voting_funcs["veto"], preference_obj, tie_agent, "veto")
test_other_rules(voting_funcs["borda"], preference_obj, tie_agent, "borda")
test_other_rules(voting_funcs["STV"], preference_obj, tie_agent, "STV")

print()
print()
print()
