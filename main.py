import telebot
import weather
import credentials

bot = telebot.TeleBot(credentials.key())


def parselocation(message):
    longitude = message.location.longitude
    latitude = message.location.latitude
    return str(longitude), str(latitude)


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("What's going on the the street?", request_location=True)
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Hi, {0.first_name}! Let me take a look... (but i need your geopsoition)".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['location'])
def get_text_messages(message):
    location = parselocation(message)
    print(location)

    req = weather.getcurrentweather(location[0], location[1])
    bot.send_message(message.from_user.id, f"Now is {req}°C")


bot.polling(none_stop=True, interval=0)
