import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Обработка параметра language из командной строки
def pytest_addoption(parser):
    parser.addoption(
        '--language', action='store', default='en', help="Choose the language for the tests"
    )


# Фикстура для запуска браузера с выбранным языком
@pytest.fixture
def browser(request):
    language = request.config.getoption('language')
    options = Options()
    options.add_argument(f'--lang={language}')  # Устанавливаем язык интерфейса браузера
    print(f"\nSetting up browser with language: {language}")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nTearing down browser...")
    browser.quit()

