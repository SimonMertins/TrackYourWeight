import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('track_your_weight')


def get_old_data():
    """
    Get old weight input from user
    """
    print("Please enter your weight in Kg.")
    print("Exampel: 75.6\n")

    data_str = input("Enter your old weight here: ")
    print(f"Your old weight is {data_str}Kg")


get_old_data()