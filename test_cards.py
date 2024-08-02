import time
from main_page import MainPage
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
