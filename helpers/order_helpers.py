import allure
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.constructor_page import ConstructorPage
from locators import StellarLocators

@allure.step("Создать заказ через UI")
def create_order(driver, ingredients=None):
    if ingredients is None:
        ingredients = ["Мясо бессмертных моллюсков"] 
    constructor_page = ConstructorPage(driver)
    
    constructor_page.open_constructor()

    for ingredient in ingredients:
        constructor_page.drag_ingredient_to_constructor(ingredient)

    constructor_page.click_element(StellarLocators.ORDER_BUTTON)

    order_number_element = WebDriverWait(driver, 25).until(
        EC.visibility_of_element_located(StellarLocators.ORDER_NUMBER_IN_MODAL)
    )
    order_number = order_number_element.text

    constructor_page.click_element(StellarLocators.CLOSE_POPUP_BUTTON)
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located(StellarLocators.INGREDIENT_POPUP)
    )
    return order_number