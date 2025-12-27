import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_elem(self, locator):
        wait = WebDriverWait(self.driver, 10)
        elem = wait.until(EC.visibility_of_element_located(locator))
        return elem

    @allure.step("Клікаю по елементу: {locator}")
    def click_elem(self, locator):
        elem = self.wait_for_elem(locator)
        elem.click()

    @allure.step("Вводжу текст в елемент: {locator}")
    def enter_text(self, locator, data):
        elem = self.wait_for_elem(locator)
        elem.clear()
        elem.send_keys(data)

    @allure.step("Отримую текст з елементу: {locator}")
    def get_text(self, locator):
        elem = self.wait_for_elem(locator)
        return elem.text