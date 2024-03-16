import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполнение поля Имя')
    def fill_name(self, name):
        locator = OrderPageLocators.NAME_LOCATOR
        self.click_on_element(locator)
        self.set_text_to_element(locator, name)

    @allure.step('Заполнение поля Фамилия')
    def fill_surname(self, surname):
        locator = OrderPageLocators.SURNAME_LOCATOR
        self.click_on_element(locator)
        self.set_text_to_element(locator, surname)

    @allure.step('Заполнение поля Адрес')
    def fill_address(self, address):
        locator = OrderPageLocators.ADDRESS_LOCATOR
        self.click_on_element(locator)
        self.set_text_to_element(locator, address)

    @allure.step('Заполнение поля Телефон')
    def fill_phone(self, phone):
        locator = OrderPageLocators.PHONE_LOCATOR
        self.click_on_element(locator)
        self.set_text_to_element(locator, phone)

    @allure.step('Заполнение поля Станция метро')
    def fill_station(self, station):
        locator = OrderPageLocators.METRO_INPUT_LOCATOR
        locator_s = OrderPageLocators.METRO_STATION_LOCATOR
        self.click_on_element(locator)
        self.set_text_to_element(locator, station)
        method, locator_s = locator_s
        locator_s = (method, locator_s.format(station))
        self.click_on_element(locator_s)

    @allure.step('Переход на вторую страницу заказа')
    def go_to_second_order_page(self):

        self.click_on_element(OrderPageLocators.FURTHER_BUTTON)

    @allure.step('Заполнение поля Дата')
    def fill_date(self, date):
        locator = OrderPageLocators.DATE_LOCATOR
        self.click_on_element(locator)
        self.set_text_to_element(locator, date)

    @allure.step('Заполнение поля Срок аренды')
    def fill_duration(self, duration):
        locator = OrderPageLocators.RENTAL_DURATION_INPUT
        locator_v = OrderPageLocators.RENTAL_DURATION_VALUE
        self.click_on_element(locator)
        method, locator_v = locator_v
        locator_v = (method, locator_v.format(duration))
        self.click_on_element(locator_v)

    @allure.step('Нажатие кнопки Заказать в форме заказа')
    def final_order(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_IN_ORDER)

    @allure.step('Подтверждение заказа, нажатии кнопки Да')
    def final_confirmation(self):
        locator = OrderPageLocators.CONFIRM_BUTTON
        self.wait_element_is_clickable(locator)
        self.click_on_element(locator)

    @allure.step('Проверка подтверждения заказа')
    def check_if_confirmed(self):
        return self.find_element(OrderPageLocators.CONFIRMATION_LOCATOR)

