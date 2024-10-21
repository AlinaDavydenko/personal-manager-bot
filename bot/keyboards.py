from aiogram.types import InlineKeyboardButton
from bot.lexicon import ru

welcome_keyboard = [
        [InlineKeyboardButton(text=ru.get('update_schedule'), callback_data='update_schedule')],

        [
            InlineKeyboardButton(text=ru.get('to_make_schedule'), callback_data='make_schedule'),
            InlineKeyboardButton(text="Всё расписание", callback_data='all_schedule')
        ],
        [InlineKeyboardButton(text="Поиск по дате", callback_data='find_data')]
    ]
