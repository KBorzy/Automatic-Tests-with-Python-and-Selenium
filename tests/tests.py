from pages.LoginPage import LoginPage
from pages.UserPage import UserPage
from utilities.Data import Data
from pathlib import Path
from time import sleep

ROOT_PATH = str(Path(__file__).parent.parent)


def tests(setup):
    driver = setup

    test_data = Data.get_test_input_data(ROOT_PATH + "/resources/data.xlsx")
    email = test_data['email']
    password = test_data['password']

    login_page = LoginPage(driver)

    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login_button()

    sleep(2)
    assert "Tasks" in driver.title
    sleep(1)


def test_add_task(setup):
    driver = setup

    title = 'Test Title'
    date = '01.01.2001'
    priority = 'Low'

    user_page = UserPage(driver)

    user_page.enter_title(title)
    user_page.select_date(date)
    user_page.select_priority(priority)
    user_page.click_add_task_button()

    sleep(2)

    assert 'Task added successfully' == user_page.get_success_info().text
    sleep(1)


def test_delete_task(setup):
    driver = setup
    user_page = UserPage(driver)
    user_page.delete_task()

    sleep(2)
    assert 'Task deleted successfully!' == user_page.get_success_delete_info().text
    sleep(1)


def test_logout(setup):
    driver = setup
    user_page = UserPage(driver)
    user_page.click_logout_button()

    sleep(2)
    assert "Login" in driver.title
    sleep(1)
