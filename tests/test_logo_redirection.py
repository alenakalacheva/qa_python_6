import allure
from data import Url
from locators.additional_locators import AdditionalLocators
from locators.main_page_locators import MainPageLocators


class TestLogoRedirections:

    def test_yandex_logo_click(self, main_page, zen_page):
        main_page.get_url(Url.MAIN_PAGE_URL)

        main_page.click_on_logo(MainPageLocators.YANDEX_LOGO)
        main_page.go_to_zen_page()

        zen_page.find_logo(AdditionalLocators.ZEN_LOGO)
        zen_page.check_zen_opened()

    def test_scooter_logo_click(self, main_page):
        main_page.get_url(Url.ORDER_PAGE_URL)
        main_page.click_on_logo(MainPageLocators.SCOOTER_LOGO)
        main_page.wait_element_is_visible(MainPageLocators.ANSWERS_TITLE)
        assert main_page.find_element(MainPageLocators.ANSWERS_TITLE)



