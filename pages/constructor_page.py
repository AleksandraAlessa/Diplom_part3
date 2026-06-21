import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import StellarLocators
from data import MAIN_URL

class ConstructorPage(BasePage):

    @allure.step("Открыть конструктор (главную страницу)")
    def open_constructor(self):
        self.open(MAIN_URL)

    @allure.step("Кликнуть на ингредиент по названию {ingredient_name}")
    def click_ingredient_by_name(self, ingredient_name):
        locator = (By.XPATH, StellarLocators.INGREDIENT_BY_NAME[1].format(name=ingredient_name))
        self.click_element(locator)

    @allure.step("Кликнуть на первый попавшийся ингредиент")
    def click_any_ingredient(self):
        self.click_element(StellarLocators.INGREDIENT)

    @allure.step("Получить счётчик ингредиента по названию {ingredient_name}")
    def get_ingredient_counter(self, ingredient_name):
        ingredient_locator = (By.XPATH, StellarLocators.INGREDIENT_BY_NAME[1].format(name=ingredient_name))
        ingredient = self.find_element(ingredient_locator)
        try:
            counter = ingredient.find_element(*StellarLocators.COUNTER)  # здесь звёздочка нужна (вызов на элементе)
            return int(counter.text)
        except:
            return 0

    @allure.step("Проверить, что попап с деталями ингредиента отображается")
    def is_ingredient_popup_displayed(self):
        return self.is_element_displayed(StellarLocators.INGREDIENT_POPUP)

    @allure.step("Закрыть попап крестиком")
    def close_popup(self):
        self.find_element(StellarLocators.CLOSE_POPUP_BUTTON).click()
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(StellarLocators.INGREDIENT_POPUP)
        )

    @allure.step("Добавить ингредиент {ingredient_name} в заказ (перетаскиванием)")
    def add_ingredient_via_popup(self, ingredient_name):
        # Используем перетаскивание вместо кнопки «Добавить»
        self.drag_ingredient_to_constructor(ingredient_name)
        # Ждём, пока попап закроется (он закрывается автоматически после перетаскивания)
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(StellarLocators.INGREDIENT_POPUP)
        )

    @allure.step("Перетащить ингредиент {ingredient_name} в конструктор")
    def drag_ingredient_to_constructor(self, ingredient_name):
        ingredient_locator = (By.XPATH, StellarLocators.INGREDIENT_BY_NAME[1].format(name=ingredient_name))
        self.drag_and_drop(ingredient_locator, StellarLocators.CONSTRUCTOR_TARGET)