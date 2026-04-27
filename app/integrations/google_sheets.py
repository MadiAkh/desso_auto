import gspread
from google.oauth2.service_account import Credentials
import os

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# абсолютный путь к корню проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

CREDS_PATH = os.path.join(BASE_DIR, "credentials", "google.json")


def get_client():
    creds = Credentials.from_service_account_file(
        CREDS_PATH,
        scopes=SCOPES
    )
    return gspread.authorize(creds)


def read_sheet(spreadsheet_id: str, sheet_name: str):
    print("1. start")
    
    client = get_client()
    print("2. client created")

    spreadsheet = client.open_by_key(spreadsheet_id)
    print("3. spreadsheet opened")

    sheet = spreadsheet.worksheet(sheet_name)
    print("4. worksheet opened")

    data = sheet.get_all_values()
    print("5. data fetched")
    return data