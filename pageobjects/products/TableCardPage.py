import logging

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pageobjects.CartPage import CartPage
from pageobjects.Header import Header
from pageobjects.products.AbstractCardPage import AbstractCardPage


class TableCardPage(AbstractCardPage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        super().wait_until_product_page_is_fully_loaded()
        self.header = Header(driver)
        self.product_title = super().get_product_title()
        self.product_price = super().get_product_price()

    @allure.step("Adding {self.product_title} to cart")
    def add_table_to_card(self):
        logging.info(f"Adding {self.product_title} to cart")
        super().add_product_to_cart()

    def open_cart_page(self) -> CartPage:
        super().open_cart_page()
        return CartPage(self.driver)

class Locators:
    pass