from fastapi import APIRouter

from app.schemas.interaction import (
    InteractionCreate,
    InteractionResponse,
)

router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"],
)


@router.post(
    "/log",
    response_model=InteractionResponse,
)
async def log_interaction(
    interaction: InteractionCreate,
):
    """
    Temporary endpoint.

    Later this request will go to LangGraph.
    """

    return InteractionResponse(
        id=1,
        **interaction.model_dump(),
    )