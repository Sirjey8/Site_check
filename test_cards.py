import time

from card_page import CardPage
from sidebar_page import SidebarPage


def test_cards(browser):
    cards = CardPage(browser)
    cards.open_site()
    time.sleep(10)
    cards.close_modal_cookies_message()
    time.sleep(3)

    cards.card1.btn_details_click("Восхождение по хребту Малого Ямантау")
    assert cards.get_current_url() == "https://bashadventure.ru/catalog/ural/na-1-den/voskhozhdenie-na-malyy-yamantau/"
    time.sleep(3)

    cards.go_to_back()

    cards.card1.btn_details_click()
    assert cards.get_current_url() == "https://bashadventure.ru/catalog/ural/na-1-den/voskhozhdenie-na-malyy-yamantau/"
    time.sleep(5)

def test_sidebar(browser):
    ASIDE_TEXT = "Экскурсии, пешие походы, сплавы, туры выходного дня, корпоративный отдых"

    sidebar = SidebarPage(browser)
    sidebar.open_site()
    #time.sleep(10)
    #sidebar.close_modal_cookies_massage()
    time.sleep(2)

    assert sidebar.get_description() == ASIDE_TEXT