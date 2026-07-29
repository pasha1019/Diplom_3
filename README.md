# Diplom_3: UI-тесты для Stellar Burgers

UI-автотесты для приложения [Stellar Burgers](https://qa-stellarburgers.education-services.ru) — учебный проект (Дипломная работа, часть 3).

## Стек

| Инструмент | Назначение |
|------------|-----------|
| Python ≥ 3.10 | Язык написания тестов |
| Selenium 4 | WebDriver для управления браузером |
| pytest | Тестовый фреймворк |
| Allure | Генерация HTML-отчётов |
| Faker | Генерация тестовых данных |
| requests | API-вызовы (регистрация, логин, удаление пользователя) |
| Ruff | Линтер |
| mypy | Статический типизатор |

## Структура проекта

```
.
├── conftest.py            # Фикстуры: driver, registered_user, order_created; хук скриншотов
├── pyproject.toml         # Конфигурация pytest, ruff, mypy, allure
├── requirements.txt       # Зависимости
├── AGENTS.md              # Инструкции для AI-агентов
│
├── browser/
│   └── browser_factory.py # Создание WebDriver (Chrome 1920×1080, Firefox; headless)
│
├── pages/                 # Page Object классы
│   ├── base_page.py       # Базовый класс: wait, click, send_keys, get_text
│   ├── main_page.py       # Конструктор бургеров, навигация, drag-and-drop
│   ├── login_page.py      # Страница входа
│   ├── register_page.py   # Страница регистрации
│   ├── account_page.py    # Личный кабинет
│   ├── feed_page.py       # Лента заказов
│   └── recovery_page.py   # Восстановление пароля
│
├── locators/              # Локаторы (Selenium By-tuples)
│   ├── main_page_locators.py
│   ├── login_page_locators.py
│   ├── register_page_locators.py
│   ├── account_page_locators.py
│   ├── feed_page_locators.py
│   └── recovery_page_locators.py
│
├── data/
│   ├── test_data.py       # URLs + Faker-генераторы (email, password, name)
│   └── api_client.py      # API-клиент: register_user, login_user, delete_user
│
└── tests/
    ├── test_password_recovery.py  # 3 теста: восстановление пароля
    ├── test_personal_account.py   # 3 теста: личный кабинет
    ├── test_main_functional.py    # 6 тестов: основной функционал
    └── test_feed_page.py          # 5 тестов: лента заказов
```

## Установка и запуск

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск всех тестов (Chrome + Firefox, headless)
pytest

# Запуск только Chrome
pytest -k chrome

# Запуск только Firefox
pytest -k firefox

# Запуск тестов конкретного файла
pytest tests/test_main_functional.py

# Запуск одного теста по имени
pytest -k test_navigate_to_constructor

# Запуск по маркеру
pytest -m password_recovery
pytest -m personal_account
pytest -m main_functional

# Линтер и типизатор
ruff check .
mypy .

# Автофикс линтера
ruff check --fix .

# Генерация Allure-отчёта
allure serve allure-results
```

## API-эндпоинты для тестов

Тестовые пользователи создаются через `POST /api/auth/register` (`data/api_client.py`):

| Метод | URL | Описание |
|-------|-----|----------|
| POST | `/api/auth/register` | Регистрация пользователя (email, password, name) |
| POST | `/api/auth/login` | Логин пользователя |
| DELETE | `/api/auth/user` | Удаление пользователя (по `Authorization`-заголовку) |

## Реализованные тест-кейсы (17 тестов × 2 браузера = 34)

### Восстановление пароля
- Переход на страницу восстановления по кнопке «Восстановить пароль»
- Ввод почты и клик по «Восстановить»
- Кнопка показать/скрыть пароль подсвечивает поле

### Личный кабинет
- Переход по клику на «Личный кабинет»
- Переход в раздел «История заказов»
- Выход из аккаунта

### Основной функционал
- Переход по клику на «Конструктор»
- Переход по клику на «Лента заказов»
- Клик по ингредиенту → модальное окно с деталями
- Закрытие модального окна крестиком
- Счётчик ингредиента увеличивается при drag-and-drop
- Залогиненный пользователь оформляет заказ

### Лента заказов
- Клик по заказу открывает модальное окно
- Заказы пользователя отображаются в ленте
- Счётчик «Выполнено за всё время» увеличивается
- Счётчик «Выполнено за сегодня» увеличивается
- Номер заказа появляется в «В работе»

## Паттерны и подходы

- **Page Object Model** — каждой странице соответствует класс в `pages/` и файл локаторов в `locators/`
- **Фикстуры pytest** — логин и создание заказа вынесены в `conftest.py`; регистрация через API
- **API-регистрация** — пользователи создаются через `POST /api/auth/register`, а не через UI
- **Headless-режим** — браузеры запускаются без GUI (Chrome `--headless=new`, Firefox `-headless`)
- **Explicit waits** — вместо `time.sleep` используются `WebDriverWait` и条件-based ожидания
- **Allure** — каждый тест и метод покрыты `@allure.step()`, `@allure.feature`, `@allure.story`
- **Faker** — тестовые данные генерируются динамически, без хардкода
- **AAA** — в каждом тесте чётко разделены Arrange / Act / Assert
- **DRY** — повторяющаяся логика (логин, оформление заказа) в фикстурах
- **Два браузера** — Chrome и Firefox запускаются через `pytest.mark.parametrize`
