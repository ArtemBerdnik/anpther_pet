import allure
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageobjects.BasePage import BasePage
from pageobjects.Header import Header


class ThankYouPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        super().wait_for_element_displayed(Locators.THANK_YOU_SIGN)
        self.header = Header(driver)

    @allure.step("Assert 'Thank you' sign is displayed")
    def assert_thank_you_sign_is_displayed(self):
        self.assert_element_is_present(*Locators.THANK_YOU_SIGN)


class Locators:
    THANK_YOU_SIGN = (By.XPATH, "//h1[@class='entry-title']")