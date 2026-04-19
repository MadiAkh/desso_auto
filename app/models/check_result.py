from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base


class CheckResult(Base):
    __tablename__ = "check_results"

    id = Column(Integer, primary_key=True, index=True)

    order_id = Column(Integer, nullable=True)

    status = Column(String)  # ok / error

    error_type = Column(String)  # bank / bitrix / cash / items

    description = Column(String)