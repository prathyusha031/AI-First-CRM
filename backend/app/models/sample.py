from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.database.database import Base


class Sample(Base):
    __tablename__ = "samples"

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

    sample_name = Column(
        String(255),
        nullable=False,
    )

    quantity = Column(
        Integer,
        nullable=True,
    )

    interaction = relationship(
        "Interaction",
        back_populates="samples",
    )