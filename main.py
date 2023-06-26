from telegram import TelegramBot
from config import settings

bot_token = settings.BOT_TOKEN
bot = TelegramBot(bot_token)

def buton(chat_id):
    button1 = bot.inlinekeyboardbutton('Button 1', 'data1')
    button2 = bot.inlinekeyboardbutton('Button 2', 'data2')
    button3 = bot.inlinekeyboardbutton('Button 3', 'data3')
    keyboard = bot.inlinekeyboardmarkup([[button1], [button2], [button3]])
    text = 'MENU'
    bot.send_message(chat_id, text, reply_markup=keyboard)

def print_received_message(chat_id, message, query):
    if query:
        print(f"Received message from {chat_id}: {query}")
        
    if message == "/start":
        bot.send_message(chat_id, text = "Bota hoşgeldiniz.")
        
    if message == "/menu":
        buton(chat_id)

    if message:
        print(f"Received message from {chat_id}: {message}")

while True:
    updates = bot.get_updates()
    if updates:
        bot.handle_updates(updates, print_callback=print_received_message)