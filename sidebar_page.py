from selenium.webdriver.common.by import By

from base_page import BasePage


class SidebarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.aside = '//aside[@class="sidebar"]'
        self.description = '//div[@class"sidearea"]]//i'

    def get_aside(self):
        return self.driver.find_element(By.XPATH, self.aside)

    def get_description(self):
        return self.driver.find_element(By.XPATH, self.description)