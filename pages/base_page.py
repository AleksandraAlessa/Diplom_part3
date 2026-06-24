import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Кликнуть на элемент {locator}")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    @allure.step("Ввести текст '{text}' в поле {locator}")
    def add_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return element

    @allure.step("Получить текст из элемента {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Прокрутить до элемента {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def is_element_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False

    @allure.step("Перетащить элемент из {source_locator} в {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", source)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target)
        time.sleep(1)  # увеличили паузу до 1 секунды
        ActionChains(self.driver).click_and_hold(source).move_to_element(target).release().perform()
        # дополнительная пауза после перетаскивания
        time.sleep(0.5)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)