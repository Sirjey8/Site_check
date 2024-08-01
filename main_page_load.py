from selenium.webdriver.common.by import By

from base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver, name):
        super().__init__(driver)
        self.card_xpath = (f'//span[contains(text(), "{name}")]'
                           f'//ancestor::div[contains(@class, '
                           f'"catalog-block__item")]')

    # Локатор - карточка тура
    def card(self):
        return self.driver.find_element(By.XPATH, self.card_xpath)


