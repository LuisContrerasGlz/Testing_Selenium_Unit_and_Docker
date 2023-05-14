import math  # Import the math module

def is_prime(n):
    """Determines if a non-negative integer is prime."""
    if n < 2:  # Check if the input is less than 2
        return False  # If so, it's not prime, so return False
    for i in range(2, int(math.sqrt(n)) + 1):  # Iterate through the range 2 to the square root of n + 1
        if n % i == 0:  # Check if n is divisible by i
            return False  # If so, n is not prime, so return False
    return True  # If n is not divisible by any number between 2 and the square root of n, it's prime, so return True
