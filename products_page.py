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
        sidebar = self.driver.find_element(By.XPATH, '//aside[contains(@class, "sidebar")]')
        links = sidebar.find_elements(By.XPATH, '//a')
        for link in links:
            print(link.text)
