from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPageLocators:
    # Вкладки
    LOGIN_TAB = (By.XPATH, "//a[@data-l='t,login_tab']")
    QR_TAB = (By.XPATH, "//a[@data-l='t,qr_tab']")

    # Поля ввода
    EMAIL_INPUT = (By.ID, "field_email")
    PASSWORD_INPUT = (By.ID, "field_password")

    # Кнопка показать/скрыть пароль
    PASSWORD_VISIBILITY_BUTTON = (By.XPATH, "//button[.//span[contains(text(),'пароль')]]")

    # Кнопки
    LOGIN_BUTTON = (By.XPATH, "//button[@data-test-id='enter-action']")
    LOGIN_BY_QR_BUTTON = (By.XPATH, "//button[@label='Войти по QR-коду']")
    REGISTER_BUTTON = (By.XPATH, "//button[@data-test-id='registration-action']")

    # Ссылки
    CANT_LOGIN_LINK = (By.XPATH, "//button[@data-test-id='forgot-password-link']")

    # Социальная авторизация
    VK_LOGIN = (By.XPATH, "//a[@data-l='t,vkc']")
    MAIL_LOGIN = (By.XPATH, "//a[@data-provider='MAILRU']")
    YA_LOGIN = (By.XPATH, "//a[@data-provider='YANDEX']")


class LoginPageHelper(BasePage):
    pass