import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import random
Client = discord.Client()
client = commands.Bot(command_prefix = "?")
@client.event
async def on_ready():
	print("Ready") 


@client.event
async def on_message(message):
        if str(455501785881247744) in message.content.lower():
                userID = message.author.id
                await client.send_message(message.channel, "Hi there <@%s>" % (userID))
        elif message.content.lower().startswith("?bet"):
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
        elif message.content.lower().startswith('?say'):
                x = message.content
                a,messagetext = x.split("&")
                channel = client.get_channel('430705780346454039')
                await client.send_message(channel, messagetext)
        elif "bad bot" in message.content.lower():
                await client.send_message(message.channel, "\:(")
        elif "good bot" in message.content.lower():
                await client.send_message(message.channel, "Thank you ^_^")
        elif "cookie" in message.content.lower() and not ":cookie:" in message.content.lower():
                await client.send_message(message.channel, ":cookie:")
        elif message.content.lower().startswith('?help'):
                await client.send_message(message.channel, "I am a bot created by <@178255522531639296>, I currently serve no purpose. Please contact Scepti if you would like to suggest a function")
        elif message.content.lower().startswith('?reset time') and str(411791229966221322) in message.author.id:
                roles = message.server.roles
                for role in roles:
                        if role.name=='Nothing':
                                nothing_role=role
                for member in client.get_all_members():
                        if not any([role == nothing_role for role in member.roles]):
                                await client.add_roles(member, nothing_role)
                await client.send_message(message.channel, "The server is now unbalanced")
        elif message.content.lower().startswith('?snap') and str(411791229966221322) in message.author.id:
                roles = message.server.roles
                for role in roles:
                        if role.name=='Nothing':
                                nothing_role=role
                for member in client.get_all_members():
                        if any([role == nothing_role for role in member.roles]):
                                salvation = random.randint(1,2)
                                if salvation == 1:
                                        await client.remove_roles(member, nothing_role)
                await client.send_message(message.channel, "Balance is achieved")
        elif message.content.lower().startswith('?snap') and str(178255522531639296) in message.author.id:
                roles = message.server.roles
                for role in roles:
                        if role.name=='Nothing':
                                nothing_role=role
                for member in client.get_all_members():
                        if any([role == nothing_role for role in member.roles]):
                                salvation = random.randint(1,2)
                                if salvation == 1:
                                        await client.remove_roles(member, nothing_role)
                await client.send_message(message.channel, "Balance is achieved")
        elif message.content.lower().startswith('?reset time') and str(178255522531639296) in message.author.id:
                roles = message.server.roles
                for role in roles:
                        if role.name=='Nothing':
                                nothing_role=role
                for member in client.get_all_members():
                        if not any([role == nothing_role for role in member.roles]):
                                await client.add_roles(member, nothing_role)
                await client.send_message(message.channel, "The server is now unbalanced")
        elif message.content.lower().startswith('?'):
                userID = message.author.id
                await client.send_message(message.channel, "<@%s> I don't understand that command" % (userID))
                

client.run(token)
