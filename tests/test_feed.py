import allure
import pytest
import time
from conftest import login_user
from pages.feed_page import FeedPage
from data import MAIN_URL
from locators import StellarLocators
from helpers.order_helpers import create_order
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Лента заказов")
class TestFeed:

    @allure.title("Переход по клику на раздел «Лента заказов»")
    def test_switch_to_feed(self, driver):
        driver.get(MAIN_URL)
        feed_page = FeedPage(driver)
        feed_page.open_feed()
        assert "/feed" in driver.current_url

    @allure.title("Счётчик «Выполнено за всё время» увеличивается после создания заказа")
    def test_total_orders_counter_increases(self, driver, registered_user):
        login_user(driver, registered_user["email"], registered_user["password"])
        feed_page = FeedPage(driver)
        feed_page.open_feed()
        total_before = feed_page.get_total_orders_count()

        create_order(driver)
        try:
            WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(StellarLocators.INGREDIENT_POPUP))
        except:
            pass
        
        time.sleep(2)

        feed_page.open_feed()

        def counter_changed(driver):
            return feed_page.get_total_orders_count() > total_before

        WebDriverWait(driver, 20).until(lambda d: counter_changed(d))

        total_after = feed_page.get_total_orders_count()
        assert total_after > total_before

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_counter_increases(self, driver, registered_user):
        login_user(driver, registered_user["email"], registered_user["password"])
        feed_page = FeedPage(driver)
        feed_page.open_feed()
        today_before = feed_page.get_today_orders_count()

        create_order(driver)
        try:
            WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(StellarLocators.INGREDIENT_POPUP))
        except:
            pass
        
        time.sleep(2)

        feed_page.open_feed()

        def counter_changed(driver):
            return feed_page.get_today_orders_count() > today_before

        WebDriverWait(driver, 20).until(lambda d: counter_changed(d))

        today_after = feed_page.get_today_orders_count()
        assert today_after > today_before

    @allure.title("Номер заказа появляется в разделе «В работе» после оформления")
    def test_order_number_in_work(self, driver, registered_user):
        login_user(driver, registered_user["email"], registered_user["password"])

        order_number = create_order(driver)
        try:
            WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(StellarLocators.INGREDIENT_POPUP))
        except:
            pass
        
        time.sleep(2)

        feed_page = FeedPage(driver)
        feed_page.open_feed()

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(StellarLocators.ORDER_IN_WORK)
        )
        assert feed_page.is_order_in_work(order_number)