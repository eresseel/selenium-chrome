import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Bereslaszlo(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument("headless")
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options)

    
    def test_title(self):
        driver = self.driver
        driver.get("https://www.python.org/")

        self.assertIn("Welcome to Python.org", driver.title)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()