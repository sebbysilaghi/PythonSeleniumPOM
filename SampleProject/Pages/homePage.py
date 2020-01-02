class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # Objects
        self.welcome_link_id = "welcome"
        self.logout_link_xpath = "//*[@id='welcome-menu']/ul/li[2]/a"

    # Actions

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()
        self.driver.implicitly_wait(5)

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()
        self.driver.implicitly_wait(2)
