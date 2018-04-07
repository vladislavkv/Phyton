import telebot

token = "Введите свой token"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def checkMessage(message):
    bot.send_message(message.chat.id, message.text[::-1])

bot.polling(none_stop=True)
