# guardrails.py
from builtins import any

def validate_goal_input(goal) :
    # Simple: must contain number + timeframe
    return any(x in goal for x in ["week", "month", "day"]) and any(char.isdigit() for char in goal)
