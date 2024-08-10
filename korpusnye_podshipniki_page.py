import re
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_page import BasePage


# Тестирование страницы "Корпусные подшипники"
class KorpusnyePodshipnikiPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    # Наведение курсора на пункт "каталог" в верхнем меню
    def hover_catalog(self):
        catalog_menu_item = self.driver.find_element(By.XPATH, '//a[contains(text(), "Каталог")]')
        actions = ActionChains(self.driver)
        actions.move_to_element(catalog_menu_item).perform()
        time.sleep(3)

    # Клик по пункту меню "корпусные подшипники"
    def click_korpusnye_podshipniki(self):
        podshipniki_submenu = self.driver.find_element(By.XPATH, '//a[contains(text(), "Корпусные подшипники")]')
        WebDriverWait(self.driver, 10).until(EC.visibility_of(podshipniki_submenu))
        podshipniki_submenu.click()
        time.sleep(3)

    # Клик по кнопке сортировки в алфавитном порядке от А до Я
    def click_sort_alphabet_asc(self):
        select = self.driver.find_element(By.XPATH, "//select[@class='sort']")
        select.click()
        time.sleep(1)
        asc_option = select.find_element(By.XPATH, "//option[contains(text(), 'По наименованию (А-Я)')]")
        asc_option.click()

    # Клик по кнопке сортировки в алфавитном порядке от Я до А
    def click_sort_alphabet_desc(self):
        select = self.driver.find_element(By.XPATH, "//select[@class='sort']")
        select.click()
        time.sleep(1)
        desc_option = select.find_element(By.XPATH, "//option[contains(text(), 'По наименованию (Я-А)')]")
        desc_option.click()

    # Проверка, что товары вывелись в алфавитном порядке по возрастанию
    def check_items_in_ascending_order(self):
        assert "sort=name" in self.get_current_url()
        assert "order=asc" in self.get_current_url()
        titles_elements = self.driver.find_elements(By.XPATH, "//div[@class='title']//a[@class='dark-color']")
        titles = []
        for title_el in titles_elements:
            text = re.sub(r'[^а-я]', '', title_el.text, flags=re.IGNORECASE)
            titles.append(text)
        assert self.is_ascending(titles)

    # Проверка, что товары вывелись в алфавитном порядке по убыванию
    def check_items_in_desc_order(self):
        assert "sort=name" in self.get_current_url()
        assert "order=desc" in self.get_current_url()
        titles_elements = self.driver.find_elements(By.XPATH, "//div[@class='title']//a[@class='dark-color']")
        titles = []
        for title_el in titles_elements:
            text = re.sub(r'[^а-я]', '', title_el.text, flags=re.IGNORECASE)
            titles.append(text)
        assert (not self.is_ascending(titles))

    # Проверяет, что массив отсортирован по возрастанию
    def is_ascending(self, titles):
        for i in range(len(titles) - 1):
            if titles[i] > titles[i + 1]:
                return False
        return True

    # Проверка открытия первой карточки товара в "Корпусных подшипниках"
    def test_open_first_card(self):
        titles_element = self.driver.find_element(By.XPATH, "//div[@class='title']//a[@class='dark-color']")
        # Находим положение по вертикали
        y_position = titles_element.location['y'] - 50
        # Прокручиваем к ней
        self.driver.execute_script(f"window.scrollTo(0, {y_position})")
        # Получаем атрибут href
        href = titles_element.get_attribute('href')
        titles_element.click()
        time.sleep(3)
        # сравниваем текущий адрес с полученным из атрибута href
        assert self.get_current_url() == href

    # Проверка отображения кнопки "Наверх"
    def test_up_butten_visibility(self):
        self.driver.get('https://берг-инжиниринг.рф/product/podshipniki/korpusnye-podshipniki/')
        time.sleep(3)
        up_butten = self.driver.find_element(By.CLASS_NAME, 'scroll-to-top')
        # прокуричваем на 500 пикселей вниз
        self.driver.execute_script(f"window.scrollTo(0, 500)")
        # проверяем, что кнопка видна
        assert up_butten.is_displayed()

    # Проверка функциональности кнопки "Наверх"
    def test_up_butten_functionality(self):
        self.test_up_butten_visibility()
        self.driver.find_element(By.CLASS_NAME, 'scroll-to-top').click()
        time.sleep(1)
        # Проверяем что логотип виден
        assert self.driver.find_element(By.CLASS_NAME, 'logo').is_displayed()

    # проверка отображения строки поиска
    def test_search_visibility(self):
        self.driver.get('https://берг-инжиниринг.рф/product/podshipniki/korpusnye-podshipniki/')
        time.sleep(3)
        # Ищем "Лупу" и кликаем по ней
        self.driver.find_element(By.CLASS_NAME, "inline-search-show").click()
        time.sleep(1)
        # Проверяем, что строка поиска и её элементы видны
        assert self.driver.find_element(By.ID, "title-search").is_displayed()
        assert self.driver.find_element(By.CLASS_NAME, "close-block").is_displayed()
        assert self.driver.find_element(By.CLASS_NAME, "btn-search").is_displayed()

    # проверка закрытия строки поиска по клику на "крестик"
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

    # Проверка работы поиска
    def test_search_work(self):
        self.driver.get('https://берг-инжиниринг.рф/product/podshipniki/korpusnye-podshipniki/')
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, "inline-search-show").click()
        time.sleep(1)
        # Ищем поле ввода в поисковой строке и вводим туда строку berg20709
        self.driver.find_element(By.ID, "title-search-input").send_keys('berg20709')
        #  кликаем по кнопке "Найти"
        self.driver.find_element(By.CLASS_NAME, "btn-search").click()
        time.sleep(3)
        # Ищем по классу text первый элемент, берем из него текст
        assert 'berg20709' in self.driver.find_element(By.CLASS_NAME, "text").text
        # Ищем по css селектору класс search_page и все ссылки (элемент a) внутри него
        elements = self.driver.find_elements(By.CSS_SELECTOR, '.search-page > a')
        # Таких ссылок должно быть 1
        assert len(elements) == 1
        # Берем эту ссылку, её атрибут href и проверяем, что данная строка входит в href
        assert '/product/podshipniki/korpusnye-podshipniki/35887' in elements[0].get_attribute('href')

    # Тестирование фильтра в боковой панели
    def test_sidebar_filter(self):
        self.driver.get('https://берг-инжиниринг.рф/product/podshipniki/korpusnye-podshipniki/')
        time.sleep(3)
        smartfilter = self.driver.find_element(By.CLASS_NAME, "smartfilter")
        y_position = smartfilter.location['y'] - 50
        self.driver.execute_script(f"window.scrollTo(0, {y_position})")
        time.sleep(3)
        # для кажлдого элемента, с классом bx_filter_parameters_box_title внутри элемента с классом
        # smartfilter
        for element in smartfilter.find_elements(By.CLASS_NAME, 'bx_filter_parameters_box'):
            if 'active' not in element.get_attribute('class'):
                # кликаем по элементу
                element.click()
            # и ждём 1 секунду пока откроется
            time.sleep(1)
        time.sleep(1)
        # Выбираем бренд FAG
        checkbox = smartfilter.find_element(By.CSS_SELECTOR, 'label[for="arrFilter_379_2324464151"]')
        checkbox.click()
        # Заполняем диаметр наружный минимальный
        smartfilter.find_element(By.ID, 'arrFilter_450_MIN').send_keys('105')
        # Заполняем диаметр наружный максимальный
        smartfilter.find_element(By.ID, 'arrFilter_450_MAX').send_keys('110')
        # Заполняем вес минимальный
        smartfilter.find_element(By.ID, 'arrFilter_454_MIN').send_keys('1')
        # Заполняем вес максимальный
        smartfilter.find_element(By.ID, 'arrFilter_454_MAX').send_keys('2')
        time.sleep(3)
        # кликаем по кнопке "показать"
        smartfilter.find_element(By.ID, 'set_filter').click()
        time.sleep(3)
        # После перезагрузки страницы, проверяем, что найдено 3 товара
        elements = self.driver.find_elements(By.CSS_SELECTOR, '.ajax_load img')
        assert len(elements) == 3

    # Проверка сброса фильтра
    def test_sidebar_filter_reset(self):
        self.test_sidebar_filter()
        del_filter = self.driver.find_element(By.ID, 'del_filter')
        # 100 - в данном случае экспериментально определенная константа
        y_position = del_filter.location['y'] - 100
        self.driver.execute_script(f"window.scrollTo(0, {y_position})")
        time.sleep(3)
        del_filter.click()
        time.sleep(3)
        assert '/product/podshipniki/korpusnye-podshipniki/filter/clear/apply/' in self.get_current_url()

    def load_more_items(self):
        for i in range(14):
            more_text_ajax = self.driver.find_elements(By.CLASS_NAME, 'ajax_load_btn')[-1]
            y_position = more_text_ajax.location['y'] - 50
            self.driver.execute_script(f"window.scrollTo(0, {y_position})")
            more_text_ajax.click()
            time.sleep(3)
