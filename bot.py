import telebot
import random


bot = telebot.TeleBot('1691834307:AAHhePEkTOE9nEboafg-iUpTdVm5fX9QFvQ')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, random.choice(['Мал базар']))

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower():
        a = [
            'Гармон жун', 'Алипекарь', 'Боботик, чтоб не болел животик', 
            'Кашат мал', 'Кудивер шланг', 'Семен алкаш', 'Жумадрыщь', 'Атайчик-зайчик',
            'Рыся-перзидент', 'Жози-ит', 'Азат-тоок', 'Нура-крокодайл', 'Пекчо-последний',
            'Тети-транс', 'Тока-бандит-95', 'Дава-нигер', 'Чика-канчика', 'Мофоня чайнавачы',
            'Вася-пидор',
            ]
        bot.send_message(message.chat.id, random.choice(a))

bot.polling(none_stop=True)