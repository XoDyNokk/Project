import telebot
import threading
import time
from datetime import datetime

TOKEN = "7775112720:AAFfBTwOWCZhHU1LdDQnQBo-3CPWv6O8e_I"
CHAT_ID = 7610703463

bot = telebot.TeleBot(TOKEN)

# === Твои ежедневные задачи ===
daily_tasks = [
    {"time": "07:30", "text": "🏃‍♂️ Время на пробежку! 30 минут — и день начнётся правильно!"},
    {"time": "08:30", "text": "📖 Прочитай 10 страниц — ум тоже требует тренировки."},
    {"time": "10:00", "text": "📚 Подготовка к ЕНТ: История Казахстана. Начни сейчас, станешь сильнее завтра."},
    {"time": "13:00", "text": "🧠 Подготовка к ЕНТ: Биология. Без знаний не будет результатов."},
    {"time": "14:30", "text": "🌿 Сделай 10-минутную прогулку. Мозгу нужен кислород."},
    {"time": "21:00", "text": "🌙 Подведение итогов: что сделал сегодня? Готовься ко сну, завтра — снова бой!"}
]

# === Мотивационные стили ===
motivations = {
    "жесткий": [
        "🔥 Никто за тебя ничего не сделает. Хочешь результата — работай как зверь!",
        "💢 Пока ты сидишь — кто-то качается, учится, работает. Он и займёт твоё место.",
        "⚔️ Либо ты рвёшься вперёд, либо остаёшься в стаде."
    ],
    "философский": [
        "🌀 Каждый день — это шанс стать лучше, чем ты был вчера.",
        "📿 Сильный не тот, кто не падает, а тот, кто встаёт каждый раз, когда упал.",
        "🧘‍♂️ Покой приходит тогда, когда ты знаешь: ты сделал всё, что мог."
    ],
    "смешной": [
        "🦷 Учи биологию, иначе твоя стоматология закончится жвачками в подъезде.",
        "🧠 Твоя голова не для прически — туда знания загружай!",
        "📚 Учёба — это не боль, это путь к деньгам (и к отпуску в 30 лет)."
    ],
    "лёгкий": [
        "🌟 Каждый шаг — шаг к победе. Даже если маленький.",
        "🚶‍♂️ Не стой. Иди. Просто иди.",
        "✨ Сегодня лучше, чем вчера — и этого уже достаточно."
    ]
}

def send_motivation():
    import random
    style = random.choice(list(motivations.keys()))
    text = random.choice(motivations[style])
    bot.send_message(CHAT_ID, f"🌟 Мотивация ({style}):\n\n{text}")

def check_schedule():
    sent = set()
    while True:
        now = datetime.now().strftime("%H:%M")
        for task in daily_tasks:
            if task["time"] == now and (now, task["text"]) not in sent:
                bot.send_message(CHAT_ID, task["text"])
                sent.add((now, task["text"]))
        if datetime.now().strftime("%H:%M") == "09:00":
            send_motivation()
        time.sleep(30)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Привет! Я твой бот-наставник. Буду напоминать и мотивировать тебя ежедневно!")

def run_bot():
    bot.polling(none_stop=True)

if __name__ == "__main__":
    t1 = threading.Thread(target=run_bot)
    t2 = threading.Thread(target=check_schedule)
    t1.start()
    t2.start()


