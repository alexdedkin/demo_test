from playwright.sync_api import Page
import allure

class AuthPage:
    """Page Object для страницы авторизации"""
    
    def __init__(self, page: Page):
        self.page = page
        # Локаторы
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")
        self.inventory_container = page.locator(".inventory_container")
        
    @allure.step("Открыть страницу авторизации")
    def open(self):
        """Открыть страницу авторизации"""
        self.page.goto("https://www.saucedemo.com/")
        
    @allure.step("Ввести логин '{username}'")
    def enter_username(self, username: str):
        """Ввести имя пользователя"""
        self.username_input.fill(username)
        
    @allure.step("Ввести пароль '{password}'")
    def enter_password(self, password: str):
        """Ввести пароль"""
        self.password_input.fill(password)
        
    @allure.step("Нажать кнопку входа")
    def click_login_button(self):
        """Нажать кнопку входа"""
        self.login_button.click()
        
    @allure.step("Авторизация пользователя '{username}'")
    def login(self, username: str, password: str):
        """Выполнить авторизацию"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        
    @allure.step("Проверить отображение сообщения об ошибке")
    def is_error_message_visible(self) -> bool:
        """Проверить, отображается ли сообщение об ошибке"""
        return self.error_message.is_visible()
        
    @allure.step("Проверить успешную авторизацию")
    def is_login_successful(self) -> bool:
        """Проверить успешную авторизацию"""
        return self.inventory_container.is_visible()
        
    @allure.step("Получить текст сообщения об ошибке")
    def get_error_message_text(self) -> str:
        """Получить текст сообщения об ошибке"""
        return self.error_message.text_content()