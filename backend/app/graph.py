from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from typing import TypedDict
from dotenv import load_dotenv
import os
import json

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY"),
)


class CRMState(TypedDict):
    user_input: str
    crm_json: dict


PROMPT = """
You are an AI Healthcare CRM Assistant.

Extract the interaction into ONLY valid JSON.

STRICT RULES

1. Return ONLY JSON.
2. Do NOT explain anything.
3. Do NOT use markdown.
4. Never return null.
5. Unknown values should be "" or [].

Date Rules
- Convert relative dates.
- today -> current date in YYYY-MM-DD
- yesterday -> previous date in YYYY-MM-DD
- tomorrow -> next date in YYYY-MM-DD
- next Tuesday -> actual YYYY-MM-DD date

Time Rules
- Convert every time to 24-hour format.
- 2 PM -> 14:00
- 11 AM -> 11:00
- 9:30 PM -> 21:30

Interaction Type
- met -> Meeting
- meeting -> Meeting
- called -> Call
- phone -> Call
- emailed -> Email

Sentiment
Must be exactly one of:

Positive
Neutral
Negative

Extract:

- hcp_name
- interaction_type
- interaction_date
- interaction_time
- attendees
- topics_discussed
- sentiment
- outcomes
- follow_up_actions
- materials
- samples
- followups

Return EXACTLY this JSON format:

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

User:
"""


def log_interaction(state: CRMState):

    response = llm.invoke(PROMPT + state["user_input"])

    print("\n========== RAW LLM RESPONSE ==========")
    print(response.content)
    print("======================================\n")

    text = response.content.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "").strip()

    start = text.find("{")
    end = text.rfind("}")

    if start != -1 and end != -1:
        text = text[start:end + 1]

    try:
        data = json.loads(text)

    except Exception as e:

        print("JSON ERROR:", e)

        data = {}

    return {
        "crm_json": {
            "hcp_name": data.get("hcp_name", ""),
            "interaction_type": data.get("interaction_type", ""),
         "interaction_date": data.get("interaction_date", ""),
"interaction_time": data.get("interaction_time", ""),
            "attendees": "",
            "topics_discussed": data.get("topics_discussed", ""),
            "sentiment": data.get("sentiment", ""),
            "outcomes": data.get("outcomes", ""),
           "follow_up_actions": data.get("follow_up_actions", ""),
            "materials": data.get("materials", []),
            "samples": data.get("samples", []),
            "followups": data.get("followups", []),
        }
    }


def edit_interaction(state: CRMState):

    response = llm.invoke(
        "Update ONLY the requested CRM fields.\n\n"
        + state["user_input"]
    )

    return {
        "crm_json": {
            "message": response.content
        }
    }


def search_hcp_history(state: CRMState):

    response = llm.invoke(
        "Answer the user's CRM history request.\n\n"
        + state["user_input"]
    )

    return {
        "crm_json": {
            "history": response.content
        }
    }


def generate_followup(state: CRMState):

    response = llm.invoke(
        "Generate follow-up suggestions.\n\n"
        + state["user_input"]
    )

    return {
        "crm_json": {
            "followup": response.content
        }
    }


def generate_summary(state: CRMState):

    response = llm.invoke(
        "Summarize this CRM interaction.\n\n"
        + state["user_input"]
    )

    return {
        "crm_json": {
            "summary": response.content
        }
    }


builder = StateGraph(CRMState)

builder.add_node("log_interaction", log_interaction)
builder.add_node("edit_interaction", edit_interaction)
builder.add_node("search_hcp_history", search_hcp_history)
builder.add_node("generate_followup", generate_followup)
builder.add_node("generate_summary", generate_summary)

builder.set_entry_point("log_interaction")

builder.add_edge("log_interaction", END)
builder.add_edge("edit_interaction", END)
builder.add_edge("search_hcp_history", END)
builder.add_edge("generate_followup", END)
builder.add_edge("generate_summary", END)

crm_graph = builder.compile()