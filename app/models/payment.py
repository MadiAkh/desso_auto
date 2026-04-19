from sqlalchemy import Column, Integer, Float, DateTime, String
from app.core.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    amount = Column(Float)
    date = Column(DateTime)

    source = Column(String)  # bank / cash
    description = Column(String, nullable=True)