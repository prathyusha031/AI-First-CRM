from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class HCP(Base):
    __tablename__ = "hcp"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(255), nullable=False)

    specialty = Column(String(150), nullable=True)

    hospital = Column(String(255), nullable=True)

    city = Column(String(100), nullable=True)

    email = Column(String(255), nullable=True)

    phone = Column(String(30), nullable=True)

    interactions = relationship(
        "Interaction",
        back_populates="hcp",
        cascade="all, delete-orphan",
    )