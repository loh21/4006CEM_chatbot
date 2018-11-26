from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import discord
from discord.ext import commands
import requests


client = commands.Bot(command_prefix = '.')
token = 'NTExMjYwNDQxNjE2NDQ5NTY3.DsokJQ.cwJiliEciMG8A4juIQBZrdjh0OA'

@client.event
async def on_ready():
    print('The bot is ready!')
    await client.change_presence(game=discord.Game(name='bot'))

@client.command()
async def weather(city):
    embed = discord.Embed(title = 'Weather', colour = discord.Colour.blue())
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=1ee311d03b2c63e7fdab818a30c8624e&units=metric'.format(city)

    req = requests.get(url)
    data = req.json()

    temp = data['main']['temp']
    mini = data['main']['temp_min']
    maxi = data['main']['temp_max']
    humid = data['main']['humidity']
    speed = data['wind']['speed']
    cloud = data['clouds']['all']
    desc = data['weather'][0]['description']
    
    embed.add_field(name = 'Temperature(°C) ', value = temp)
    embed.add_field(name = 'Min Temperature(°C) ', value = mini)
    embed.add_field(name = 'Max Temperature(°C) ', value = maxi)
    embed.add_field(name = 'Humidity(%) ', value = humid)
    embed.add_field(name = 'Wind Speed(mph) ', value = speed)
    embed.add_field(name = 'Average Cloud Cover(%) ', value = cloud)
    embed.add_field(name = 'Short Description ', value = desc)
    embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/506220495318941736/515923771413102602/images.png')

    await client.say(embed = embed) ##originally just use await.client.say for each line
    
bot = ChatBot('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {   'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.70,
            'default_response': 'I am sorry, but I do not understand.'
        }])

bot.set_trainer(ListTrainer)

@client.event
async def on_message(message):
    if message.author == client.user: ## stops bot replying to itself
        return
    while True:
        if message.content[0] == '.': ## breaks while loop if it is a command
            break
        if message.content.strip() != ('bye'):
            reply = bot.get_response(message.content)
            await client.send_message(message.channel, reply)
            print(reply)
            break
        if message.content.strip() == 'bye':
            await client.send_message(message.channel, 'bye!')
            break
    await client.process_commands(message)


        
client.run(token)
