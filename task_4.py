from typing import TypedDict
from datetime import datetime, timedelta


class User(TypedDict):
    name: str
    birthday: str


users: list[User] = [
    {"name": "John Doe", "birthday": "1985.10.02"},
    {"name": "Jane Smith", "birthday": "1990.09.05"},
]


def get_upcoming_birthdays(users):
    # Get the current date
    today = datetime.today().date()
    # Initialize the list for upcoming birthdays
    upcoming_birthdays = []

    # Iterate over all users
    for user in users:
        # Parse the user's birthday from string to datetime object
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Replace year in birthday with the current year
        birthday_this_year = birthday.replace(year=today.year)

        # Check if the birthday is within the next 7 days
        if 0 <= (birthday_this_year - today).days <= 7:
            # If the birthday falls on a weekend (Saturday=5, Sunday=6), move it to Monday
            if birthday_this_year.weekday() >= 5:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            # Add the user's name and the adjusted congratulation date to the list
            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": birthday_this_year.strftime("%Y.%m.%d"),
                }
            )

    return upcoming_birthdays


upcoming_birthdays = get_upcoming_birthdays(users)

print("List of users that have birthday on this week:", upcoming_birthdays)
