from app.models.hcp import HCP
from app.models.interaction import Interaction
from app.models.material import Material
from app.models.sample import Sample
from app.models.followup import FollowUp


def save_interaction(db, data):
    """
    Save structured AI output into PostgreSQL.
    """

    # ----------------------------------
    # Find or Create HCP
    # ----------------------------------

    hcp = (
        db.query(HCP)
        .filter(HCP.full_name == data["hcp_name"])
        .first()
    )

    if not hcp:
        hcp = HCP(
            full_name=data["hcp_name"]
        )

        db.add(hcp)
        db.commit()
        db.refresh(hcp)

    # ----------------------------------
    # Interaction
    # ----------------------------------

    interaction = Interaction(
        hcp_id=hcp.id,
        interaction_type=data["interaction_type"],
        interaction_date=data["interaction_date"],
        interaction_time=data.get("interaction_time"),
        attendees=data.get("attendees"),
        topics_discussed=data.get("topics_discussed"),
        sentiment=data.get("sentiment"),
        outcomes=data.get("outcomes"),
        follow_up_actions=data.get("follow_up_actions"),
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    # ----------------------------------
    # Materials
    # ----------------------------------

    for item in data.get("materials", []):

        material = Material(
            interaction_id=interaction.id,
            material_name=item,
            material_type="Document",
        )

        db.add(material)

    # ----------------------------------
    # Samples
    # ----------------------------------

    for item in data.get("samples", []):

        sample = Sample(
            interaction_id=interaction.id,
            sample_name=item,
            quantity=1,
        )

        db.add(sample)

    # ----------------------------------
    # Follow Ups
    # ----------------------------------

    for item in data.get("followups", []):

        followup = FollowUp(
            interaction_id=interaction.id,
            status="Pending",
            notes=item,
        )

        db.add(followup)

    db.commit()

    return interaction