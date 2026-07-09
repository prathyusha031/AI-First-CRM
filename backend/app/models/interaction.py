from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Date,
    Time,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.database.database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    hcp_id = Column(
        Integer,
        ForeignKey("hcp.id"),
        nullable=False,
    )

    interaction_type = Column(
        String(100),
        nullable=False,
    )

    interaction_date = Column(
        Date,
        nullable=False,
    )

    interaction_time = Column(
        Time,
        nullable=True,
    )

    attendees = Column(
        Text,
        nullable=True,
    )

    topics_discussed = Column(
        Text,
        nullable=True,
    )

    sentiment = Column(
        String(30),
        nullable=True,
    )

    outcomes = Column(
        Text,
        nullable=True,
    )

    follow_up_actions = Column(
        Text,
        nullable=True,
    )

    hcp = relationship(
    "HCP",
    back_populates="interactions",
)

materials = relationship(
    "Material",
    back_populates="interaction",
    cascade="all, delete-orphan",
)

samples = relationship(
    "Sample",
    back_populates="interaction",
    cascade="all, delete-orphan",
)

followups = relationship(
    "FollowUp",
    back_populates="interaction",
    cascade="all, delete-orphan",
)

    # These relationships will be enabled
    # after we create the corresponding models.

    # materials = relationship(
    #     "Material",
    #     back_populates="interaction",
    #     cascade="all, delete-orphan",
    # )

    # samples = relationship(
    #     "Sample",
    #     back_populates="interaction",
    #     cascade="all, delete-orphan",
    # )

    # followups = relationship(
    #     "FollowUp",
    #     back_populates="interaction",
    #     cascade="all, delete-orphan",
    # )