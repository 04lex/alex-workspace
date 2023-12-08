from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class TestFacebookLogin(unittest.TestCase):

    def setUp(self):
        # selenium cfg
        self.driver = webdriver.Chrome()
        self.driver.get("https://google.com/")

    def test_facebook_login(self):
        # caut search box
        search_box = self.driver.find_element("name", "q")
        search_box.send_keys("facebook")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2) # astept results

        # caut link fb si il accesez
        facebook_link = self.driver.find_element("https://facebook.com/", "Facebook")
        facebook_link.click()

        # caut auth box
        email_input = self.driver.find_element("name", "email")
        password_input = self.driver.find_element("name", "pass")
        email_input.send_keys("invalidemail")
        password_input.send_keys("invalidpassword")

        # trimit auth form
        password_input.send_keys(Keys.RETURN)
        time.sleep(2) # astept results

        # verific daca exista mesajul pentru date incorecte
        error_message = self.driver.find_element("xpath", "//div[text()='The email address or mobile number you entered isn’t connected to an account. Find your account and log in.']")

        self.assertTrue(error_message.is_displayed(), "Mesajul de autentificare gresita nu a fost chemat")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()