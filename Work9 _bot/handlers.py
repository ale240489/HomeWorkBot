from aiogram import types
from create import dp
import random as rnd
total_candie = 100


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'{message.from_user.first_name} привет тебе!!!  Этот бот для игры в кофеты! Давай играть!'
                         f'Набери /help для подробностей')

@dp.message_handler(commands=['set'])
async def mes_start(message: types.Message):
    global total_candie
    count = message.text.split()[1]
    total_candie = int(count)
    await message.answer(f'Стартовое количество конфет: {total_candie}')

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Через команду "/set_количество конфет" задается стартовое'
                         'количество конфет. Дальше мы с тобой поочереди забираем из кучки конфеты(но не более 28 за раз!!!!)'
                         'Выигрывает тот, кто забирает последним!!! Поехали!!!'
                         'для того что бы забрать конфеты введи число равное количеству конфет, которые ты хочешь '
                         'забрать!')

@dp.message_handler()
async def mes_help(message: types.Message):
    global total_candie
    bot_candies = rnd.randint(0, 28)
    if message.text.isdigit():
        if int(message.text) <= 28:
            total_candie -= int(message.text)
            await message.answer(f'Ты забрал {message.text} конфет, осталось {total_candie} конфет.')
            if total_candie == 0:
                await message.answer(f'Ты выиграл! Что бы сыграть еще, задай заново стартовое количество конфет!')
            else:
                if total_candie > 56:
                    total_candie -= bot_candies
                    await message.answer(f'Я забрал {bot_candies} конфет, осталось {total_candie} конфет.')
                elif total_candie <=56 and total_candie > 28:
                    bot_candies = (29 - total_candie) * (-1)
                    total_candie -= bot_candies
                    await message.answer(f'Я забрал {bot_candies} конфет, осталось {total_candie} конфет.')
                elif total_candie <= 28:
                    bot_candies = total_candie
                    total_candie -= bot_candies
                    await message.answer(f'Я забрал {bot_candies} конфет, осталось {total_candie} конфет,'
                                         f'Я победил!!!')
                elif total_candie == 29:
                    bot_candies = 1
                    total_candie -= bot_candies
                    await message.answer(f'Я забрал {bot_candies} конфет, осталось {total_candie} конфет.')
        else:
            await message.answer('Количество не должно быть больше 28!')


