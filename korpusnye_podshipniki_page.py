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

    def test_search_closure(self):
        self.driver.get('https://берг-инжиниринг.рф/product/podshipniki/korpusnye-podshipniki/')
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, "inline-search-show").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "close-block").click()
        time.sleep(1)
        assert not self.driver.find_element(By.ID, "title-search").is_displayed()
        assert not self.driver.find_element(By.CLASS_NAME, "close-block").is_displayed()
        assert not self.driver.find_element(By.CLASS_NAME, "btn-search").is_displayed()

    def test_search_work(self):
        self.driver.get('https://берг-инжиниринг.рф/product/podshipniki/korpusnye-podshipniki/')
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, "inline-search-show").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "title-search-input").send_keys('berg20709')
        self.driver.find_element(By.CLASS_NAME, "btn-search").click()
        time.sleep(3)
        assert 'berg20709' in self.driver.find_element(By.CLASS_NAME, "text").text
        elements = self.driver.find_elements(By.CSS_SELECTOR, '.search-page > a')
        assert len(elements) == 1
        assert '/product/podshipniki/korpusnye-podshipniki/35887' in elements[0].get_attribute('href')

    def test_sidebar_filter(self):
        self.driver.get('https://берг-инжиниринг.рф/product/podshipniki/korpusnye-podshipniki/')
        time.sleep(3)
        smartfilter = self.driver.find_element(By.CLASS_NAME, "smartfilter")
        y_position = smartfilter.location['y']-50
        self.driver.execute_script(f"window.scrollTo(0, {y_position})")
        time.sleep(3)
        for element in smartfilter.find_elements(By.CLASS_NAME, 'bx_filter_parameters_box_title'):
            element.click()
            time.sleep(1)
        time.sleep(1)
        checkbox = smartfilter.find_element(By.CSS_SELECTOR, 'label[for="arrFilter_379_2324464151"]')
        checkbox.click()
        smartfilter.find_element(By.ID, 'arrFilter_450_MIN').send_keys('105')
        smartfilter.find_element(By.ID, 'arrFilter_450_MAX').send_keys('110')
        smartfilter.find_element(By.ID, 'arrFilter_454_MIN').send_keys('1')
        smartfilter.find_element(By.ID, 'arrFilter_454_MAX').send_keys('2')
        time.sleep(3)
        smartfilter.find_element(By.ID, 'set_filter').click()
        time.sleep(3)
        elements = self.driver.find_elements(By.CLASS_NAME, 'img-responsive')
        assert len(elements) == 3

    def test_sidebar_filter_reset(self):
        self.test_sidebar_filter()
        del_filter = self.driver.find_element(By.ID, 'del_filter')
        y_position = del_filter.location['y'] -100
        self.driver.execute_script(f"window.scrollTo(0, {y_position})")
        time.sleep(3)
        del_filter.click()
        time.sleep(3)
        assert '/product/podshipniki/korpusnye-podshipniki/filter/clear/apply/' in self.get_current_url()











