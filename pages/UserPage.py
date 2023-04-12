from selenium.webdriver.common.by import By

from actions.Actions import Actions


class UserPage:
    driver = None
    # locators
    logout_button = (By.XPATH, "//button[text()='Logout']")
    title_input = (By.ID, "title")
    date_input = (By.ID, "date")
    priority_input = (By.ID, "priority")
    add_task_button = (By.XPATH, "//input[@type='submit'][@value='Add Task']")
    tasks_list = (By.XPATH, "//ul[@id='tasks']/li")
    success_info = (By.XPATH, "//div[text()='Task added successfully']")
    success_delete = (By.XPATH, "//div[text()='Task deleted successfully!']")
    last_row_xpath = (By.XPATH, "(//tbody//tr)[last()]")
    delete_button_xpath = (By.XPATH, "//button[text()='Delete']")

    title = "Test Title"
    xpath = f"//tr[td[contains(text(), '{title}')]]"

    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)

    def click_logout_button(self):
        logout_button = self.driver.find_element(*self.logout_button)
        self.actions.click(logout_button)

    def enter_title(self, title):
        title_input = self.driver.find_element(*self.title_input)
        self.actions.sendKeys(title_input, title)

    def select_date(self, date):
        date_input = self.driver.find_element(*self.date_input)
        self.actions.sendKeys(date_input, date)

    def select_priority(self, priority):
        priority_input = self.driver.find_element(*self.priority_input)
        self.actions.select_by_visible_text(priority_input, priority)

    def click_add_task_button(self):
        add_task = self.driver.find_element(*self.add_task_button)
        self.actions.click(add_task)

    def get_task(self):
        task_title = self.driver.find_element_by_xpath(*self.xpath)
        return task_title

    def get_success_info(self):
        success_info = self.driver.find_element(*self.success_info)
        return success_info

    def get_success_delete_info(self):
        success_delete = self.driver.find_element(*self.success_delete)
        return success_delete

    def delete_task(self):
        delete_task = self.driver.find_element(*self.delete_button_xpath)
        self.actions.click(delete_task)
