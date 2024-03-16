import allure
from locators.additional_locators import AdditionalLocators
from pages.base_page import BasePage


class ZenPage(BasePage):
    @allure.step('Поиск логотипа Дзена')
    def find_logo_zen(self):
        locator = AdditionalLocators.ZEN_LOGO
        self.wait_element_is_visible(locator)
        self.find_element(locator)

    @allure.step('Проверка что открыта страница Дзена')
    def check_zen_opened(self):
        current_url = self.get_current_url()
        assert current_url == "https://dzen.ru/?yredirect=true"



