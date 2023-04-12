from selenium.webdriver.support.ui import Select

class Actions:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        element.click()

    def sendKeys(self, inputField, value):
        inputField.send_keys(value)

    def getText(self, element):
        return element.text

    def select_by_visible_text(self, select_element, visible_text):
        select = Select(select_element)
        select.select_by_visible_text(visible_text)
