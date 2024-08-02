import time
import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_page import BasePage

class KorpusnyePodshipnikiPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def hover_catalog(self):
        catalog_menu_item = self.driver.find_element(By.XPATH, '//a[contains(text(), "Каталог")]')
        actions = ActionChains(self.driver)
        actions.move_to_element(catalog_menu_item).perform()
        time.sleep(3)

    def click_korpusnye_podshipniki(self):
        podshipniki_submenu = self.driver.find_element(By.XPATH, '//a[contains(text(), "Корпусные подшипники")]')
        WebDriverWait(self.driver, 10).until(EC.visibility_of(podshipniki_submenu))
        podshipniki_submenu.click()
        time.sleep(3)

    def click_sort_alphabet_asc(self):
        select = self.driver.find_element(By.XPATH, "//select[@class='sort']")
        select.click()
        time.sleep(1)
        asc_option = select.find_element("//option[contains(text(), 'По наименованию (А-Я)')]")
        asc_option.click()

    def check_items_in_ascending_order(self):
        pass


