import pytest
import allure
from data import Answers, Url
from locators.main_page_locators import MainPageLocators
from locators.additional_locators import AdditionalLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver



class TestMainPage:

    @pytest.mark.parametrize("num, expected_result", [
        (0, Answers.ANSWER_0),
        (1, Answers.ANSWER_1),
        (2, Answers.ANSWER_2),
        (3, Answers.ANSWER_3),
        (4, Answers.ANSWER_4),
        (5, Answers.ANSWER_5),
        (6, Answers.ANSWER_6),
        (7, Answers.ANSWER_7),
    ]
                             )
    @allure.title('Проверка Соответствия текста ответа №{num}')
    @allure.description('На главной странице ищем вопрос и проверяем, что ответ соответствует')
    def test_questions(self, main_page, num, expected_result):
        main_page.get_url(Url.MAIN_PAGE_URL)
        result = main_page.click_on_question_get_answer(
            MainPageLocators.QUESTION_LOCATOR, MainPageLocators.ANSWER_LOCATOR, num)
        assert main_page.check_answer(result, expected_result)









