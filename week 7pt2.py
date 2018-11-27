from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('steve')
bot.set_trainer(ListTrainer)

while True:
    message = input()
    if message.strip() != 'bye':
        reply = bot.get_response(message)
        print(reply)
    if message.strip() == 'bye':
        print('bye!')
        break
    
