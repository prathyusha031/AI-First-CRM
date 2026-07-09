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

    state = {
        "user_input": request.message,
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

    structured_data = result["structured_data"]

    save_interaction(
        db=db,
        data=structured_data,
    )

    return structured_data