from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_LOCATOR = By.XPATH, ".//input[@placeholder='* Имя']"
    SURNAME_LOCATOR = By.XPATH, ".//input[@placeholder='* Фамилия']"
    ADDRESS_LOCATOR = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_INPUT_LOCATOR = By.XPATH, ".//input[@placeholder='* Станция метро']"
    PHONE_LOCATOR = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    METRO_STATION_LOCATOR = By.XPATH, ".//div[text()='{}']"
    FURTHER_BUTTON = By.XPATH, ".//button[text()='Далее']"
    DATE_LOCATOR = By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"
    RENTAL_DURATION_INPUT = By.XPATH, ".//div[text()='* Срок аренды']"
    RENTAL_DURATION_VALUE = By.XPATH, ".//div[text()='{}']"
    ORDER_BUTTON_IN_ORDER = By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Заказать']"
    CONFIRM_BUTTON = By.XPATH, ".//button[text()='Да']"
    CONFIRMATION_LOCATOR = By.XPATH, ".//div[text()='Заказ оформлен']"

