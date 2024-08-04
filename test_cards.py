import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from korpusnye_podshipniki_card import KorpusnyePodshipnikiCard
from korpusnye_podshipniki_page import KorpusnyePodshipnikiPage
from main_page import MainPage
from podshipniki_page import PodshipnikiPage
from podshipniki_skolgeniya_page import PodshipnikiSkolgeniyaPage
from products_page import ProductsPage


def test_main_page_load(browser):
    main_page = MainPage(browser, "MainPage")
    main_page.open_site()
    time.sleep(3)
    assert main_page.get_current_url() == "https://xn----9sbgbhinbaa5ccc6ai.xn--p1ai/"


def test_products_page_load(browser):
    page = ProductsPage(browser)
    page.open_site()
    time.sleep(1)
    page.go_to_products()
    time.sleep(3)
    assert page.get_current_url() == "https://xn----9sbgbhinbaa5ccc6ai.xn--p1ai/product/"

def test_products_page_ina_fag_load(browser):
    page = ProductsPage(browser)
    page.open_site()
    time.sleep(1)
    page.go_to_products_ina_fag()
    page.check_iframe()

def test_podshiphiki_paga(browser):
    page = PodshipnikiPage(browser)
    page.open_site()
    time.sleep(3)
    page.hover_catalog()
    page.click_podshipniki()
    assert page.get_current_url() == 'https://xn----9sbgbhinbaa5ccc6ai.xn--p1ai/product/podshipniki/'

def test_korpusnye_podshiphiki_paga(browser):
    page = KorpusnyePodshipnikiPage(browser)
    page.open_site()
    time.sleep(3)
    page.hover_catalog()
    page.click_korpusnye_podshipniki()
    assert page.get_current_url() == 'https://xn----9sbgbhinbaa5ccc6ai.xn--p1ai/product/podshipniki/korpusnye-podshipniki/'

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
    # todo: не могу проверить - не понятно как загрузить все страницы
    page.check_items_in_desc_order()

def test_open_item_card(browser):
    page = KorpusnyePodshipnikiPage(browser)
    page.open_site()
    time.sleep(3)
    page.hover_catalog()
    page.click_korpusnye_podshipniki()
    assert page.get_current_url() == 'https://xn----9sbgbhinbaa5ccc6ai.xn--p1ai/product/podshipniki/korpusnye-podshipniki/'
    page.test_open_first_card()

def test_back_url(browser):
    page = KorpusnyePodshipnikiCard(browser)
    page.open_site()
    time.sleep(3)
    page.hover_catalog()
    page.click_korpusnye_podshipniki()
    page.test_open_first_card()
    page.click_back_url()

def test_images_page_podshipniki_skolgeniya(browser):
    page = PodshipnikiSkolgeniyaPage(browser)
    page.open_site()
    page.test_images_page_podshipniki_skolgeniya()
    page.test_hover_cards()

def test_tiled_page_display(browser):
    page = PodshipnikiSkolgeniyaPage(browser)
    page.open_site()
    page.test_tiled_page_display()

def test_up_butten_visibility(browser):
    page = KorpusnyePodshipnikiPage(browser)
    page.test_up_butten_visibility()

def test_up_butten_functionality(browser):
    page = KorpusnyePodshipnikiPage(browser)
    page.test_up_butten_functionality()

def test_search_visibility(browser):
    page = KorpusnyePodshipnikiPage(browser)
    page.test_search_visibility()

def test_search_closure(browser):
    page = KorpusnyePodshipnikiPage(browser)
    page.test_search_closure()

def test_search_work(browser):
    page = KorpusnyePodshipnikiPage(browser)
    page.test_search_work()

def test_sidebar_filter(browser):
    page = KorpusnyePodshipnikiPage(browser)
    page.test_sidebar_filter()

