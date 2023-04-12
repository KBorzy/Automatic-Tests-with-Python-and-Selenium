from actions.Actions import Actions
from selenium.webdriver.common.by import By

class LoginPage:
    driver = None
    #locators
    email_input_field = (By.ID, "email")
    password_input_field = (By.ID, "password")
    login_button = (By.XPATH, "//button[text()='Login']")

    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)

    def enter_email(self, email):
        email_input_field = self.driver.find_element(*self.email_input_field)
        self.actions.sendKeys(email_input_field, email)

    def enter_password(self, password):
        password_input_field = self.driver.find_element(*self.password_input_field)
        self.actions.sendKeys(password_input_field, password)

    def click_login_button(self):
        login_button = self.driver.find_element(*self.login_button)
        self.actions.click(login_button)