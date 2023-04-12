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
