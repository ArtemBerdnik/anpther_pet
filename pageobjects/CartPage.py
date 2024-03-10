import allure
import logging

from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageobjects.BasePage import BasePage
from pageobjects.CheckoutPage import CheckoutPage
from pageobjects.Header import Header
from pageobjects.products.AbstractCardPage import AbstractCardPage


class CartPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        super().wait_for_element_displayed(Locators.PLACE_ORDER_BUTTON)
        self.header = Header(driver)
        self.total = self.find_element(Locators.PRODUCT_TOTAL).text

    @allure.step("Assert product price in cart")
    def assert_total_price(self, product: AbstractCardPage):
        logging.info("Asserting produce price in cart")
        assert product.product_price == self.total, \
            f'\nexpected price was: {product.product_price}\nactual price is {self.total}'
        return self

    @allure.step("Click 'Place order' button")
    def place_order(self) -> CheckoutPage:
        logging.info("Clicking 'Please order' button")
        self.find_element(Locators.PLACE_ORDER_BUTTON).click()
        return CheckoutPage(self.driver)


class Locators:
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//a[contains(@class, 'continue_shopping')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//input[@value='Place an order']")
    PRODUCT_TOTAL = (By.XPATH, "//table[@class='cart-products']//td[contains(@class, 'product_total')]")
