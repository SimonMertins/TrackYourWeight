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
    while True:
        print("Please enter your weight in Kg.")
        print("Exampel: 72.0 or 75.8\n")

        data_str = input("Enter your old weight here: ")

        old_data = data_str.split(",")

        if validate_data(old_data):
            print("Weight is valid!")
            break

    return old_data


def validate_data(weight):
    """
    Convert string data into float and raise ValueError
    if wrong value is entered
    """
    try:
        [float(weight) for weight in weight]
        if len(weight) != 1:
            raise ValueError(
                f"Only 1 weight required, you provided {len(weight)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")
        return False

    return True


def update_old_worksheet(data):
    """
    Update old weight worksheet, with the weight provided by the user.
    """
    print("Updating old weight worksheet...\n")
    old_worksheet = SHEET.worksheet("old")
    old_worksheet.append_row(data)
    print("Old weight added successfully!\n")


data = get_old_data()
old_data = [float(num) for num in data]
update_old_worksheet(old_data)
