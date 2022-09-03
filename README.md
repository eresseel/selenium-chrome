# selenium-chrome-image

Selenium is a suite of tools for automating web browsers.

- Read the documentation and more at https://www.selenium.dev/documentation/
- Open Docker Hub at https://hub.docker.com/r/eresseel/selenium-chrome

## Available Docker image versions

The following Selenium Docker images are as small as possible and only contain Selenium and Chrome browser itself.

| Docker tag                        | Debian from   | Python from    | Build from                                |
| --------------------------------- | ------------- | ---------------| ----------------------------------------- |
| `latest`                          | Debian Buster | Python 3.10.6  | Latest stable Selenium version            |
| `4.4.3`                           | Debian Buster | Python 3.10.6  | Selenium 4.4.3 version      |


## Docker run commands

```bash
docker run --rm -it -v ${PWD}:/ws -w /ws eresseel/selenium-chrome:latest bash
```

## Selenium test example

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class SeleniumTest(unittest.TestCase):
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

        self.assertIn("Welcome to Python.org", driver.title.text)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
```