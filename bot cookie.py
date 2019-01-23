import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import logging

Client = discord.Client()
client = commands.Bot (command_prefix = "!")

chat_filter = ["KANKER", "KUT", "KK", "KKR", "TYFUS", "TERING"]
bypass_list = [] 





@client.event
async def on_message(message):
    if message.content.upper().startswith('!HELP'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Hallo! als eerst bedankt dat je mijn bot wil gebruiken en daarom hier een paar commands die je kan gebruiken: ``!say [iets wat je de bot wil laten zeggen]`` ``!koekje [dan stuurt de bot je een koekje :)]````!benikadmin kijk of je dezelfde rechten als een admin hebt.``" % (userID))
    if message.content.upper().startswith('!SAY'):
        if "535116112606527498" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "Je hebt hier geen rechten voor, sorrie!")
    if message.content.upper().startswith('!BENIKADMIN'):
        if "535116112606527498" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, "Jazeker! :D")
        else:
            await client.send_message(message.channel, "Nee, sorrie D:")
    if message.content == "!koekje":
         await client.send_message(message.channel, "Hier heb je je koekje :cookie:")
    contents = message.content.split(" ") #contents is a list
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                await client.delete_message(message)
                await client.send_message(message.channel, "**ho, ho, doe a.u.b. een beetje rustig**")
         
@client.event
async def on_ready():
    print ("je bot staat aan!!!!")        

client.run(os.getenv('TOKEN'))
