import re
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_page import BasePage
from korpusnye_podshipniki_page import KorpusnyePodshipnikiPage


class KorpusnyePodshipnikiCard(KorpusnyePodshipnikiPage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    def open_first_card(self):
        titles_element = self.driver.find_element(By.XPATH, "//div[@class='title']//a[@class='dark-color']")
        y_position = titles_element.location['y']
        self.driver.execute_script(f"window.scrollTo(0, {y_position})")
        titles_element.click()
        time.sleep(3)

    def click_back_url(self):
        back_url = self.driver.find_element(By.CLASS_NAME, 'back-url')
        y = back_url.location['y']
        self.driver.execute_script(f'window.scrollTo(0, {y})')
        back_url.click()
        time.sleep(3)
        assert self.get_current_url() == 'https://xn----9sbgbhinbaa5ccc6ai.xn--p1ai/product/podshipniki/korpusnye-podshipniki/'




