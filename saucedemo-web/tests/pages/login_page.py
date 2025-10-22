class LoginPage:
    URL = "https://www.saucedemo.com/"
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"
    ERROR_MSG = "[data-test='error']"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME, username)
        self.page.fill(self.PASSWORD, password)
        self.page.click(self.LOGIN_BTN)

    def error_text(self):
        el = self.page.locator(self.ERROR_MSG)
        return el.text_content() if el.count() else ""
