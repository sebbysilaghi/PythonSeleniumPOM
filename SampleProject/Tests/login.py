import unittest
import HtmlTestRunner

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from SampleProject.Pages.loginPage import LoginPage
from SampleProject.Pages.homePage import HomePage


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        home_page = HomePage(driver)
        home_page.click_welcome()
        home_page.click_logout()

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


# If you are running tests from command line / terminal the following lines will be helpful to use a shorter command

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="SampleProject/Results"))
