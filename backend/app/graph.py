from langgraph.graph import StateGraph, END

from app.agents.state import CRMState
from app.agents.nodes import log_interaction_node


workflow = StateGraph(CRMState)

workflow.add_node(
    "log_interaction",
    log_interaction_node,
)

workflow.set_entry_point("log_interaction")

workflow.add_edge(
    "log_interaction",
    END,
)

crm_graph = workflow.compile()