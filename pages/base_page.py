import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Ждем кликабельности элемента')
    def wait_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 6).until(
            expected_conditions.element_to_be_clickable(locator))

    @allure.step('Ждем видимости элемента')
    def wait_element_is_visible(self, locator):
        return WebDriverWait(self.driver, 6).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step('Нажимаем на элемент')
    def click_on_element(self, locator):
        element = self.find_element(locator)
        self.wait_element_is_clickable(locator)
        element.click()

    @allure.step('Получаем текст элемента')
    def get_text_from_element(self, locator):
        return self.find_element(locator).text

    @allure.step('Передаем текст в элемент')
    def set_text_to_element(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    @allure.step('Скролим до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Собираем нужный локатор')
    def make_locator(self, locator, num):
        method, locator = locator
        locator = (method, locator.format(num))
        return locator

    @allure.step('Переходим на страницу')
    def get_url(self, url):
        return self.driver.get(url)

    def switch_to_new_window(self):
        current_window = self.driver.current_window_handle
        self.find_window()
        all_windows = self.driver.window_handles
        new_window = next(window for window in all_windows if window != current_window)
        self.driver.switch_to.window(new_window)

    def find_window(self, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.number_of_windows_to_be(2))

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url
