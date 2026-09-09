import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper
from pages.RegistrationPage import RegistrationPageHelper

BASE_URL = 'https://sn.rv-school.ru/'

def test_registration_random_country(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelper(browser)
    RegistrationPage.click_register_by_phone()
    selected_country, country_code = RegistrationPage.select_random_country()

    assert country_code in selected_country, (f'Код страны {country_code} отсутствует в выбранной стране {selected_country}')
