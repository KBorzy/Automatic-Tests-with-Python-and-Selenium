import pytest
from selenium import webdriver
from pathlib import Path

ROOT_PATH = str(Path(__file__).parent.parent)


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(ROOT_PATH + '/resources/chromedriver.exe')
    driver.get('http://kborzyszkowski.pythonanywhere.com/')
    yield driver
    driver.quit()
