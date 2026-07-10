from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.graph import crm_graph
from app.schemas.interaction import ChatRequest
from app.services.interaction_service import save_interaction

router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"],
)


@router.post("/log")
def log_interaction(
    request: ChatRequest,
    db: Session = Depends(get_db),
):

    message = request.message.lower()

    # ----------------------------
    # Decide which LangGraph tool
    # ----------------------------

    if "edit" in message or "update" in message or "change" in message:
        action = "edit_interaction"

    elif "history" in message or "previous" in message:
        action = "search_hcp_history"

    elif "summary" in message:
        action = "generate_summary"

    elif "follow-up" in message or "follow up" in message or "suggest" in message:
        action = "generate_followup"

    else:
        action = "log_interaction"

    # ----------------------------
    # Run LangGraph
    # ----------------------------

    result = crm_graph.invoke(
        {
            "user_input": request.message,
            "crm_json": {},
        }
    )

    structured_data = result.get("crm_json", {})

    if not structured_data:
        raise HTTPException(
            status_code=500,
            detail="AI failed to process the request.",
        )

    # ----------------------------
    # Save ONLY new interactions
    # ----------------------------

    if action == "log_interaction":

        save_interaction(
            db=db,
            data=structured_data,
        )

    # ----------------------------
    # Return AI response
    # ----------------------------

    return structured_data