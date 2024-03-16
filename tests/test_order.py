import pytest
import allure
from data import Url
from locators.order_page_locators import OrderPageLocators


class TestOrderPage:

    @pytest.mark.parametrize("name, surname, address, station, phone, date, duration, is_scroll",
                             [('Света', 'Андреева', 'Авторская 17', 'Автозаводская', '59648754125', '10.03.2024', 'сутки', False),
                              ('Антон', 'Евгеньев', 'Надзорная 33', 'Нагорная', '98741236875', '15.04.2024', 'четверо суток', True)])
    @allure.title('Проверка Позитивного сценария заказа с коректными данными')
    def test_scooter_order(self, main_page, order_page, name, surname, address, station, phone, date, duration, is_scroll):
        main_page.get_url(Url.MAIN_PAGE_URL)
        main_page.click_on_order_button(is_scroll)

        order_page.fill_name(name)
        order_page.fill_surname(surname)
        order_page.fill_address(address)
        order_page.fill_station(station)
        order_page.fill_phone(phone)

        order_page.go_to_second_order_page()
        order_page.fill_duration(duration)
        order_page.fill_date(date)

        order_page.final_order()
        order_page.final_confirmation()
        assert order_page.check_if_confirmed()











