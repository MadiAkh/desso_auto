from fastapi import FastAPI
from app.core.database import engine, Base
from sqlalchemy import text

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.payment import Payment
from app.models.cash_report import CashReport
from app.models.check_result import CheckResult
from app.integrations.google_sheets import read_sheet
from app.services.sheet_parser import normalize_data
from app.services.cash_report_service import save_cash_reports


app = FastAPI(title="Desso Finance Control")

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"result": [row[0] for row in result]}

# Base.metadata.create_all(bind=engine)

@app.get("/test-sheets")
def test_sheets():
    data = read_sheet(
        spreadsheet_id="1dZjOshFx1AZAafBPmeuYpzbFmqz6b_OoU1Z2sza_UVU",
        sheet_name="Касса"
    )

    normalized = normalize_data(data)

    return {"rows": normalized[:5]}


@app.get("/ping")
def ping():
    print("PING WORKED")
    return {"ok": True}

@app.get("/")
def root():
    return {"ok": True}


@app.get("/import-sheets")
def import_sheets():
    data = read_sheet(
        spreadsheet_id="1dZjOshFx1AZAafBPmeuYpzbFmqz6b_OoU1Z2sza_UVU",
        sheet_name="Касса"
    )

    normalized = normalize_data(data)

    save_cash_reports(normalized)

    return {"saved": len(normalized)}

