import logging

import allure
from selenium.webdriver.common.by import By


class Header:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Open 'Gatling HW' page")
    def open_gatling_hw_page(self):
        self.driver.find_element(*Locators.GATLING_HW_TASK_LINK).click()

    @allure.step("Open 'Chairs' page")
    def open_chairs_page(self):
        self.driver.find_element(*Locators.CHAIRS_LINK).click()

    @allure.step("Open 'Talbes' page")
    def open_tables_page(self):
        logging.info("opening 'Tables' page")
        self.driver.find_element(*Locators.TABLES_LINK).click()

    @allure.step("Open 'Cart' page")
    def open_cart_page(self):
        logging.info("opening 'Cart' page")
        self.driver.find_element(*Locators.CART_LINK).click()


class Locators:
    COMMON_LOCATOR = "//div[@class='menu']//li//a[contains(text(),'<TITLE>')]"
    GATLING_HW_TASK_LINK = (By.XPATH, COMMON_LOCATOR.replace("<TITLE>", "Gatling"))
    TABLES_LINK = (By.XPATH, COMMON_LOCATOR.replace("<TITLE>", "Tables"))
    CHAIRS_LINK = (By.XPATH, COMMON_LOCATOR.replace("<TITLE>", "Chairs"))
    CART_LINK = (By.XPATH, COMMON_LOCATOR.replace("<TITLE>", "Cart"))
