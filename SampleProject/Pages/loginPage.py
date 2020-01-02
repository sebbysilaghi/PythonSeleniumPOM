class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Objects

        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"

        self.invalidCredentials_message_id = "spanMessage"

    # Actions with objects

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()
        self.driver.implicitly_wait(2)

    def return_invalidCredential_message(self):
        self.driver.find_element_by_id(self.invalidCredentials_message_id).text
