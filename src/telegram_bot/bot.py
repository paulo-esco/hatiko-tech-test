import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage

from src.config import TELEGRAM_BOT_TOKEN, ALLOWED_TELEGRAM_USERS
from src.imei_checker.validator import ImeiValidator
from src.imei_checker.service import ImeiService

logger = logging.getLogger(__name__)


class TelegramImeiBot:
    def __init__(self, bot_token: str, imei_service: ImeiService):
        self.bot = Bot(token=bot_token)
        self.dispatcher = Dispatcher(storage=MemoryStorage())
        self.imei_service = imei_service
        self.register_handlers()

    def register_handlers(self):
        @self.dispatcher.message(CommandStart())
        async def start(message: types.Message):
            await message.answer("Привет! Отправь мне IMEI для проверки.")

        @self.dispatcher.message()
        async def handle_message(message: types.Message):
            user_id = message.from_user.id

            if user_id not in ALLOWED_TELEGRAM_USERS:
                await message.answer("Доступ запрещён.")
                return

            imei_input = message.text.strip()
            if not ImeiValidator.is_valid(imei_input):
                await message.answer("Неверный формат IMEI или не проходит контрольная сумма.")
                return

            await message.answer("Проверяем IMEI, подождите...")

            loop = asyncio.get_running_loop()
            info = await loop.run_in_executor(None, self.imei_service.get_info, imei_input)
            await message.answer(f"Информация по IMEI:\n{info}")
