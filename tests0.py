from prime import is_prime  # Import the is_prime function from the prime module


def test_prime(n, expected):  # Define a function that takes a number and an expected value
    if is_prime(n) != expected:  # Check if the result of is_prime(n) matches the expected value
        print(f"ERROR on is_prime({n}), expected {expected}")  # If the expected value is not matched, print an error message
