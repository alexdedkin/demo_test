import pytest
import allure
from page_objects.auth_page import AuthPage

# Список пользователей и их ожидаемых результатов
USERS_DATA = [
    ("standard_user", "secret_sauce", True, "Успешная авторизация стандартного пользователя"),
    ("locked_out_user", "secret_sauce", False, "Блокировка пользователя"),
    ("problem_user", "secret_sauce", True, "Успешная авторизация пользователя с проблемами"),
    ("performance_glitch_user", "secret_sauce", True, "Успешная авторизация пользователя с glitch"),
    ("error_user", "secret_sauce", True, "Ошибка авторизации пользователя с ошибкой"),
    ("visual_user", "secret_sauce", True, "Успешная авторизация визуального пользователя")
]

@pytest.mark.parametrize("username, password, expected_success, description", USERS_DATA)
@allure.feature("Авторизация")
@allure.story("Тестирование авторизации пользователей")
@allure.title("Тест авторизации пользователя {username}")
def test_user_authentication(page, username, password, expected_success, description):
    """Тест авторизации различных пользователей"""
    with allure.step(f"Выполняется тест: {description}"):
        # Создаем экземпляр страницы авторизации
        auth_page = AuthPage(page)
        
        # Открываем страницу авторизации
        auth_page.open()
        
        # Выполняем авторизацию
        auth_page.login(username, password)
        
        # Проверяем результат
        if expected_success:
            with allure.step("Проверка успешной авторизации"):
                assert auth_page.is_login_successful(), f"Авторизация пользователя {username} не удалась, хотя ожидалась успешная авторизация"
                allure.attach(page.screenshot(), name="Успешная авторизация", attachment_type=allure.attachment_type.PNG)
        else:
            with allure.step("Проверка неуспешной авторизации"):
                assert auth_page.is_error_message_visible(), f"Авторизация пользователя {username} была успешной, хотя ожидалась неуспешная авторизация"
                error_text = auth_page.get_error_message_text()
                allure.attach(error_text, name="Сообщение об ошибке", attachment_type=allure.attachment_type.TEXT)
                assert "Epic sadface" in error_text or "locked out" in error_text.lower(), f"Ожидалось сообщение об ошибке, получено: {error_text}"

@allure.feature("Авторизация")
@allure.story("Тестирование неуспешной авторизации с неверным паролем")
@allure.title("Тест авторизации с неверным паролем")
def test_invalid_password_authentication(page):
    """Тест авторизации с неверным паролем"""
    with allure.step("Тест авторизации с неверным паролем"):
        auth_page = AuthPage(page)
        auth_page.open()
        auth_page.login("standard_user", "wrong_password")
        
        with allure.step("Проверка сообщения об ошибке"):
            assert auth_page.is_error_message_visible(), "Не отобразилось сообщение об ошибке при вводе неверного пароля"
            error_text = auth_page.get_error_message_text()
            allure.attach(error_text, name="Сообщение об ошибке", attachment_type=allure.attachment_type.TEXT)
            assert "Epic sadface" in error_text, f"Ожидалось сообщение об ошибке, получено: {error_text}"

@allure.feature("Авторизация")
@allure.story("Тестирование неуспешной авторизации без ввода данных")
@allure.title("Тест авторизации без ввода данных")
def test_empty_fields_authentication(page):
    """Тест авторизации без ввода данных"""
    with allure.step("Тест авторизации без ввода данных"):
        auth_page = AuthPage(page)
        auth_page.open()
        auth_page.click_login_button()
        
        with allure.step("Проверка сообщения об ошибке"):
            assert auth_page.is_error_message_visible(), "Не отобразилось сообщение об ошибке при пустых полях"
            error_text = auth_page.get_error_message_text()
            allure.attach(error_text, name="Сообщение об ошибке", attachment_type=allure.attachment_type.TEXT)
            assert "Epic sadface" in error_text, f"Ожидалось сообщение об ошибке, получено: {error_text}"