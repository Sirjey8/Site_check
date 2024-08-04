import re
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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
        asc_option = select.find_element(By.XPATH, "//option[contains(text(), 'По наименованию (А-Я)')]")
        asc_option.click()
    def click_sort_alphabet_desc(self):
        select = self.driver.find_element(By.XPATH, "//select[@class='sort']")
        select.click()
        time.sleep(1)
        desc_option = select.find_element(By.XPATH, "//option[contains(text(), 'По наименованию (Я-А)')]")
        desc_option.click()

    def check_items_in_ascending_order(self):
        assert "sort=name" in self.get_current_url()
        assert "order=asc" in self.get_current_url()
        titles_elements = self.driver.find_elements(By.XPATH, "//div[@class='title']//a[@class='dark-color']")
        titles = []
        for title_el in titles_elements:
            text = re.sub(r'[^а-я]', '', title_el.text, flags=re.IGNORECASE)
            titles.append(text)
        assert self.is_ascending(titles)
    def check_items_in_desc_order(self):
        assert "sort=name" in self.get_current_url()
        assert "order=desc" in self.get_current_url()
        titles_elements = self.driver.find_elements(By.XPATH, "//div[@class='title']//a[@class='dark-color']")
        titles = []
        for title_el in titles_elements:
            text = re.sub(r'[^а-я]', '', title_el.text, flags=re.IGNORECASE)
            titles.append(text)
        assert not self.is_ascending(titles)

    def is_ascending(self, titles):
        for i in range(len(titles) - 1):
            if titles[i] > titles[i + 1]:
                return False
        return True

    def test_open_first_card(self):
        titles_element = self.driver.find_element(By.XPATH, "//div[@class='title']//a[@class='dark-color']")
        y_position = titles_element.location['y']
        self.driver.execute_script(f"window.scrollTo(0, {y_position})")
        href = titles_element.get_attribute('href')
        titles_element.click()
        time.sleep(3)
        assert self.get_current_url() == href
    def test_up_butten_visibility(self):
        self.driver.get('https://берг-инжиниринг.рф/product/podshipniki/korpusnye-podshipniki/')
        time.sleep(3)
        up_butten = self.driver.find_element(By.CLASS_NAME, 'scroll-to-top')
        self.driver.execute_script(f"window.scrollTo(0, 500)")
        assert up_butten.is_displayed()

    def test_up_butten_functionality(self):
        self.test_up_butten_visibility()
        self.driver.find_element(By.CLASS_NAME, 'scroll-to-top').click()
        time.sleep(1)
        assert self.driver.find_element(By.CLASS_NAME, 'logo').is_displayed()

    def test_search_visibility(self):
        self.driver.get('https://берг-инжиниринг.рф/product/podshipniki/korpusnye-podshipniki/')
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, "inline-search-show").click()
        time.sleep(1)
        assert self.driver.find_element(By.ID, "title-search").is_displayed()
        assert self.driver.find_element(By.CLASS_NAME, "close-block").is_displayed()
        assert self.driver.find_element(By.CLASS_NAME, "btn-search").is_displayed()














