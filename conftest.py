import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Specify the language for testing")

@pytest.fixture
def language(request):
    return request.config.getoption("--language")
    
# Фикстура для настройки браузера
@pytest.fixture
def browser(request):
    language = request.config.getoption("--language")
    options = Options()

    # Устанавливаем язык браузера
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    # Инициализация драйвера браузера
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
