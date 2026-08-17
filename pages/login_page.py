from pages.base_page import BasePage


class LoginPage(BasePage):

    PAGE_NAME = "login_page"

    def open_login_page(self):
        self.open(self.URL)

    def enter_username(self,username):
        self.type_text(self.PAGE_NAME,"username",username)

    def enter_password(self,password):
        self.type_text(self.PAGE_NAME,"password",password)

    def click_login(self):
        self.click(self.PAGE_NAME,"login_button")

    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_text(self.PAGE_NAME,"error_message")

    def is_login_button_displayed(self):
        return self.is_displayed(self.PAGE_NAME,"login_button")