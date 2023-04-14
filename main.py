import telebot
import weather

bot = telebot.TeleBot('5990736399:AAGEsp1ZvZVabyDJ9jELJLHBX2FQ3g1WzZg')


def parselocation(message):
    longitude = message.location.longitude
    latitude = message.location.latitude
    return str(longitude), str(latitude)


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Что сейчас с погодой?", request_location=True)
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я расскажу про погоду... (но мне нужны твои координаты)".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['location'])
def get_text_messages(message):
    location = parselocation(message)
    print(location)

    req = weather.getcurrentweather(location[0], location[1])
    bot.send_message(message.from_user.id, f"Cейчас {req}°C")


bot.polling(none_stop=True, interval=0)
