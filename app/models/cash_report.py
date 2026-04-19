from sqlalchemy import Column, Integer, Float, DateTime, String, ForeignKey
from app.core.database import Base


class CashReport(Base):
    __tablename__ = "cash_reports"

    id = Column(Integer, primary_key=True, index=True)

    employee = Column(String)  # имя сотрудника
    order_id = Column(String)  # ID заказа из таблицы (пока строка)

    amount = Column(Float)
    date = Column(DateTime)

    payment_type = Column(String)  # cash / kaspi / card