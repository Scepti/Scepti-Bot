import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
Client = discord.Client()
client = commands.Bot(command_prefix = "?")
@client.event
async def on_ready():
	print("Ready") 


@client.event
async def on_message(message):
    if message.content.lower().startswith("?balance"):
        x = message.content
        a,option1,amountbet1,option2,amountbet2,margin = x.split(" ")
        ab1 = int(amountbet1)
        ab2 = int(amountbet2)
        m = int(margin)/100
        o1 = int((1+(1-(ab1/(ab1+ab2))))*1000)/1000
        o2 = int((1+(1-(ab2/(ab2+ab1))))*1000)/1000
        oo1 = int((o1 - o1 * m) * 1000)/1000
        oo2 = int((o2 - o2 * m) * 1000)/1000
        overodds1 = str(oo1)
        overodds2 = str(oo2)
        odds1 = str(o1)
        odds2 = str(o2)
        await client.send_message(message.channel, "Fair Book:\n" + option1 + " odds: " + odds1 + "\n" + option2 + " odds: " + odds2)
        await client.send_message(message.channel, "Rigged Book:\n" + option1 + " odds: " + overodds1 + "\n" + option2 + " odds: " + overodds2)
    elif message.content.lower() == "bad bot":
        await client.send_message(message.channel, "\:(")
    elif message.content.lower() == "good bot":
        await client.send_message(message.channel, "Thank you ^_^")
    elif "cookie" in message.content.lower() and not ":cookie:" in message.content.lower():
        await client.send_message(message.channel, ":cookie:")
    elif message.content.lower().startswith('hi'):
        userID = message.author.id
        await client.send_message(message.channel, "Hi there <@%s>" % (userID))
    elif message.content.lower().startswith('?help'):
        await client.send_message(message.channel, "That command is not currently functional")
    elif message.content.lower().startswith('?'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> I don't understand that command" % (userID))
                

client.run(token)
