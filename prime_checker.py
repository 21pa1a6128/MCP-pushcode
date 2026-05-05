def is_prime(number: int) -> bool:
    """Return True if number is prime, otherwise False."""
    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    try:
        value = int(input("Enter a number: "))
        print(f"{value} is prime: {is_prime(value)}")
    except ValueError:
        print("Please enter a valid integer.")
