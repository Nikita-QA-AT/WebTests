from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import allure
import random


class RegistrationPageLocators:

    # Регистрация по email
    DISPLAY_NAME_INPUT = (By.XPATH, "//input[@data-test-id='display-name']")
    USERNAME_INPUT = (By.XPATH, "//input[@data-test-id='username']")
    EMAIL_INPUT = (By.XPATH, "//input[@data-test-id='email']")
    PHONE_INPUT = (By.XPATH, "//input[@data-test-id='phone']")
    PASSWORD_INPUT = (By.XPATH, "//input[@data-test-id='register-password']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@data-test-id='confirm-password']")
    REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[@data-test-id='register-submit-btn']")
    REGISTER_ERROR = (By.XPATH, "//*[@data-test-id='register-error']")

    # Переключение на регистрацию по телефону
    REGISTER_BY_PHONE_BUTTON = (By.XPATH, "//button[@data-test-id='register-phone-toggle']")

    # Регистрация по телефону
    COUNTRY_LIST = (By.XPATH, "//*[@class='phone-country-select']")
    COUNTRY_ITEM = (By.XPATH, "//*[@class='phone-country-select']/option")
    PHONE_NUMBER_INPUT = (By.XPATH, "//input[@data-test-id='phone-number-input']")
    SEND_CODE_BUTTON = (By.XPATH, "//button[@data-test-id='phone-send-code-btn']")
    BACK_TO_EMAIL_REGISTRATION_BUTTON = (By.XPATH, "//button[@data-test-id='phone-cancel-btn']")



class RegistrationPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
            self.find_element(RegistrationPageLocators.DISPLAY_NAME_INPUT)
            self.find_element(RegistrationPageLocators.USERNAME_INPUT)
            self.find_element(RegistrationPageLocators.EMAIL_INPUT)
            self.find_element(RegistrationPageLocators.PHONE_INPUT)
            self.find_element(RegistrationPageLocators.PASSWORD_INPUT)
            self.find_element(RegistrationPageLocators.CONFIRM_PASSWORD_INPUT)
            self.find_element(RegistrationPageLocators.REGISTER_SUBMIT_BUTTON)
            self.find_element(RegistrationPageLocators.REGISTER_BY_PHONE_BUTTON)

    @allure.step('Выбрали рандомную страну из выпадающего списка')
    def select_random_country(self):
        random_number = random.randint(0, 39)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        selected_country = country_items[random_number]
        selected_country.click()

        return selected_country.text, selected_country.get_attribute('value')



    @allure.step('Нажимаем на кнопку "Регистрация по телефону"')
    def click_register_by_phone(self):
        self.attach_screenshot()
        self.find_element(RegistrationPageLocators.REGISTER_BY_PHONE_BUTTON).click()