import time
import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_page import BasePage

class PodshipnikiPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def hover_catalog(self):
        catalog_menu_item = self.driver.find_element(By.XPATH, '//a[contains(text(), "Каталог")]')
        actions = ActionChains(self.driver)
        actions.move_to_element(catalog_menu_item).perform()
        time.sleep(3)

    def click_podshipniki(self):
        podshipniki_submenu = self.driver.find_element(By.XPATH, '//a[contains(text(), "Подшипники")]')
        WebDriverWait(self.driver, 10).until(EC.visibility_of(podshipniki_submenu))
        podshipniki_submenu.click()
        time.sleep(3)


