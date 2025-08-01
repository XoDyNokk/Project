import telebot
import threading
import time
import random
from datetime import datetime

# ТВОЙ ТОКЕН и CHAT_ID
TOKEN = "7775112720:AAFfBTwOWCZhHU1LdDQnQBo-3CPWv6O8e_I"
CHAT_ID = 7610703463

bot = telebot.TeleBot(TOKEN)

motivations = {
    "жёсткий": [
        "Вставай! Пока ты тупишь — другие забирают твою мечту.",
        "Не ноешь — побеждаешь. Всё просто.",
        "Ты либо станешь зверем, либо останешься овцой. Выбирай."
    ],
    "философский": [
        "Труд создает не тело, а характер. А характер ведёт к победе.",
        "Настоящая сила в терпении и выносливости.",
        "Боль — это просто урок. Проходи и иди дальше."
    ],
    "лёгкий": [
        "Ты красавчик, ты идешь вперёд. Продолжай!",
        "Каждый шаг — шаг к победе. Даже если маленький.",
        "Ты уже на пути. Не сдавайся сейчас."
    ]
}

# Расписание
schedule = {
    "07:30": "⏰ Подъём! Вперёд!",
    "07:40": "🏃‍♂️ Пробежка до 08:15",
    "08:15": "📘 Прочитай 10 страниц",
    "08:45": "🧠 История Казахстана (ЕНТ)",
    "10:30": "🧬 Биология (ЕНТ)",
    "12:30": "🍴 Обед и отдых",
    "14:00": "⚗️ Химия (ЕНТ)",
    "15:30": "📚 Грамотное чтение",
    "17:30": "🚶 Прогулка 10 минут",
    "18:00": "🥋 Таеквондо тренировка",
    "21:00": "📵 Телефон в сторону, отдыхай!",
}

# ПН/СР/ПТ утром — зал с 9 до 11
gym_days = ["Monday", "Wednesday", "Friday"]

def send_schedule():
    while True:
        now = datetime.now().strftime("%H:%M")
        weekday = datetime.now().strftime("%A")

        if weekday in gym_days and now == "09:00":
            bot.send_message(CHAT_ID, "🏋️ Зал: тренировка с 09:00 до 11:00")

        if now in schedule:
            bot.send_message(CHAT_ID, schedule[now])
        time.sleep(30)

def send_daily_motivation():
    while True:
        style = random.choice(list(motivations.keys()))
        message = random.choice(motivations[style])
        bot.send_message(CHAT_ID, f"🌟 Мотивация ({style}):\n\n{message}")
        time.sleep(60 * 60 * 4)  # Каждые 4 часа

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "👋 Привет! Я твой бот-наставник. Буду напоминать и мотивировать тебя ежедневно!")

threading.Thread(target=send_schedule).start()
threading.Thread(target=send_daily_motivation).start()

bot.polling()
