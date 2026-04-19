import gspread
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

def get_client():
    creds = Credentials.from_service_account_file(
        "credentials/google.json",
        scopes=SCOPES
    )
    return gspread.authorize(creds)


def read_sheet(spreadsheet_name: str, sheet_name: str):
    client = get_client()
    spreadsheet = client.open(spreadsheet_name)
    sheet = spreadsheet.worksheet(sheet_name)
    return sheet.get_all_records()