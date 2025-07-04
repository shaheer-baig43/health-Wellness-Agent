from builtins import str
from pydantic import BaseModel
from typing import Optional, List, Dict

class UserSessionContext(BaseModel):
    email: str
    goal: Optional[str] = None
    diet_preferences: Optional[str] = None
    injury_notes: Optional[str] = None
    meal_plan: Optional[str] = None
    workout_plan: Optional[str] = None
    handoffs: List[str] = []
    progress_logs: List[Dict[str, str]] = []
