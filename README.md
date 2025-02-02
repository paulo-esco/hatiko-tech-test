# IMEI Check Bot and API

Этот проект является тестовым заданием для позиции Python Junior и представляет собой систему для проверки IMEI устройств. Проект включает два основных компонента:

- **Telegram-бот** (на основе [aiogram](https://docs.aiogram.dev)):  
  Позволяет пользователям отправлять IMEI для проверки. Бот проверяет корректность номера (с использованием алгоритма Луна) и, если IMEI валиден, запрашивает информацию с внешнего API IMEIcheck. Доступ к функционалу бота разрешён только для пользователей из белого списка.

- **REST API** (на базе [Flask](https://flask.palletsprojects.com/)):  
  Предоставляет endpoint `/api/check-imei`, который принимает POST-запрос с JSON-телом, содержащим IMEI и внутренний токен авторизации. После проверки IMEI обращается к IMEIcheck API и возвращает JSON-ответ с информацией.

## Структура репозитория

```
my_imei_project/
├── README.md
├── requirements.txt
├── setup.py           # (опционально, для упаковки)
└── src/
    ├── .env
    ├── config.py         # Конфигурация (токены, API-ключи, настройки)
    ├── imei_checker/
    │   ├── validator.py  # Логика валидации IMEI (проверка длины, цифры, алгоритм Луна)
    │   └── service.py    # Обращение к внешнему API IMEIcheck с использованием Bearer-аутентификации
    ├── telegram_bot/
    │   └── bot.py        # Реализация Telegram-бота с использованием aiogram
    ├── api/
    │   └── server.py     # Flask API для проверки IMEI
    └── main.py           # Точка входа, которая запускает Telegram-бота и REST API
```

## Установка

1. **Клонируйте репозиторий с GitHub:**

   ```bash
   git clone https://github.com/paulo-esco/hatiko-tech-test.git
   cd hatiko-tech-test
   ```

2. **Создайте и активируйте виртуальное окружение:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # На Windows: venv\Scripts\activate
   ```

3. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

## Конфигурация

Настройте необходимые параметры в файлах `.env` и `src/config.py`:

- **Telegram Bot:**
  - `TELEGRAM_BOT_TOKEN`: токен вашего Telegram-бота, полученный через BotFather.
  - `ALLOWED_TELEGRAM_USERS`: множество chat_id пользователей, которым разрешён доступ к функционалу.

- **Внутренний API:**
  - `API_AUTH_TOKEN`: токен для авторизации запросов к REST API.

- **IMEIcheck API:**
  - `IMEI_API_URL`: базовый URL для обращения к API (по умолчанию `https://api.imeicheck.net`).
  - `IMEI_API_TOKEN`: API-ключ для IMEIcheck (используется Bearer-аутентификация).

## Использование

### Запуск проекта

Запустить проект можно одной командой, которая запустит как Telegram-бота, так и REST API:

```bash
python src/main.py
```

- **Telegram-бот:**
  - Бот начнёт опрос обновлений (polling).
  - Авторизованные пользователи могут отправлять сообщения с IMEI, после чего бот проверит их корректность и вернёт информацию, полученную с IMEIcheck API.

- **REST API:**
  - API будет доступен по адресу `http://localhost:5000/api/check-imei`.
  - Для проверки IMEI необходимо отправить POST-запрос с JSON-телом:

    ```json
    {
      "imei": "123456789012345",
      "token": "MY_SECRET_API_TOKEN"
    }
    ```

### Пример запроса cURL

```bash
curl -X POST http://localhost:5000/api/check-imei \
     -H "Content-Type: application/json" \
     -d '{"imei": "123456789012345", "token": "MY_SECRET_API_TOKEN"}'
```

## Лицензия

Этот проект предоставляется "как есть" для тестовых целей. При желании модифицируйте и расширяйте его в соответствии с вашими потребностями.

## Автор

*Рублев Павел Дмитриевич*  
*Email: p1avel07@mail.ru*
