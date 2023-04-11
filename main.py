from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from decouple import config


TOKEN = config('TOKEN')
print(TOKEN)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=message.text)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)



