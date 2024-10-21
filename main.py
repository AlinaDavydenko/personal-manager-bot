import os
from dotenv import load_dotenv

import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from bot.keyboards import welcome_keyboard
from src.function_json_file import read_json, write_json
from src.utils import find_data_in_json
import pprint


# we get keys and settings from the file .env
load_dotenv()

BOT_API = os.getenv('BOT_TOKEN')  # authorization token for bot

bot = Bot(token=BOT_API)  # pass the bot token to the class
dp = Dispatcher()  # monitors incoming messages, analyzes them, is responsible for functionality

data = read_json()
pprint.pp(data)
data.update({'27.05.2025': {'23:59': 'идти спать'}})
pprint.pp(data)
write_json(data)


class Schedule(StatesGroup):
    date = State()
    calendar_date = State()
    language = State()


# Кнопки
@dp.message(Command('start'))
async def start_command(message: types.Message) -> None:
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=welcome_keyboard)
    await message.answer('Бот отвечает за твоё расписнание\n'
                         'Нажми кнопку ...', reply_markup=keyboard)


# Блок кода к кнопке Показать всё расписание
# Показать всё расписание
@dp.callback_query(F.data == "all_schedule")
async def about_me_callback(callback: types.CallbackQuery):
    all_my_schedule = read_json()
    await callback.message.answer(f'Вся информация по вашему расписанию:\n')
    for element in all_my_schedule:
        await callback.message.answer(f'{element}: {all_my_schedule[element]}')


# Обновить расписание
@dp.callback_query(F.data == "update_schedule")
async def about_me_callback(callback: types.CallbackQuery):
    await callback.message.answer('Здесь пока ничего нет')
# если расписание на дату уже есть, функция добавляет расписание к дате


# Блок кода для кнопки Поиск по дате
# Запрос даты у пользователя
@dp.callback_query(F.data == "find_data")
async def schedule(callback: types.CallbackQuery, state: FSMContext):
    """ функция запрашивает дату """
    await callback.message.answer('Введите дату')
    await state.set_state(Schedule.date)


# Поиск по дате
@dp.message(Schedule.date)
async def make_date(message: Message, state: FSMContext):
    """ функция выводит расписание на экран или просит составить расписание """
    print(message.model_dump_json(indent=4, exclude_none=True))
    key = message.text
    date_info = read_json()
    find_information = find_data_in_json(date_info, key)  # функция проверяет наличие ключа в файле
    if find_information != 0:
        for key, value in find_information.items():
            await message.answer(f'{key}: {value}')
    else:
        await message.answer('Список дел не найден\nВведите команду:\n\nСоставить расписание')


# Блок кода к кнопке Составить расписание
# Составить расписание
@dp.callback_query(F.data == "make_schedule")
async def about_me_callback(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Составьте своё расписание!\nВведите дату')
    await state.set_state(Schedule.calendar_date)


# Блок кода для вызова функции
async def main_bot() -> None:
    """ asking tg about new messages to the bot"""
    await dp.start_polling(bot)  # launches the bot into operation

asyncio.run(main_bot())




#TODO:
# сделать ввод числа и задачи
# словарь json, который будет обновляться
# из словаря можно вытащить значение
# данные заполняются в google



