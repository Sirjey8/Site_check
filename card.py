from selenium.webdriver.common.by import By

from base_page import BasePage


class Card(BasePage):
    def __init__(self, driver, name):
        super().__init__(driver)
        self.card_xpath = (f'//span[contains(text(), "{name}")]'
                           f'//ancestor::div[contains(@class, '
                           f'"catalog-block__item")]')

    # Локатор - карточка тура
    def card(self):
        return self.driver.find_element(By.XPATH, self.card_xpath)

    # Локатор - название в карточке тура
    # def card_name(self):
    #     return self.card().find_element(By.XPATH, f'//span[contains(text(), "{name}")]')

    def card_name(self):
        return self.card().find_element(By.XPATH, '(//span[contains(text(), "Восхождение по хребту Малого Ямантау")]//ancestor::div[contains(@class, "catalog-block__item")]//span)[1]')

    # Локатор - кнопка "Подробнее"
    def btn_details(self):
        return self.card().find_element(By.XPATH, '//a[contains(@class, "btn btn-default")]')

    # Метод клика на название
    # def card_name_click(self):
    #     return self.card_name(name).click()

    # Метод клика на кнопку "Подробнее"
    def btn_details_click(self):
        self.btn_details().click()
