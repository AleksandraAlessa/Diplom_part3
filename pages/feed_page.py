import allure
import time
from selenium.webdriver.support.ui import WebDriverWait  # <-- добавлен импорт
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import StellarLocators

class FeedPage(BasePage):

    @allure.step("Открыть ленту заказов")
    def open_feed(self):
        try:
            self.click_element(StellarLocators.ORDERS_FEED_LINK)
        except Exception:
            # Если клик перехвачен модалкой – закрываем её и пробуем снова
            try:
                self.find_element(StellarLocators.CLOSE_POPUP_BUTTON).click()
                WebDriverWait(self.driver, 3).until(
                    EC.invisibility_of_element_located(StellarLocators.INGREDIENT_POPUP)
                )
            except:
                pass
            # Повторный клик по ссылке
            self.click_element(StellarLocators.ORDERS_FEED_LINK)

        self.wait.until(EC.url_contains("/feed"))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(StellarLocators.TOTAL_ORDERS_COUNTER)
        )

    @allure.step("Получить количество заказов за всё время")
    def get_total_orders_count(self):
        return int(self.get_text(StellarLocators.TOTAL_ORDERS_COUNTER))

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        return int(self.get_text(StellarLocators.TODAY_ORDERS_COUNTER))

    @allure.step("Получить список номеров заказов в разделе 'В работе'")
    def get_orders_in_work(self):
        elements = self.find_elements(StellarLocators.ORDER_IN_WORK)
        return [el.text for el in elements]

    @allure.step("Проверить, что номер заказа {order_number} отображается в 'В работе'")
    def is_order_in_work(self, order_number):
        orders = self.get_orders_in_work()
        return str(order_number) in orders