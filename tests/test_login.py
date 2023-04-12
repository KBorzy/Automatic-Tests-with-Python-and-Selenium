from pages.LoginPage import LoginPage
from pages.UserPage import UserPage
from utilities.Data import Data
from pathlib import Path

ROOT_PATH = str(Path(__file__).parent.parent)


def test_login(setup):
    driver = setup

    test_data = Data.get_test_input_data(ROOT_PATH + "/resources/data.xlsx")
    email = test_data['email']
    password = test_data['password']

    # Inicjalizacja strony logowania
    login_page = LoginPage(driver)

    # Wprowadzenie danych do logowania
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login_button()
