from pages.login_page import LoginPage

def test_login_page(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url, "Ми не перейшли на сторінку інвентаря!"
