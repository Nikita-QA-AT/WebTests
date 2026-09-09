import allure
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPageLocators:
    # Вкладки
    LOGIN_TAB = (By.XPATH, "//div[@data-test-id='tab-login']")
    QR_TAB = (By.XPATH, "//div[@data-test-id='tab-qr']")

    # Поля ввода
    EMAIL_INPUT = (By.XPATH, "//input[@data-test-id='login-phone-email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@data-test-id='login-password']")

    # Кнопки
    LOGIN_BUTTON = (By.XPATH, "//button[@data-test-id='login-submit-btn']")
    HERO_LOGIN_BUTTON = (By.XPATH, "//button[@data-test-id='hero-login-btn']")
    REGISTER_BUTTON = (By.XPATH, "//button[@data-test-id='hero-register-btn']")
    CANCEL_BUTTON = (By.XPATH, "//button[@data-test-id='lockout-cancel-btn']")
    RECOVERY_BUTTON = (By.XPATH, "//a[@data-test-id='lockout-recover-btn']")
    REGISTER_LOCKOUT_BUTTON = (By.XPATH, "//button[@data-test-id='lockout-register-btn']")


    # Ссылки
    CANT_LOGIN_LINK = (By.XPATH, "//a[@data-test-id='forgot-password-link']")

    # Ошибки
    ERROR_TEXT = (By.ID, "login-error")

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.EMAIL_INPUT)
        self.find_element(LoginPageLocators.PASSWORD_INPUT)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.HERO_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.REGISTER_BUTTON)
        self.find_element(LoginPageLocators.CANT_LOGIN_LINK)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text


    @allure.step('Вводим логин')
    def type_login(self, login):
        self.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(login)
        self.attach_screenshot()


    @allure.step('Вводим пароль')
    def type_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.attach_screenshot()


    @allure.step('Нажимаем на кнопку "Восстановить"')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RECOVERY_BUTTON).click()

    @allure.step('Нажимаем на кнопку "Зарегистрироваться"')
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTER_BUTTON).click()