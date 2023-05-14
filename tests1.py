import unittest  # Import the unittest module
from prime import is_prime  # Import the is_prime function from the prime module

class Tests(unittest.TestCase):  # Define a test class that inherits from unittest.TestCase

    def test_1(self):  # Define a test method
        """Check that 1 is not prime."""  # Add a docstring to describe the test
        self.assertFalse(is_prime(1))  # Use the assertFalse method to verify that is_prime(1) returns False

    def test_2(self):  # Define another test method
        """Check that 2 is prime."""
        self.assertTrue(is_prime(2))  # Use the assertTrue method to verify that is_prime(2) returns True

    def test_8(self):  # Define another test method
        """Check that 8 is not prime."""
        self.assertFalse(is_prime(8))  # Use the assertFalse method to verify that is_prime(8) returns False

    def test_11(self):  # Define another test method
        """Check that 11 is prime."""
        self.assertTrue(is_prime(11))  # Use the assertTrue method to verify that is_prime(11) returns True

    def test_25(self):  # Define another test method
        """Check that 25 is not prime."""
        self.assertFalse(is_prime(25))  # Use the assertFalse method to verify that is_prime(25) returns False

    def test_28(self):  # Define another test method
        """Check that 28 is not prime."""
        self.assertFalse(is_prime(28))  # Use the assertFalse method to verify that is_prime(28) returns False


if __name__ == "__main__":  # Check if this module is being run as the main program
    unittest.main()  # Run the tests defined in the Tests class using the unittest framework
