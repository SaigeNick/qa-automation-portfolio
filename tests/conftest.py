import pytest
import os
import allure
from datetime import datetime
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument("--headless")  # Запуск без вікна (важливо для сервера!)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")  # Імітуємо Full HD екран

    print("\nStarting Chrome Driver (Headless)")
    my_driver = webdriver.Chrome(options=options)
    yield my_driver
    my_driver.quit()

@pytest.fixture
def auto_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Якщо це фаза виконання тесту і він впав
    if report.when == 'call' and report.failed:
        # 1. Дістаємо драйвер з аргументів функції (надійніше для pytest фікстур)
        driver = item.funcargs.get('driver', None)

        if driver:
            # 2. Беремо скріншот як байти (PNG), не зберігаючи файл на диск
            png_bytes = driver.get_screenshot_as_png()

            # 3. Атачимо байти
            allure.attach(
                png_bytes,
                name="Screenshot on Failure",
                attachment_type=allure.attachment_type.PNG
            )