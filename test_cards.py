import time
from main_page_load import MainPage
def test_main_page_load(browser):
    main_page = MainPage(browser, "MainPage")
    main_page.open_site()
    time.sleep(3)
    assert main_page.get_current_url() == "https://xn----9sbgbhinbaa5ccc6ai.xn--p1ai/"


