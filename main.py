import telebot

# импорт types для работы с кнопками
from telebot import types

from functions_for_database import print_free_table, booking_tables
# импорты для работы с файлом .env
from dotenv import load_dotenv
import os
from os.path import join, dirname


def get_from_env(key):
    """
    Получаем и загружаем токен телеграмбота из .env файла
    """
    dotenv_path = join(dirname(__file__), 'token.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)


token = get_from_env('TG_BOT_TOKEN')

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'hello'])  # обрабатывает базовые команды
def main(message):
    bot.send_message(message.chat.id,
                     f'Привет! {message.from_user.first_name},'
                     f' я Ваш виртуальный ассистент по резервированию столов в Ваших любимых заведениях')
    markup = types.InlineKeyboardMarkup()
    btn1_restaurant1 = types.InlineKeyboardButton('Макдональдс 🍔', callback_data='Макдональдс')
    btn2_restaurant2 = types.InlineKeyboardButton('KFC 🍗', callback_data='KFC')
    markup.row(btn1_restaurant1, btn2_restaurant2)
    bot.send_message(message.chat.id, f'Выберите заведение, в котором хотите забронировать столик', reply_markup=markup)


# функция обрабатывает нажатия на кнопки мак и кфс
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'Макдональдс':
        bot.send_message(callback.message.chat.id, 'Введите номер стола, который хотите забронировать')
        # Выводит таблицу свободных столов
        bot.send_message(callback.message.chat.id, print_free_table('table_McDonald', 'table_booking_McDonald'))
    elif callback == 'KFC':
        pass  # функция, которая выдает список столов kfc


@bot.message_handler(commands=['booking_table'])  # отдельная функция выбора заведения
def booking_table(message):
    markup = types.InlineKeyboardMarkup()  # создаются кнопки макдональдс и кфс
    btn1_restaurant1 = types.InlineKeyboardButton('Макдональдс 🍔', callback_data='Макдональдс')
    btn2_restaurant2 = types.InlineKeyboardButton('KFC 🍗', callback_data='KFC')
    markup.row(btn1_restaurant1, btn2_restaurant2)
    bot.send_message(message.chat.id,
                     f'Выберите заведение, в котором хотите забронировать столик', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def number_booking_table(message):
    """
    Функция проверяет, существует ли такой номер стола и запускает функцию booking_table
    :param message: принимает сообщение (номер стола, который вы хотите забронировать)
    """
    if message.text in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        booking_tables(message)
        bot.reply_to(message, f'Стол успешно забронирован')


if __name__ == '__main__':
    bot.polling(none_stop=True)  # функция делает так, чтобы бот работал постоянно


