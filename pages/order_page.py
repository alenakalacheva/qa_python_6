import allure
from pages.base_page import BasePage


class OrderPage(BasePage):
    def fill_name(self, name, locator):
        self.click_on_element(locator)
        self.set_text_to_element(locator, name)

    def fill_surname(self, surname, locator):
        self.click_on_element(locator)
        self.set_text_to_element(locator, surname)

    def fill_address(self, address, locator):
        self.click_on_element(locator)
        self.set_text_to_element(locator, address)

    def fill_phone(self, phone, locator):
        self.click_on_element(locator)
        self.set_text_to_element(locator, phone)

    def fill_station(self, station, locator, locator_s):
        self.click_on_element(locator)
        self.set_text_to_element(locator, station)
        method, locator_s = locator_s
        locator_s = (method, locator_s.format(station))
        self.click_on_element(locator_s)

    def go_to_second_order_page(self, locator):
        self.click_on_element(locator)

    def fill_date(self, date, locator):
        self.click_on_element(locator)
        self.set_text_to_element(locator, date)

    def fill_duration(self, duration, locator, locator_v):
        self.click_on_element(locator)
        method, locator_v = locator_v
        locator_v = (method, locator_v.format(duration))
        self.click_on_element(locator_v)

    def final_order(self, locator):
        self.click_on_element(locator)

    def final_confirmation(self, locator):
        self.wait_element_is_clickable(locator)
        self.click_on_element(locator)

