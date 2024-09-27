import random


def get_numbers_ticket(min: int, max: int, quantity: int):
    # Check if min and max values are in range of 1-1000 and quantity is greater than or equal 1 and less than or equal to max amount of unique numbers in range from min and max values
    if 1 <= min < max <= 1000 and 1 <= quantity <= (max - min + 1):
        # Select unique numbers from given range
        numbers = random.sample(range(min, max + 1), quantity)
        # Return sorted list
        return sorted(numbers)

    return []


lottery_numbers = get_numbers_ticket(1, 36, 5)
print(f"Your lottery numbers: {lottery_numbers}")
