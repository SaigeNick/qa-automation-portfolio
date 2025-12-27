from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    ADD_TO_CART_BUTTON  = (By.ID, "addd-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def __init__(self, driver):
        super().__init__(driver)

    def add_backpack_to_cart(self):
        self.click_elem(self.ADD_TO_CART_BUTTON)

    def get_cart_text(self):
        cart_text = self.get_text(self.CART_BADGE)
        return cart_text