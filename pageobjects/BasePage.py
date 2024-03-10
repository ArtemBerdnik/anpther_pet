from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utils.PropertiesHanlder import get_properties


class BasePage:

    def __init__(self, driver: WebDriver, url=f"{get_properties('url')}"):
        self.driver = driver
        self.url = url

    def find_element(self, locator: tuple, timeout=10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def find_elements(self, locator: tuple, timeout=10) -> List[WebElement]:
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def select_value_from_dropdown_by_text(self, dropdown_locator, text_to_select, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(dropdown_locator)
        )
        dropdown = self.driver.find_element(*dropdown_locator)
        select = Select(dropdown)
        select.select_by_visible_text(text_to_select)

    def assert_element_is_present(self, how_to_locate: By, locator: str):
        if self.find_element((how_to_locate, locator)):
            assert True
        else:
            assert False, f"There is no element on the page located by {how_to_locate}:{locator}"

    def open_page(self, url: str):
        return self.driver.get(url)


    def wait_for_element_displayed(self, locator: tuple, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_url_to_contain(self, url: str, timeout=3):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url))

    def wait_for_dom_update(self):
        old_dom = self.driver.page_source

        def dom_has_updated(driver):
            return old_dom != driver.page_source

        WebDriverWait(self.driver, 10).until(dom_has_updated)
