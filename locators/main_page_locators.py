from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_LOCATOR = By.ID, 'accordion__heading-{}'
    ANSWER_LOCATOR = By.ID, 'accordion__panel-{}'
    ORDER_BUTTON_HEADER = By.CLASS_NAME, 'Button_Button__ra12g'
    ORDER_BUTTON = By.CLASS_NAME, 'Home_FinishButton__1_cWm'
    YANDEX_LOGO = By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]"
    SCOOTER_LOGO = By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]"
    ANSWERS_TITLE = By.XPATH, ".//div[contains(@class, 'Home_SubHeader') and text()='Вопросы о важном']"

