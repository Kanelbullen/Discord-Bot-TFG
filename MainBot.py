from itertools import cycle
import discord
from discord.ext import tasks, commands
import random
from phue import Bridge
import json
import time
import os
import webbrowser

TOKEN = 'ODQzMTIwMTE5Mjg2OTg4ODIw.YJ_OzA.EEpIrdR23KOqc-VRXGNRLnxovIg'
client = discord.Client()
os.chdir(r'C:\Users\twota\PycharmProjects\lamps')

@client.event
async def on_ready():
    change_status.start()
    print("We have logged in as {0.user}".format(client))

bridge = Bridge("Light here")
bridge.connect()

lights = bridge.get_light_objects('name')

def lights_random():
    lights["Anton"].on = True
    lights["Anton"].hue = random.randrange(50000)
    lights["Anton"].sat = random.randrange(200)
    lights["Anton1"].on = True
    lights["Anton1"].hue = random.randrange(50000)
    lights["Anton1"].sat = random.randrange(200)

def lights_off():
    lights["Anton"].on = False
    lights["Anton1"].on = False

def lights_on():
    lights["Anton"].on = True
    lights["Anton1"].on = True

#commandlist
commandlist = (' hello/bye - will say it back to you \n '
               '!random - gives random number between 1 and 1000\n '
               '!random_light- gives a random color on lights\n '
               '!rick - will start rickroll\n '
               '!lights_off - turns off all lights\n '
               '!lights_on - will turn on lights\n '
               '!fap_time - will open pornhub\n ')

#status
status = cycle(['Free', 'min', 'sihan', 'han', 'menade', 'inte', 'att', 'döda', 'barnet'])

@tasks.loop(seconds=2)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
    return

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'tf-gang':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'good bye faggot')
            return
        elif user_message.lower() == '!random':
            response = f'Random number: {random.randrange(1000)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == '!p':
            await message.channel.send(f'This shit coming soon')
            return
        elif user_message.lower() == '!s':
            await message.channel.send(f'Nah bro im to sceard he is a big dude')
            return
        elif user_message.lower() == '!random_light':
            lights_random()
            await message.channel.send(f'You just put a random color in antons rum nice')
            return
        elif user_message.lower() == '!lights_off':
            lights_off()
            await message.channel.send(f'Lights are now off you faggot')
            return
        elif user_message.lower() == '!lights_on':
            lights_on()
            await message.channel.send(f'Lights are now on you faggot')
            return
        elif user_message.lower() == '!rick':
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO')
            await message.channel.send(f'{username} you did him dirty on that one')
            return
        elif user_message.lower() == '!fap_time':
            webbrowser.open('https//:pornhub.com')
            await message.channel.send(f' {username} is going BRB for a while hehe:)')
            return
        elif user_message.lower() == '!command':
            await message.channel.send(f'{username} bro you bad at those commands')
            await message.channel.send(commandlist)
            return
        elif user_message.lower() == '!mayonäs':
            webbrowser.open('https://www.youtube.com/watch?v=zo4OzT7wbb0')
            return
        elif user_message.lower() == "!time":
            await message.channel.send(f'')

client.run(TOKEN)
