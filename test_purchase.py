import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

logging.basicConfig(level=logging.INFO)


def test_purchase(driver):

    # Авторизация
    driver.get("https://www.saucedemo.com/")
    user_name_input = driver.find_element(By.ID, "user-name")
    user_name_input.send_keys("standard_user")

    user_password_input = driver.find_element(By.ID, "password")
    user_password_input.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Проверяем, что авторизация успешна
    assert "inventory.html" in driver.current_url, "Authorization failed!"
    logging.info("Authorization successful!")

    # Добавляем в корзину случайный товар со страницы и запоминаем его название
    item = driver.find_element(By.CLASS_NAME, "inventory_item_description")
    item_name = item.find_element(By.CLASS_NAME, "inventory_item_name")
    expected_item_name = item_name.text
    add_to_cart_button = item.find_element(By.XPATH, ".//button[text()='Add to cart']")
    add_to_cart_button.click()

    # Идем в корзину и убеждаемся, что в ней именно тот товар, который мы добавили
    cart_button = driver.find_element(By.XPATH, "//a[contains(@class, 'shopping_cart_link')]")
    cart_button.click()

    item_name = driver.find_element(By.XPATH,
                                    f"//div[@class='inventory_item_name' and text()='{expected_item_name}']")
    assert item_name != expected_item_name, f"The selected item named '{expected_item_name}' was not found in the cart."
    logging.info(f"The selected item named '{expected_item_name}' was found in the cart.")

    # Оформление заказа
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    first_name_input = driver.find_element(By.ID, "first-name")
    first_name_input.send_keys("Wendy")

    last_name_input = driver.find_element(By.ID, "last-name")
    last_name_input.send_keys("Wobblebottom")

    postal_code_input = driver.find_element(By.ID, "postal-code")
    postal_code_input.send_keys("123456")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    # Завершение покупки и итоговая проверка
    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()

    assert "checkout-complete.html" in driver.current_url, "Order failed!"
    logging.info("Order completed successfully!")
