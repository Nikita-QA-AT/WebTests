import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class RecoveryPageLocators:
    PHONE_BUTTON = (By.XPATH, "//a[@data-test-id='recovery-phone-btn']")
    EMAIL_BUTTON = (By.XPATH, "//a[@data-test-id='recovery-email-btn']")
    QR_CODE = (By.XPATH, "//div[@data-test-id='qr-image']")
    SUPPORT_BUTTON = (By.XPATH, "//button[@data-test-id='support-contact-btn']")




class RecoveryPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(RecoveryPageLocators.PHONE_BUTTON)
        self.find_element(RecoveryPageLocators.EMAIL_BUTTON)
        self.find_element(RecoveryPageLocators.QR_CODE)
        self.find_element(RecoveryPageLocators.SUPPORT_BUTTON)
