import allure
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageobjects.BasePage import BasePage
from pageobjects.Header import Header


@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Tables Page")
class TablesPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.header = Header(driver)


    @allure.step("Assert only tables are displayed within products in 'Tables' page")
    def assert_only_tables_displayed(self):
        not_tables = [t for t in super().find_elements(Locators.ALL_PRODUCTS) if 'table' not in t.text.lower()]
        assert not not_tables, f'Only tables were expected, but the following products found: ' \
                               f'{[p.text for p in not_tables]}'


class Locators:
    ALL_PRODUCTS = (By.XPATH, "//div[contains(@class, 'product-list default')]")
