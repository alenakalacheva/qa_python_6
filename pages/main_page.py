import allure

from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Нажимаем на вопрос и получаем ответ')
    def click_on_question_get_answer(self, locator_q, locator_a, num):
        locator_q = self.make_locator(locator_q, num)
        locator_a = self.make_locator(locator_a, num)

        self.scroll_to_element(locator_q)
        self.wait_element_is_clickable(locator_q)
        self.click_on_element(locator_q)
        self.wait_element_is_visible(locator_a)
        return self.get_text_from_element(locator_a)

    @allure.step('Проверяет соответствие вопроса ожидаемому результату')
    def check_answer(self, result, expected_result):
        return result == expected_result

    def click_on_order_button(self, is_scroll, locator_h, locator_p):
        if is_scroll:
            self.scroll_to_element(locator_p)
            self.wait_element_is_clickable(locator_p)
            self.click_on_element(locator_p)
        else:
            self.click_on_element(locator_h)

    def click_on_logo(self, locator):
        self.wait_element_is_clickable(locator)
        self.click_on_element(locator)

    def go_to_zen_page(self):
        self.switch_to_new_window()
