from pages.login_page import LoginPage
import os
from dotenv import load_dotenv

load_dotenv()

def test_login_page(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(os.getenv("USER_LOGIN"), os.getenv("USER_PASSWORD"))
    assert "inventory" in driver.current_url, "Ми не перейшли на сторінку інвентаря!"
