import allure
from data import Url
from locators.additional_locators import AdditionalLocators
from locators.main_page_locators import MainPageLocators


class TestLogoRedirections:

    @allure.title('Проверка перехода на страницу Дзен при клике на логотип Яндекса')
    def test_yandex_logo_click(self, main_page, zen_page):
        main_page.get_url(Url.MAIN_PAGE_URL)

        main_page.click_on_logo_yandex()
        main_page.go_to_zen_page()

        zen_page.find_logo_zen()
        zen_page.check_zen_opened()

    @allure.title('Проверка перехода на страницу главную страницу при клике на логотип Самокат')
    def test_scooter_logo_click(self, main_page):
        main_page.get_url(Url.ORDER_PAGE_URL)
        main_page.click_on_logo_scooter()
        assert main_page.check_if_on_main_page()



