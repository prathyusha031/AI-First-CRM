from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.database.database import Base


class FollowUp(Base):
    __tablename__ = "followups"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    interaction_id = Column(
        Integer,
        ForeignKey("interactions.id"),
        nullable=False,
    )

    due_date = Column(
        Date,
        nullable=True,
    )

    status = Column(
        String(50),
        default="Pending",
    )

    notes = Column(
        String(500),
        nullable=True,
    )

    interaction = relationship(
        "Interaction",
        back_populates="followups",
    )