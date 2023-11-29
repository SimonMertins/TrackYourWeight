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
    print("Exampel: 72.0 or 75.6\n")

    data_str = input("Enter your old weight here: ")

    old_data = data_str.split(",")
    validate_data(old_data)


def validate_data(weight):
    """
    Convert string data into integers and raise ValueError
    if wrong value is entered
    """
    try:
        if len(weight) != 1:
            raise ValueError(
                f"Only 1 weight required, you provided {len(weight)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")


get_old_data()
