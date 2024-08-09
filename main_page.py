from selenium.webdriver.common.by import By

from base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)