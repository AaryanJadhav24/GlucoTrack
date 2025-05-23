from pydantic import BaseModel
from typing import Optional

class LogEntry(BaseModel):
    date: str  # e.g. "2025-05-20"
    glucose: Optional[float]
    meals: Optional[str]
    activity: Optional[str]
    sleep_hours: Optional[float]
