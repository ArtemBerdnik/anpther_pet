import allure
import pytest
from selenium.webdriver.android.webdriver import WebDriver

from pageobjects.MainPage import MainPage


@pytest.mark.smoke
@allure.parent_suite("Tests for 'Tables' page")
@allure.suite("Tests for general functionality")
@allure.title("Test only tables displayed in 'Tables' page")
def test_only_tables_displayed(driver: WebDriver):
    MainPage(driver) \
        .open_page() \
        .open_tables_page() \
        .assert_only_tables_displayed()
