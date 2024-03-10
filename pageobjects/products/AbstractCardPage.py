import logging

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pageobjects.AbstractPage import AbstractPage
from pageobjects.Header import Header


class AbstractCardPage(AbstractPage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.header = Header(driver)

    def add_product_to_cart(self):
        self.driver.find_element(*Locators.ADD_TO_CARD_BUTTON).click()
        self.wait_for_dom_update()
        self.wait_for_element_displayed(Locators.PRODUCT_ADDED_MESSAGE, timeout=2)
        return self

    def get_product_title(self) -> str:
        logging.info("Getting product title")
        return self.find_element(Locators.PRODUCT_TITLE).text

    def get_product_price(self) -> str:
        logging.info("Getting product price")
        return self.find_element(Locators.PRODUCT_PRICE).text.replace('$', '')

    def wait_until_product_page_is_fully_loaded(self):
        self.wait_for_element_displayed(Locators.BREADCRUMBS)
        self.wait_for_element_displayed(Locators.PRODUCT_TITLE)

    @allure.step("Assert message 'Added! See your cart.' is displayed")
    def assert_product_added_message_displayed(self):
        logging.info("Assert message 'Added! See your cart.' is displayed")
        self.assert_element_is_present(*Locators.PRODUCT_ADDED_MESSAGE), \
            "Expected to see message 'Added! See your cart.' but it didn't displayed"
        return self


class Locators:
    BREADCRUMBS = (By.XPATH, "//div[@id='crumbs']")
    PRODUCT_TITLE = (By.XPATH, "//h1[@class='entry-title']")
    PRODUCT_PRICE = (By.XPATH, "//td[contains(@class, 'price-value')]")
    ADD_TO_CARD_BUTTON = (By.XPATH, "//button[@type='submit']")
    PRODUCT_ADDED_MESSAGE = (By.XPATH, "//span[@class='al-box success cart-added-info ']")
