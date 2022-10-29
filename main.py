import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import warnings


class RihareSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def test_search(self):
        driver = self.driver
        driver.get("https://riigihanked.riik.ee/rhr-web/#/")
        self.assertIn('Riigihangete register', driver.title)
        search_input = driver.find_element(By.XPATH, '/html/body/div[2]/rhr-front-page/rhr-main-content/main/ng-transclude/div[1]/div/form/input')
        search_input.send_keys('<iframe src="javascript:alert(`xss`)">')
        search_input.send_keys(Keys.RETURN)
        try:
            WebDriverWait(driver, 5).until(ec.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

            alert = driver.switch_to.alert
            alert.accept()
            print("alert accepted")
        except TimeoutException:
            print("no alert")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
