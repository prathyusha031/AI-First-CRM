import json

from app.agents.state import CRMState
from app.services.groq_service import llm


SYSTEM_PROMPT = """
You are an AI CRM Assistant.

Convert the user's natural language into structured CRM JSON.

Return ONLY valid JSON.

Extract:

{
  "hcp_name":"",
  "interaction_type":"",
  "interaction_date":"",
  "interaction_time":"",
  "attendees":"",
  "topics_discussed":"",
  "sentiment":"",
  "outcomes":"",
  "follow_up_actions":"",
  "materials":[],
  "samples":[],
  "followups":[]
}

Do not explain.
Do not use markdown.
Return JSON only.
"""


def log_interaction_node(state: CRMState):

    prompt = f"""
{SYSTEM_PROMPT}

User Input:

{state["user_input"]}
"""

    response = llm.invoke(prompt)

    try:

        structured = json.loads(response.content)

        state["structured_data"] = structured

    except Exception:

        state["error"] = "Invalid JSON returned from LLM."

    return state