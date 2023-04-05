import sqlite3


from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


con = sqlite3.connect('database.db')
cursor = con.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS trees (id INTEGER PRIMARY KEY, 
    tree_type TEXT, 
    age INTEGER, 
    health INTEGER, 
    size_x INTEGER, 
    size_y INTEGER)
    ''')
# Токен бота
token = "5922522563:AAG-4qUAunILTg1hzwDKstVK2893cdVwhBw"
HELP_COMMAND = """
/help - список команд
/start - приветствие
/trees - показать список деревьев"""

bot = Bot(token=token)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Button 1',
                           url="https://www.youtube.com/shorts/xdwymUwjjzY")
ib2 = InlineKeyboardButton(text='Button 2',
                           url="https://www.youtube.com/shorts/xdwymUwjjzY"
                           )
ikb.add(ib1, ib2)


@dp.message_handler(commands=['start'])
async def send_kb(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Приветствую тебя в нашем саду, выбирай действия с садом🌳',
                           reply_markup=ikb

                           )  # пишет смску

@dp.message_handler(commands=['trees'])
async def send_help(message: types.Message):
    await message.answer(text=HELP_COMMAND)



@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.answer(text=HELP_COMMAND)  # пишет смску


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply('Но такой команды нет>_<, (напиши /help для ознакомления с командами.)')  # пишет смску


if __name__ == "__main__":
    executor.start_polling(dp)
