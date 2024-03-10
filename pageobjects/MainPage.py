import logging

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageobjects.BasePage import BasePage
from pageobjects.Header import Header
from pageobjects.TablesPage import TablesPage
from utils.PropertiesHanlder import get_properties


@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Main Page")
class MainPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.header = Header(driver)

    def open_page(self, url=f"{get_properties('url')}"):
        logging.info("opening 'Main' page")
        super().open_page(url)
        return self

    def open_tables_page(self) -> TablesPage:
        self.header.open_tables_page()
        return TablesPage(self.driver)

    # ================Actions=================#

    @allure.step("Type {search_phrase} to input field in 'Main' page")
    def type_to_search_input(self, search_phrase: str):
        logging.info(f"Typing {search_phrase} into 'Search' input")
        super().find_element(Locators.SEARCH_INPUT).send_keys(search_phrase)
        logging.info("Clicking 'Submit' button")
        submit_button = super().find_element(Locators.SEARCH_SUBMIT_BUTTON)
        ActionChains(self.driver).move_to_element(submit_button).click().perform()
        self.wait_for_dom_update()

    # ================Assertions=================#

    @allure.step("Assert main categories section is displayed")
    def assert_main_categories_displayed(self):
        logging.info(f"Assert main categories section is displayed")
        self.assert_element_is_present(*Locators.MAIN_CATEGORIES)
        return self

    @allure.step("Assert search result for {search_phrase}")
    def assert_search_result(self, search_phrase: str):
        all_products_in_search = super().find_elements(Locators.PRODUCT_IN_SEARCH)
        assert all(search_phrase in t.text.lower() for t in all_products_in_search), \
            f'Requested product "{search_phrase}" was not found in search result'

    @allure.step("Assert search result is empty")
    def assert_search_result_is_empty(self):
        expected_msg = "Sorry, but nothing matched your search terms. Please try again with some different keywords."
        products_not_found = super().find_element(Locators.NO_PRODUCT_FOUND_MESSAGE)
        assert products_not_found.text == expected_msg, f"Expected message was: {expected_msg},\n" \
                                                        f"actual is: {products_not_found}"


class Locators:
    MAIN_CATEGORIES = (By.XPATH, "//div[@class='product-subcategories responsive default  per-row-5']")
    SEARCH_INPUT = (By.XPATH, "//input[@class='product-search-box']")
    SEARCH_SUBMIT_BUTTON = (By.XPATH, "//input[@class='product-search-submit']")
    PRODUCT_IN_SEARCH = (By.XPATH, "//div[contains(@class, 'al_archive') and contains(@class, 'product')]")
    NO_PRODUCT_FOUND_MESSAGE = (By.XPATH, "//div[contains(@class, 'active-product-listing') and contains(@class, "
                                          "'product')]//p")
