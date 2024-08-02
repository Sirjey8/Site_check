import logging
import time

from selenium.webdriver.common.by import By

from base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.xpath = (f'//div[contains(@class, "table-menu")]')

    def go_to_products(self):
        menu = self.driver.find_element(By.XPATH, self.xpath)
        menu.find_element(By.XPATH, '//a[contains(text(), "Каталог")]').click()

    def go_to_products_ina_fag(self):
        menu = self.driver.find_element(By.XPATH, self.xpath)
        menu.find_element(By.XPATH, '//a[contains(text(), "Каталог")]').click()
        time.sleep(3)
        xpath = '//aside[@class="sidebar"]//a[@href="/catalog-ina-fag/"]'
        elements = self.driver.find_elements(By.XPATH, xpath)
        elements[0].click()
        time.sleep(3)
        assert self.get_current_url() == "https://xn----9sbgbhinbaa5ccc6ai.xn--p1ai/catalog-ina-fag/"

    def check_iframe(self):
        time.sleep(3)
        iframe = self.driver.find_element(By.CLASS_NAME, "fram")
        self.driver.switch_to.frame(iframe)
        assert self.get_current_url() != 'https://medias.schaeffler.de/ru#1'
        self.driver.switch_to.default_content()
