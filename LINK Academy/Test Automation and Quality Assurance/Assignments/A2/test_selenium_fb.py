from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestFacebookLogin(unittest.TestCase):

    def setUp(self):
        # selenium
        self.driver = webdriver.Chrome(executable_path)
        self.driver.get("https://www.google.com/")

    def test_facebook_login(self):

        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("facebook")
        search_box.send_keys(Keys.RETURN)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Facebook")))
        facebook_link = self.driver.find_element_by_partial_link_text("Facebook")
        facebook_link.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        email_input = self.driver.find_element(By.NAME, "email")
        
        email_input.clear()
        email_input.send_keys("invalidemail")

        password_input = self.driver.find_element(By.NAME, "pass")
        password_input.send_keys("invalidpassword")

        # auth
        password_input.send_keys(Keys.RETURN)

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='The email address or mobile number you entered isn’t connected to an account. Find your account and log in.']")))
        error_message = self.driver.find_element_by_xpath("//div[text()='The email address or mobile number you entered isn’t connected to an account. Find your account and log in.']")

        self.assertTrue(error_message.is_displayed(), "Mesajul de autentificare greșită nu a fost afișat")

    def tearDown(self):
        # reset
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
