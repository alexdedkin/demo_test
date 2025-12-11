import pytest
import allure

@allure.id("3521")
# @allure.issue("https://ababkin.atlassian.net/browse/KAN-2","KAN-2")
@allure.title("Проверка суммы с параметрами2")
@allure.tag("e2e", "regress")
@allure.label("owner", "dedkin")
@allure.description('Это поле описание "description"')
@allure.feature("o2-1214 Сумма чисел")
@pytest.mark.parametrize('x, y, expected', [
    pytest.param(1, 2, 3, id="1+2=3"),
    pytest.param(5, 6, 11, id="5+6=11"),
    pytest.param(-1, 1, 0, id="-1+1=0"),
    pytest.param(0, 0, 1, id="0+0=0"),
])
def test_sum_detailed(x, y, expected):
    result = func_sum(x, y)
    with allure.step(f'Проверить сумму: {x} + {y} = {result}'):
        assert result == expected, f"{x} + {y} = {result}, ожидалось {expected}"

def func_sum(x, y):
    return x+y

@allure.id("3518")
@allure.title("Проверка авторизации")
@allure.tag("e2e", "regress")
@allure.label("owner", "dedkin")
@allure.description('Это поле описание "description"')
@allure.feature("o2-1213 Авторизация")
def test_something():
    with allure.step("Auth"):
        with allure.step("Перейти на страницу авторизации"):
            # Имитация перехода на страницу авторизации
            # Например: driver.get("https://testops.ru/login")
            pass
    with allure.step("Ввести креды"):
        # Имитация ввода логина и пароля
        # Например: driver.find_element(By.ID, "login").send_keys("username")
        # driver.find_element(By.ID, "password").send_keys("password")
        pass
    with allure.step("Нажать Login"):
        with allure.step("Произошел редирект на главную страницу"):
            # Имитация нажатия кнопки входа
            # Например: driver.find_element(By.ID, "submit").click()
            pass
    with allure.step("Зайти на страницу https://testops.ru"):
        with allure.step("Страница доступна, код 200"):
            # Проверка доступности страницы через HTTP-запрос
            # Например: response = requests.get("https://testops.ru")
            # assert response.status_code == 200
            pass
    with allure.step("Нажать на кнопку Войти"):
        with allure.step("Открылась панель для ввода кредов"):
            # Имитация клика по кнопке "Войти" в шапке
            # Например: driver.find_element(By.CLASS_NAME, "login-button").click()
            pass
    with allure.step("Ввести креды и нажать кнопку Login"):
        with allure.step("Открылась начальная страница приложения"):
            # Имитация ввода учетных данных и нажатия кнопки входа
            # Например: driver.find_element(By.ID, "username").send_keys("user")
            # driver.find_element(By.ID, "password").send_keys("pass")
            # driver.find_element(By.ID, "login-btn").click()
            pass
    with allure.step("Проверить, что открыта главная страница"):
        with allure.step("Проверить, что отображается заголовок 'Главная'"):
            # Проверка наличия заголовка на странице
            # Например: assert "Главная" in driver.title
            pass
    with allure.step("Проверить наличие элемента 'Профиль'"):
        with allure.step("Элемент 'Профиль' отображается в шапке"):
            # Проверка наличия элемента "Профиль" в навигационной шапке
            # Например: profile_element = driver.find_element(By.CLASS_NAME, "profile-link")
            # assert profile_element.is_displayed()
            pass
    with allure.step("Нажать на элемент 'Профиль'"):
        with allure.step("Открылась страница профиля пользователя"):
            # Имитация клика по элементу "Профиль"
            # Например: driver.find_element(By.CLASS_NAME, "profile-link").click()
            pass
    with allure.step("Проверить, что открыта страница профиля"):
        with allure.step("Проверить, что отображается имя пользователя"):
            # Проверка отображения имени пользователя на странице профиля
            # Например: username = driver.find_element(By.CLASS_NAME, "username").text
            # assert "Иван Иванов" in username
            pass
