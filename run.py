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
        print("Example: 72 or 75.8\n")

        data_str = input("Enter your old weight here:\n")

        old_data = data_str.split(",")

        if validate_data(old_data):
            print("Weight is valid!")
            break

    return old_data


def get_new_data():
    """
    Get new weight input from user
    """
    while True:
        print("Please enter your weight in Kg.")
        print("Example: 72 or 75.8\n")

        data_str = input("Enter your new weight here:\n")

        new_data = data_str.split(",")

        if validate_data(new_data):
            print("Weight is valid!")
            break

    return new_data


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


def update_new_worksheet(data):
    """
    Update new weight worksheet, with the weight provided by the user.
    """
    print("Updating new weight worksheet...\n")
    new_worksheet = SHEET.worksheet("new")
    new_worksheet.append_row(data)
    print("New weight added successfully!\n")


def calculate_and_update_difference(old_weight, new_weight):
    """
    Calculate the difference between old weight and new weight,
    print the result and update the difference worksheet
    """
    difference = new_weight - old_weight
    print(f"You have {'gained' if difference > 0 else 'lost'} "
          f"{abs(difference)} Kg.")

    difference_worksheet = SHEET.worksheet("difference")
    difference_worksheet.append_row([difference])
    print("Difference successfully added to worksheet.\n")


def main():
    """
    For old weight
    """
    data = get_old_data()
    old_data = [float(num) for num in data]
    update_old_worksheet(old_data)
    """
    For new weight
    """
    data = get_new_data()
    new_data = [float(num) for num in data]
    update_new_worksheet(new_data)
    """
    For difference
    """
    calculate_and_update_difference(old_data[0], new_data[0])


print("Welcome to Track Your Weight!")
main()
