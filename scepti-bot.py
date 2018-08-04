#trip-wire.py
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

async def on_ready():
	print("Ready")


@client.event
async def on_message(message):
        if '455501785881247744' in message.author.id:
                await client.send_message(message.channel, "<@178255522531639296>") 
            
client.run("NDU1NTAxNzg1ODgxMjQ3NzQ0.DkaDkw.WRzAmvGw3ifhfGPB01TniFM9W6w")
