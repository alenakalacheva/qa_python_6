import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Нажимаем на вопрос и получаем ответ')
    def click_on_question_get_answer(self, num):
        locator_q = self.make_locator(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a = self.make_locator(MainPageLocators.ANSWER_LOCATOR, num)

        self.scroll_to_element(locator_q)
        self.wait_element_is_clickable(locator_q)
        self.click_on_element(locator_q)
        self.wait_element_is_visible(locator_a)
        return self.get_text_from_element(locator_a)

    @allure.step('Проверяет соответствие вопроса ожидаемому результату')
    def check_answer(self, result, expected_result):
        return result == expected_result

    @allure.step('Нажатие кнопки Заказать')
    def click_on_order_button(self, is_scroll):
        locator_h = MainPageLocators.ORDER_BUTTON_HEADER
        locator_p = MainPageLocators.ORDER_BUTTON
        if is_scroll:
            self.scroll_to_element(locator_p)
            self.wait_element_is_clickable(locator_p)
            self.click_on_element(locator_p)
        else:
            self.click_on_element(locator_h)

    @allure.step('Нажатие на логотип')
    def click_on_logo_yandex(self):
        locator = MainPageLocators.YANDEX_LOGO
        self.wait_element_is_clickable(locator)
        self.click_on_element(locator)

    @allure.step('Нажатие на логотип')
    def click_on_logo_scooter(self):
        locator = MainPageLocators.SCOOTER_LOGO
        self.wait_element_is_clickable(locator)
        self.click_on_element(locator)

    @allure.step('Переход на страницу Дзена')
    def go_to_zen_page(self):
        self.switch_to_new_window()

    @allure.step('Проверяем что мы на главной странице')
    def check_if_on_main_page(self):
        locator = MainPageLocators.ANSWERS_TITLE
        return self.wait_element_is_visible(locator)



