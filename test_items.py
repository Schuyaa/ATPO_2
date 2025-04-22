import time
import pytest
from selenium.webdriver.common.by import By


# Тест для проверки кнопки добавления в корзину на странице товара
def test_add_to_cart_button(browser):
    # Открываем страницу товара
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    
    # Вставляем паузу, чтобы проверить визуально, что интерфейс на нужном языке
    time.sleep(30)
    
    # Ищем кнопку добавления в корзину
    button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    
    # Проверяем, что кнопка есть на странице
    assert button.is_displayed(), "Add to basket button is not displayed!"
    
    # Печатаем текст на кнопке для проверки правильности языка
    print(f"Text on the button: {button.text}")
    
    # Проводим проверку текста кнопки для указанного языка
    assert button.text in ['Add to basket', 'Añadir al carrito', 'Ajouter au panier'], \
        f"Unexpected button text: {button.text}"

