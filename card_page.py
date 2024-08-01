from selenium.webdriver.common.by import By

from base_page import BasePage
from card import Card


class CardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.body = '//div[contains(@class, "section-content-wrapper")]'
        self.card1 = Card(driver, 'Восхождение по хребту Малого Ямантау')
        self.card2 = Card(driver, 'Абзаково и Синие скалы')

    def body(self):
        return self.driver.find_element(By.XPATH, self.body)