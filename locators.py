from selenium.webdriver.common.by import By

class StellarLocators:
    # ---------- Регистрация ----------
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    REGISTER_NAME = (By.XPATH, "(//input[@type='text'])[1]")
    REGISTER_EMAIL = (By.XPATH, "(//input[@type='text'])[2]")
    REGISTER_PASSWORD = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    REGISTER_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default']")

    # ---------- Вход ----------
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    LOGIN_BUTTON_PERSONAL = (By.XPATH, "//a[text()='Личный кабинет']")
    LOGIN_BUTTON_REGISTER_FORM = (By.XPATH, "//a[text()='Войти']")
    LOGIN_BUTTON_RECOVERY_FORM = (By.XPATH, "//a[text()='Войти']")
    LOGIN_EMAIL = (By.NAME, "name")
    LOGIN_PASSWORD = (By.NAME, "Пароль")
    LOGIN_SUBMIT = (By.XPATH, "//button[text()='Войти']")

    # ---------- Личный кабинет ----------
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[contains(@href, '/account')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    # ---------- Конструктор и логотип ----------
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.XPATH, "//a[contains(@href, '/')]//*[local-name()='svg']")
    INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    # Используем contains(text()) для частичного совпадения
    INGREDIENT_BY_NAME = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient') and .//p[contains(text(), '{name}')]]")
    INGREDIENT_POPUP = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    CLOSE_POPUP_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    COUNTER = (By.XPATH, ".//div[contains(@class, 'counter_counter')]")
    # Исправленный локатор для корзины (область конструктора)
    CONSTRUCTOR_TARGET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")

    # ---------- Вкладки конструктора ----------
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span")

    # ---------- Лента заказов ----------
    ORDERS_FEED_LINK = (By.XPATH, "//a[contains(@href, '/feed')]")
    ORDERS_LIST = (By.XPATH, "//ul[contains(@class, 'OrdersList_list')]/li")
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'за все время')]/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'за сегодня')]/following-sibling::p")
    ORDER_IN_WORK = (By.XPATH, "//div[contains(@class, 'OrderFeed_orderNumber')]")
    
    # ---------- Оформление заказа ----------
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER_IN_MODAL = ORDER_NUMBER_IN_MODAL = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large') and contains(@class, 'Modal_modal__title')]")