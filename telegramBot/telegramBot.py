import telebot

token = "null"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def check_message(message):
    personInfo ={
                  'виктор':['+7(***)***9052', 'Ул. 1'],
                  'рахат':['+7(***)****1265', 'Ул. 2'],
                  'максим':['+7(***)***7542', 'Ул. 3'],
                  'олег':['+7(***)***2374', 'Ул. 4']
                }
    
    personName = message.text.lower()

    if personName in personInfo:
        bot.send_message(message.chat.id, personInfo[personName])
        bot.send_message(message.chat.id, personInfo[personName][1])
    else:
        bot.send_message(message.chat.id, 'Ошибка! Такого имени не найдено')

bot.polling(none_stop=True)
