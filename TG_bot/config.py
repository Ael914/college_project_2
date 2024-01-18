import telebot as tb
from telebot.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup
import funcs
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
bot = tb.TeleBot("")

start_markup = ReplyKeyboardMarkup(resize_keyboard=True)
start_markup.add(KeyboardButton("Предметы"))	
start_markup.add(KeyboardButton("Курсы"))	


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    with open(BASE_DIR/"media/rice.gif", "rb") as gif:
        bot.send_animation(message.chat.id, gif)
    bot.send_message(message.chat.id, """Приветствую тебя, тварь (божья)... \
Ты попал в мою казарму, и теперь ты будешь служить на рисовых полях всю свою жизнь. \
А чтобы ты не откинулся, я предлагаю тебе пройти мои курсы!
    """, reply_markup=start_markup)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    answer =  "Не положено тебе отвечать, плебеище"
    markup = ReplyKeyboardRemove()
    if message.text == "Предметы":
        data = funcs.get_subjects()
        answer = "\n".join(data[0])
        markup=data[1]
    elif message.text == "Курсы":
        data = funcs.get_courses()
        answer = "\n".join(data[0])
        markup=data[1]
    bot.reply_to(message, answer, reply_markup=markup)

bot.infinity_polling()