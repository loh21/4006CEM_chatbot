from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('steve')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/Users/Alan\AppData/Local/Programs/Python/Python36/Lib/site-packages/chatterbot_corpus/data/english/'):
    data = open('C:/Users/Alan\AppData/Local/Programs/Python/Python36/Lib/site-packages/chatterbot_corpus/data/english/' + files ,'r').readlines()
    bot.train(data)

while True:
    message = input()
    if message.strip() != 'bye':
        reply = bot.get_response(message)
        print(reply)
    if message.strip() == 'bye':
        print('bye!')
        break
    
