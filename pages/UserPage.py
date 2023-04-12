from selenium.webdriver.common.by import By
from actions.Actions import Actions

class UserPage:
    driver = None
    #locators
    logout_button = (By.XPATH, "//button[text()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)

    def click_logout_button(self):
        logout_button = self.driver.find_element(*self.logout_button)
        self.actions.click(logout_button)