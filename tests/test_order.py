import pytest
import allure
from data import Url
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators



class TestOrderPage:

    @pytest.mark.parametrize("name, surname, address, station, phone, date, duration, is_scroll",
                             [('Света', 'Андреева', 'Авторская 17', 'Автозаводская', '59648754125', '10.03.2024', 'сутки', False),
                              ('Антон', 'Евгеньев', 'Надзорная 33', 'Нагорная', '98741236875', '15.04.2024', 'четверо суток', True)])
    def test_scooter_order(self, main_page, order_page, name, surname, address, station, phone, date, duration, is_scroll):
        main_page.get_url(Url.MAIN_PAGE_URL)
        main_page.click_on_order_button(is_scroll, MainPageLocators.ORDER_BUTTON_HEADER, MainPageLocators.ORDER_BUTTON)

        order_page.fill_name(name, OrderPageLocators.NAME_LOCATOR)
        order_page.fill_surname(surname, OrderPageLocators.SURNAME_LOCATOR)
        order_page.fill_address(address, OrderPageLocators.ADDRESS_LOCATOR)
        order_page.fill_station(station, OrderPageLocators.METRO_INPUT_LOCATOR, OrderPageLocators.METRO_STATION_LOCATOR)
        order_page.fill_phone(phone, OrderPageLocators.PHONE_LOCATOR)

        order_page.go_to_second_order_page(OrderPageLocators.FURTHER_BUTTON)
        order_page.fill_duration(duration, OrderPageLocators.RENTAL_DURATION_INPUT,
                                 OrderPageLocators.RENTAL_DURATION_VALUE)
        order_page.fill_date(date, OrderPageLocators.DATE_LOCATOR)

        order_page.final_order(OrderPageLocators.ORDER_BUTTON_IN_ORDER)
        order_page.final_confirmation(OrderPageLocators.CONFIRM_BUTTON)
        assert order_page.find_element(OrderPageLocators.CONFIRMATION_LOCATOR)











