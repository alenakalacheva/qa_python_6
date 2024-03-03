import allure
from pages.base_page import BasePage


class ZenPage(BasePage):
    def find_logo(self, locator):
        self.wait_element_is_visible(locator)
        self.find_element(locator)

    def check_zen_opened(self):
        current_url = self.get_current_url()
        assert current_url == "https://dzen.ru/?yredirect=true"



