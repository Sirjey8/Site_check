import re
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_page import BasePage


class PodshipnikiSkolgeniyaPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    def open_site(self):
        self.driver.get('https://берг-инжиниринг.рф/product/podshipniki/podshipniki-skolzheniya/')
        time.sleep(3)
    def test_images_page_podshipniki_skolgeniya(self):
        img_responsive = self.driver.find_elements(By.XPATH, "//img[@class='img-responsive']")
        for img in img_responsive:
            assert "noimage_product.png" in img.get_attribute('src')

    def test_hover_cards(self):
        first_card = self.driver.find_element(By.CLASS_NAME, 'item')
        y = first_card.location['y']
        self.driver.execute_script(f'window.scrollTo(0, {y})')
        actions = ActionChains(self.driver)
        actions.move_to_element(first_card).perform()
        time.sleep(3)
        assert first_card.find_element(By.CLASS_NAME, 'btn').is_displayed()

    def test_tiled_page_display(self):
        ajax_load = self.driver.find_element(By.CLASS_NAME, 'ajax_load')
        assert 'table' in ajax_load.get_attribute('class')
        view_list = self.driver.find_element(By.CLASS_NAME, 'view-list')
        y = view_list.location['y']
        self.driver.execute_script(f'window.scrollTo(0, {y})')
        view_list.click()
        time.sleep(3)
        ajax_load = self.driver.find_element(By.CLASS_NAME, 'ajax_load')
        assert 'list' in ajax_load.get_attribute('class')

        view_price = self.driver.find_element(By.CLASS_NAME, 'view-price')
        y = view_price.location['y']
        self.driver.execute_script(f'window.scrollTo(0, {y})')
        view_price.click()
        time.sleep(3)
        ajax_load = self.driver.find_element(By.CLASS_NAME, 'ajax_load')
        assert 'price' in ajax_load.get_attribute('class')




