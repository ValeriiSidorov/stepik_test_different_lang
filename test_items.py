from selenium.webdriver.common.by import By
import time


def test_add_to_cart_button(browser):
    browser.get("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    # time.sleep(30)
    
    # Код для проверки отображения содержимого на сайте
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert add_to_cart_button is not None, "Кнопка 'Добавить в корзину' не найдена на странице"
 
