import os
import discord

client = discord.Client()
my_secret = os.environ['token']

@client.event
async def on_ready(): 
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    
    await message.channel.send('Hello!')

client.run(my_secret)

  