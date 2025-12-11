import pytest
import allure

@allure.id("3521")
# @allure.issue("https://ababkin.atlassian.net/browse/KAN-2","KAN-2")
@allure.title("Проверка суммы с параметрами")
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
            pass
    with allure.step("Ввести креды"):
        pass
    with allure.step("Нажать Login"):
        with allure.step("Произошел редирект на главную страницу"):
            pass
    with allure.step("Зайти на страницу https://testops.ru"):
        with allure.step("Страница доступна, код 200"):
            pass
    with allure.step("Нажать на кнопку Войти"):
        with allure.step("Открылась панель для ввода кредов"):
            pass
    with allure.step("Ввести креды и нажать кнопку Login"):
        with allure.step("Открылась начальная страница приложения"):
            pass
    with allure.step("Проверить, что открыта главная страница"):
        with allure.step("Проверить, что отображается заголовок 'Главная'"):
            pass
    with allure.step("Проверить наличие элемента 'Профиль'"):
        with allure.step("Элемент 'Профиль' отображается в шапке"):
            pass
    with allure.step("Нажать на элемент 'Профиль'"):
        with allure.step("Открылась страница профиля пользователя"):
            pass
    with allure.step("Проверить, что открыта страница профиля"):
        with allure.step("Проверить, что отображается имя пользователя"):
            pass

@allure.id("3532")
@allure.title("Сломанный тест-кейс")
@allure.label("owner", "dedkin")
def test_broken():
    with allure.step("Подготовка тестовых данных"):
        with allure.step("Тест сломался с Exception"):
            result = 1 / 0
    with allure.step("Тело теста"):
        pass

@allure.title("Пропущенный тест-кейс")
@allure.label("owner", "dedkin")
@pytest.mark.skip("Пропускаем тест")
def test_skip():
    with allure.step("Подготовка тестовых данных"):
        with allure.step("Тест сломался с Exception"):
            result = 1 / 0
    with allure.step("Тело теста"):
        pass

@allure.title("Пропущенный тест-кейс")
@allure.label("owner", "dedkin")
@pytest.mark.xfail("Пропускаем если падаетл")
def test_xfail():
    with allure.step("Подготовка тестовых данных"):
        with allure.step("Тест сломался с Exception"):
            result = 1 / 0
    with allure.step("Тело теста"):
        pass