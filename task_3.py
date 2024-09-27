import re


def normalize_phone(phone_number: str):
    # Remove '+' at the beginning if present, after remove '38' if present, and remove any characters that are not digits
    phone_number = re.sub(r"^\+?38?|[^\d]", "", phone_number)

    # Return adjusted phone_number with +38 on the beginning
    return f"+38{phone_number}"


raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    " +38(050)123-32-34",
    " 0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11 ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS campaigns:", sanitized_numbers)
