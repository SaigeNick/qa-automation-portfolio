from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com"

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click_elem(self.BUTTON)
