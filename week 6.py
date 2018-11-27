import discord

client = discord.Client()
token = 'NTExMjYwNDQxNjE2NDQ5NTY3.DsokJQ.cwJiliEciMG8A4juIQBZrdjh0OA'

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(game=discord.Game(name="test"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower() == ["when is your birthday?"]:
        await client.send_message(message.channel, "i dont have a birthday")
    if message.content.lower() == "when do you use an umbrella?":
        await client.send_message(message.channel, "while it is raining")
    else:
        await client.send_message(message.channel, "i don't understand")
        
client.run(token)
