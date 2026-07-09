from typing import TypedDict, Optional


class CRMState(TypedDict):
    user_input: str

    action: Optional[str]

    structured_data: Optional[dict]

    response: Optional[dict]

    error: Optional[str]