from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper

BASE_URL = 'https://sn.rv-school.ru/'
LOGIN_ERROR =  'Введите телефон, email или логин и пароль.'

def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == LOGIN_ERROR

def test_login_with_empty_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.enter_login("123@mail.ru")
    LoginPage.click_login()

    assert LoginPage.get_error_text() == LOGIN_ERROR


