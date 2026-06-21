import allure
import pytest
from conftest import login_user
from pages.constructor_page import ConstructorPage
from data import MAIN_URL
from locators import StellarLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Конструктор")
class TestConstructor:

    @allure.title("Переход по клику на «Конструктор»")
    def test_switch_to_constructor(self, driver, registered_user):
        login_user(driver, registered_user["email"], registered_user["password"])
        try:
            WebDriverWait(driver, 3).until(EC.invisibility_of_element_located(StellarLocators.INGREDIENT_POPUP))
        except:
            pass
        driver.find_element(*StellarLocators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(StellarLocators.LOGOUT_BUTTON))
        constructor_page = ConstructorPage(driver)
        constructor_page.scroll_to_element(StellarLocators.CONSTRUCTOR_BUTTON)
        constructor_page.click_element(StellarLocators.CONSTRUCTOR_BUTTON)
        assert driver.current_url == MAIN_URL
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(StellarLocators.BUNS_TAB)
        )

    @allure.title("Клик по ингредиенту открывает всплывающее окно с деталями")
    def test_ingredient_popup_appears(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor()
        constructor_page.click_any_ingredient()
        assert constructor_page.is_ingredient_popup_displayed()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_popup_closes_by_cross(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor()
        constructor_page.click_any_ingredient()
        assert constructor_page.is_ingredient_popup_displayed()
        constructor_page.close_popup()
        assert not constructor_page.is_ingredient_popup_displayed()

    @allure.title("Счётчик ингредиента увеличивается при добавлении")
    def test_counter_increases(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor()
        ingredient_name = "Мясо бессмертных моллюсков"
        initial_counter = constructor_page.get_ingredient_counter(ingredient_name)

        constructor_page.drag_ingredient_to_constructor(ingredient_name)

        def counter_updated(driver):
            return constructor_page.get_ingredient_counter(ingredient_name) == initial_counter + 1

        WebDriverWait(driver, 30).until(lambda d: counter_updated(d))

        new_counter = constructor_page.get_ingredient_counter(ingredient_name)
        assert new_counter == initial_counter + 1