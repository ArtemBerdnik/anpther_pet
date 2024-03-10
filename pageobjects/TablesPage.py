import logging
import random

import allure
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageobjects.BasePage import BasePage
from pageobjects.Header import Header
from pageobjects.products.TableCardPage import TableCardPage


@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Tables Page")
class TablesPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.header = Header(driver)

    @allure.step("Assert only tables are displayed within products in 'Tables' page")
    def assert_only_tables_displayed(self):
        logging.info("Getting all the products on 'Tables' page")
        not_tables = [t for t in super().find_elements(Locators.ALL_PRODUCTS) if 'table' not in t.text.lower()]
        assert not not_tables, f'Only tables were expected, but the following products found: ' \
                               f'{[p.text for p in not_tables]}'

    @allure.step("Open card page for table")
    def open_random_card_page(self) -> TableCardPage:
        all_products = [t for t in super().find_elements(Locators.ALL_PRODUCTS)]
        logging.info("Open random product from ALL tables on the page")
        random_element = random.choice(all_products)
        random_element.click()
        self.wait_for_url_to_contain("products")
        return TableCardPage(self.driver)


class Locators:
    ALL_PRODUCTS = (By.XPATH, "//div[contains(@class, 'product-list default')]")
