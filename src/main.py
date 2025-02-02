# src/main.py
import asyncio
import threading
import logging
from src.imei_checker.service import ImeiService
from src.telegram_bot.bot import TelegramImeiBot
from src.api.server import create_app
from src.config import TELEGRAM_BOT_TOKEN

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_api_server(imei_service: ImeiService, port: int = 5000):
    from waitress import serve  # Используем Waitress для production-окружения
    app = create_app(imei_service)
    logger.info(f"Запуск Flask API на порту {port}...")
    serve(app, host="0.0.0.0", port=port)


def main():
    # Инициализация сервиса проверки IMEI
    imei_service = ImeiService()

    # Запуск Flask API в отдельном потоке
    api_thread = threading.Thread(target=run_api_server, args=(imei_service,))
    api_thread.daemon = True  # завершается вместе с основным процессом
    api_thread.start()

    # Запуск Telegram-бота (aiogram)
    imei_bot = TelegramImeiBot(bot_token=TELEGRAM_BOT_TOKEN, imei_service=imei_service)
    logger.info("Запуск Telegram-бота (aiogram)...")
    asyncio.run(
        imei_bot.dispatcher.start_polling(imei_bot.bot, skip_updates=True)
    )


if __name__ == '__main__':
    main()

