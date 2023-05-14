import os
import pathlib
import unittest

from selenium import webdriver

# Define a function to convert a filename to a file URI
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Define a new test case for a web page
class WebpageTests(unittest.TestCase):

    # Define a test method to check the page title
    def test_title(self):
        driver.get(file_uri("counter.html"))  # Load the web page
        self.assertEqual(driver.title, "Counter")  # Check that the page title is "Counter"

    # Define a test method to check the "increase" button
    def test_increase(self):
        driver.get(file_uri("counter.html"))  # Load the web page
        increase = driver.find_element_by_id("increase")  # Find the "increase" button element
        increase.click()  # Click the "increase" button
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")  # Check that the counter value is now 1

    # Define a test method to check the "decrease" button
    def test_decrease(self):
        driver.get(file_uri("counter.html"))  # Load the web page
        decrease = driver.find_element_by_id("decrease")  # Find the "decrease" button element
        decrease.click()  # Click the "decrease" button
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "-1")  # Check that the counter value is now -1

    # Define a test method to check multiple "increase" button clicks
    def test_multiple_increase(self):
        driver.get(file_uri("counter.html"))  # Load the web page
        increase = driver.find_element_by_id("increase")  # Find the "increase" button element
        for i in range(3):
            increase.click()  # Click the "increase" button three times
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "3")  # Check that the counter value is now 3

# Run the test case if this file is executed as the main program
if __name__ == "__main__":
    unittest.main()
