from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.interaction import ChatRequest
from app.services.interaction_service import save_interaction

from app.graph import (
    log_interaction,
    edit_interaction,
    search_hcp_history,
    generate_followup,
    generate_summary,
)

router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"],
)


@router.post("/log")
def interaction_router(
    request: ChatRequest,
    db: Session = Depends(get_db),
):

    message = request.message.lower()

    state = {
        "user_input": request.message,
        "crm_json": {},
    }

    # -------------------------
    # Decide which tool to run
    # -------------------------

    if "edit" in message or "update" in message or "change" in message:

        result = edit_interaction(state)

        return result["crm_json"]

    elif "history" in message or "previous" in message:

        result = search_hcp_history(state)

        return result["crm_json"]

    elif "summary" in message:

        result = generate_summary(state)

        return result["crm_json"]

    elif (
           "suggest follow-up" in message
           or "suggest follow up" in message
           or "generate follow-up" in message
           or "generate follow up" in message
    ):

        result = generate_followup(state)

        return result["crm_json"]

    # -------------------------
    # Default → Log Interaction
    # -------------------------

    result = log_interaction(state)

    structured_data = result["crm_json"]

    save_interaction(
        db=db,
        data=structured_data,
    )

    return structured_data