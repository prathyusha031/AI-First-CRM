from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from typing import TypedDict
from dotenv import load_dotenv
import os
import json

load_dotenv()

llm = ChatGroq(
    model="gemma2-9b-it",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)


class CRMState(TypedDict):
    user_input: str
    crm_json: dict


PROMPT = """
You are an AI Healthcare CRM assistant.

Extract ONLY the following JSON.

{
"hcp_name":"",
"interaction_type":"",
"date":"",
"time":"",
"topics_discussed":"",
"materials_shared":"",
"samples_distributed":"",
"sentiment":"",
"outcomes":"",
"follow_up":""
}

Return ONLY JSON.

User:
"""


def log_interaction(state: CRMState):

    response = llm.invoke(PROMPT + state["user_input"])

    try:
        data = json.loads(response.content)
    except Exception:
        data = {
            "hcp_name": "",
            "interaction_type": "",
            "date": "",
            "time": "",
            "topics_discussed": "",
            "materials_shared": "",
            "samples_distributed": "",
            "sentiment": "",
            "outcomes": "",
            "follow_up": ""
        }

    return {
        "crm_json": data
    }


builder = StateGraph(CRMState)

builder.add_node("log_interaction", log_interaction)

builder.set_entry_point("log_interaction")

builder.add_edge("log_interaction", END)

graph = builder.compile()