from sqlalchemy import Column, Integer, String, Float, DateTime
from app.core.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    bitrix_id = Column(String, unique=True, index=True)

    amount = Column(Float)
    payment_amount = Column(Float)

    delivery_date = Column(DateTime)

    status = Column(String, default="new")

    