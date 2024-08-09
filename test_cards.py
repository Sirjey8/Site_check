import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from korpusnye_podshipniki_card import KorpusnyePodshipnikiCard
from korpusnye_podshipniki_page import KorpusnyePodshipnikiPage
from main_page import MainPage
from podshipniki_page import PodshipnikiPage
from podshipniki_skolgeniya_page import PodshipnikiSkolgeniyaPage
from products_page import ProductsPage

# тестирование загрузки главной страницы
def test_main_page_load(browser):
    main_page = MainPage(browser)
    main_page.open_site()
    time.sleep(3)
    assert main_page.get_current_url() == "https://xn----9sbgbhinbaa5ccc6ai.xn--p1ai/"

# тестироваие перехода через верхнее меню сраницы каталога 
def test_products_page_load(browser):
    page = ProductsPage(browser)
    page.open_site()
    time.sleep(1)
    page.go_to_products()
    time.sleep(3)
    assert page.get_current_url() == "https://xn----9sbgbhinbaa5ccc6ai.xn--p1ai/product/"

# тестироваие перехода на страницу «Подробный каталог INA/FAG»
def test_products_page_ina_fag_load(browser):
    page = ProductsPage(browser)
    page.open_site()
    time.sleep(1)
    page.go_to_products_ina_fag()
    page.check_iframe()

# тестироваие перехода на страницу «Главная > Каталог Berg > Подшипники"
def test_podshiphiki_paga(browser):
    page = PodshipnikiPage(browser)
    page.open_site()
    time.sleep(3)
    page.hover_catalog()
    page.click_podshipniki()
    assert page.get_current_url() == 'https://xn----9sbgbhinbaa5ccc6ai.xn--p1ai/product/podshipniki/'

# тестироваие перехода на страницу "Главная > Каталог Berg > Подшипники > Корпусные подшипники"
def test_korpusnye_podshiphiki_paga(browser):
    page = KorpusnyePodshipnikiPage(browser)
    page.open_site()
    time.sleep(3)
    page.hover_catalog()
    page.click_korpusnye_podshipniki()
    assert page.get_current_url() == 'https://xn----9sbgbhinbaa5ccc6ai.xn--p1ai/product/podshipniki/korpusnye-podshipniki/'

# тестироваие сортировки на странице "Корпусные подшипники"
def test_korpusnye_podshiphiki_paga_sort(browser):
    page = KorpusnyePodshipnikiPage(browser)
    page.open_site()
    time.sleep(3)
    page.hover_catalog()
    page.click_korpusnye_podshipniki()
    assert page.get_current_url() == 'https://xn----9sbgbhinbaa5ccc6ai.xn--p1ai/product/podshipniki/korpusnye-podshipniki/'
    page.click_sort_alphabet_asc()
    time.sleep(3)
    page.check_items_in_ascending_order()
    time.sleep(3)
    page.click_sort_alphabet_desc()
    time.sleep(3)
    page.check_items_in_desc_order()

# тестироваие карточки товара
def test_open_item_card(browser):
    # отрываю сайт 
    page = KorpusnyePodshipnikiPage(browser)
    page.open_site()
    time.sleep(3)
    # наводим на пункт меню "каталог"
    page.hover_catalog()
    # кликаем на подпункт "Корпусные подшипники"
    page.click_korpusnye_podshipniki()
    # сверка URL с ожидаемым значением
    assert page.get_current_url() == 'https://xn----9sbgbhinbaa5ccc6ai.xn--p1ai/product/podshipniki/korpusnye-podshipniki/'
    page.test_open_first_card()

# тестироваие кнопки возврата в карточке товара
def test_back_url(browser):
    page = KorpusnyePodshipnikiCard(browser)
    page.open_site()
    time.sleep(3)
    page.hover_catalog()
    page.click_korpusnye_podshipniki()
    page.test_open_first_card()
    page.click_back_url()

# тестироваие отображения миниатюр страницы "Подшипники скольжения"
def test_images_page_podshipniki_skolgeniya(browser):
    page = PodshipnikiSkolgeniyaPage(browser)
    page.open_site()
    page.test_images_page_podshipniki_skolgeniya()
    page.test_hover_cards()

# тестироваие плиточного, строчного и прайсового отображения 
def test_tiled_page_display(browser):
    page = PodshipnikiSkolgeniyaPage(browser)
    page.open_site()
    page.test_tiled_page_display()

# тестироваие отображения кнопки "Наверх"
def test_up_butten_visibility(browser):
    page = KorpusnyePodshipnikiPage(browser)
    page.test_up_butten_visibility()

# тестироваие функциональности кнопки "Наверх"
def test_up_butten_functionality(browser):
    page = KorpusnyePodshipnikiPage(browser)
    page.test_up_butten_functionality()

# тестироваие отображения поисковой строки
def test_search_visibility(browser):
    page = KorpusnyePodshipnikiPage(browser)
    page.test_search_visibility()

# тестироваие закрытия поисковой строки
def test_search_closure(browser):
    page = KorpusnyePodshipnikiPage(browser)
    page.test_search_closure()

# тестироваие работы поиска
def test_search_work(browser):
    page = KorpusnyePodshipnikiPage(browser)
    page.test_search_work()

# тестироваие фильтра по параметрам в боковом  меню
def test_sidebar_filter(browser):
    page = KorpusnyePodshipnikiPage(browser)
    page.test_sidebar_filter()

# тестироваие сброса фильтра по параметрам в боковом  меню
def test_sidebar_filter_reset(browser):
    page = KorpusnyePodshipnikiPage(browser)
    page.test_sidebar_filter_reset()
