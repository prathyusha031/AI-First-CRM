from datetime import date, time
from typing import List, Optional

from pydantic import BaseModel


class MaterialItem(BaseModel):
    material_name: str
    material_type: Optional[str] = None


class SampleItem(BaseModel):
    sample_name: str
    quantity: Optional[int] = None


class FollowUpItem(BaseModel):
    due_date: Optional[date] = None
    status: Optional[str] = "Pending"
    notes: Optional[str] = None


class InteractionCreate(BaseModel):
    hcp_name: str
    interaction_type: str
    interaction_date: date
    interaction_time: Optional[time] = None

    attendees: Optional[str] = None
    topics_discussed: Optional[str] = None

    sentiment: Optional[str] = None
    outcomes: Optional[str] = None
    follow_up_actions: Optional[str] = None

    materials: List[MaterialItem] = []
    samples: List[SampleItem] = []
    followups: List[FollowUpItem] = []


class InteractionResponse(InteractionCreate):
    id: int

    class Config:
        from_attributes = True