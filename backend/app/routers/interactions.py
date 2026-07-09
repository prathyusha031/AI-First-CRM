from fastapi import APIRouter, HTTPException

from app.graph import crm_graph
from app.schemas.interaction import InteractionCreate

router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"],
)


@router.post("/log")
def log_interaction(request: InteractionCreate):

    state = {
        "user_input": (
            f"""
HCP Name: {request.hcp_name}

Interaction Type: {request.interaction_type}

Date: {request.interaction_date}

Time: {request.interaction_time}

Attendees: {request.attendees}

Topics Discussed:
{request.topics_discussed}

Sentiment:
{request.sentiment}

Outcomes:
{request.outcomes}

Follow Up:
{request.follow_up_actions}
"""
        ),
        "action": "log_interaction",
        "structured_data": None,
        "response": None,
        "error": None,
    }

    result = crm_graph.invoke(state)

    if result.get("error"):
        raise HTTPException(
            status_code=500,
            detail=result["error"],
        )

    return result["structured_data"]