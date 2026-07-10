from datetime import datetime, date, time, timedelta
from app.models.hcp import HCP
from app.models.interaction import Interaction
from app.models.material import Material
from app.models.sample import Sample
from app.models.followup import FollowUp

def parse_date(value):
    if not value:
        return date.today()

    value = value.lower().strip()

    if value == "today":
        return date.today()

    if value == "yesterday":
        return date.today() - timedelta(days=1)

    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except:
        return date.today()


def parse_time(value):
    if not value:
        return None

    try:
        return datetime.strptime(value.upper(), "%I %p").time()
    except:
        pass

    try:
        return datetime.strptime(value.upper(), "%I:%M %p").time()
    except:
        return None

def save_interaction(db, data):
    """
    Save structured AI output into PostgreSQL.
    """

    # -----------------------------
    # Find or Create HCP
    # -----------------------------

    hcp = (
        db.query(HCP)
        .filter(HCP.full_name == data.get("hcp_name", ""))
        .first()
    )

    if not hcp:
        hcp = HCP(
            full_name=data.get("hcp_name", "")
        )

        db.add(hcp)
        db.commit()
        db.refresh(hcp)

    # -----------------------------
    # Interaction
    # -----------------------------

    interaction = Interaction(
        hcp_id=hcp.id,

        interaction_type=data.get("interaction_type", ""),

        interaction_date=parse_date(data.get("interaction_date")),
        interaction_time=parse_time(data.get("interaction_time")),

        attendees=data.get("attendees", ""),

        topics_discussed=data.get("topics_discussed", ""),

        sentiment=data.get("sentiment", ""),

        outcomes=data.get("outcomes", ""),

        follow_up_actions=data.get("follow_up_actions", ""),
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    # -----------------------------
    # Materials
    # -----------------------------

    for item in data.get("materials", []):

        material = Material(
            interaction_id=interaction.id,
            material_name=item,
            material_type="Document",
        )

        db.add(material)

    # -----------------------------
    # Samples
    # -----------------------------

    for item in data.get("samples", []):

        sample = Sample(
            interaction_id=interaction.id,
            sample_name=item,
            quantity=1,
        )

        db.add(sample)

    # -----------------------------
    # Follow Ups
    # -----------------------------

    for item in data.get("followups", []):

        followup = FollowUp(
            interaction_id=interaction.id,
            due_date=None,
            status="Pending",
            notes=item,
        )

        db.add(followup)

    db.commit()

    return {
        "hcp_name": data.get("hcp_name", ""),
        "interaction_type": data.get("interaction_type", ""),
        "interaction_date": str(date.today()),
        "interaction_time": "",
        "attendees": data.get("attendees", ""),
        "topics_discussed": data.get("topics_discussed", ""),
        "sentiment": data.get("sentiment", ""),
        "outcomes": data.get("outcomes", ""),
        "follow_up_actions": data.get("follow_up_actions", ""),
        "materials": data.get("materials", []),
        "samples": data.get("samples", []),
        "followups": data.get("followups", []),
    }