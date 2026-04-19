from fastapi import FastAPI
from app.core.database import engine, Base
from sqlalchemy import text

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.payment import Payment
from app.models.cash_report import CashReport
from app.models.check_result import CheckResult


app = FastAPI(title="Desso Finance Control")

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"result": [row[0] for row in result]}

Base.metadata.create_all(bind=engine)

