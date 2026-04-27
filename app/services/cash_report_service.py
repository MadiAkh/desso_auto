from app.models.cash_report import CashReport
from app.core.database import SessionLocal


def save_cash_reports(data: list):
    db = SessionLocal()

    for item in data:
        report = CashReport(
            order_id=item["order_id"],
            date=item["date"],
            payment_type=item["payment_type"],
            amount=item["amount"]
        )
        db.add(report)

    db.commit()
    db.close()