from datetime import datetime


def get_days_from_today(date: str):
    try:
        # Parsing a date string into a date object
        date_obj = datetime.strptime(date, "%Y-%m-%d")
    except:
        print("Date format is not supported, use YYYY-MM-DD format")
        return 0

    # Get the current date
    today = datetime.now()
    # Find a difference
    difference = today - date_obj
    # Return a difference in days
    return difference.days


print(get_days_from_today("2023-09-27"))
