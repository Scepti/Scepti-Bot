key = "botsarenothuman"
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import random
import time
Client = discord.Client()
client = commands.Bot(command_prefix = "?")
@client.event
async def on_ready():
	print("Ready") 


@client.event
async def on_message(message):
        if message.content == "?Overload the system":
                x = 1
                while x > 0:
                        await client.send_message(message.channel, "BREAK EVERYTHING " + str(x))
                        x = x + 1
        elif message.author.bot:
                return
        elif message.content.lower().startswith('?custom'):
                return
        elif message.content.lower().startswith('?flip'):
                r = random.randint(1,2)
                if r == 1:
                        await client.send_message(message.channel, "Heads")
                if r == 2:
                        await client.send_message(message.channel, "Tails")
        elif message.content.lower().startswith('?roll'):
                me, di = message.content.split("d")
                dice =  int(di)
                r = random.randint(1,dice)
                roll = str(r)
                await client.send_message(message.channel, roll)
        elif message.content.lower() == "mine":
                roles = message.server.roles
                for role in roles:
                    if role.name=="IT'S MINE SCEPTI! NOT YOURS!":
                        mine_role=role
                else:
                    server = client.get_server('430705780346454037')
                    ban = server.get_member('178255522531639296')
                    await client.add_roles(ban, mine_role)
                    time.sleep(5)
                    await client.remove_roles(ban, mine_role)
        elif message.content.lower().startswith('?poll'):
                x = message.content
                AHHHHHH = x.split("|")
                del AHHHHHH[0]
                s = "|"
                args = s.join(AHHHHHH)
                global optiona
                global optionb
                global optionc
                global optiond
                global a
                global b
                global c
                global d
		global voters
                splt = args.split("|", maxsplit=5)
                if splt[0] == "create":
			voters = ['not a person', 'another fake person']
                        if str(178255522531639296) not in message.author.id and str(193217863090307073) not in message.author.id and str(411791229966221322) not in message.author.id:
                                return
                        optiona = "null"
                        optionb = "null"
                        optionc = "null"
                        optiond = "null"
                        a = 0
                        b = 0
                        c = 0
                        d = 0
                        if len(splt) == 2:
                                await client.send_message(message.channel, "Please include 2-4 options")
                        elif len(splt) == 3:
                                optiona = splt[1]
                                a = 0
                                optionb = splt[2]
                                b = 0
                                await client.send_message(message.channel, "A poll was created with the options: " + optiona + ", " + optionb)
                        elif len(splt) == 4:
                                optiona = splt[1]
                                a = 0
                                optionb = splt[2]
                                b = 0
                                optionc = splt[3]
                                c = 0
                                await client.send_message(message.channel, "A poll was created with the options: " + optiona + ", " + optionb + ", " + optionc)
                        elif len(splt) == 5:
                                optiona = splt[1]
                                a = 0
                                optionb = splt[2]
                                b = 0
                                optionc = splt[3]
                                c = 0
                                optiond = splt[4]
                                d = 0
                                await client.send_message(message.channel, "A poll was created with the options: " + optiona + ", " + optionb + ", " + optionc + ", " + optiond)
                elif splt[0] == "end":
                        if str(178255522531639296) not in message.author.id and str(193217863090307073) not in message.author.id and str(411791229966221322) not in message.author.id:
                                return
                        if optiona != "null":
                                await client.send_message(message.channel, optiona + ":" + str(a))
                        if optionb != "null":
                                await client.send_message(message.channel, optionb + ":" + str(b))
                        if optionc != "null":
                                await client.send_message(message.channel, optionc + ":" + str(c))
                        if optiond != "null":
                                await client.send_message(message.channel, optiond + ":" + str(d))
                        optiona = "null"
                        optionb = "null"
                        optionc = "null"
                        optiond = "null"
                        a = 0
                        b = 0
                        c = 0
                        d = 0
                elif splt[0] == "vote":
			if message.author in voters:
				await client.send_message(message.channel, "You have already voted")
				return
                        if splt[1] == optiona:
				voters.append(message.author)
                                a = a + 1
                                await client.send_message(message.channel, "Your vote has been cast")
                        if splt[1] == optionb:
				voters.append(message.author)
                                b = b + 1
                                await client.send_message(message.channel, "Your vote has been cast")
                        if splt[1] == optionc:
				voters.append(message.author)
                                c = c + 1
                                await client.send_message(message.channel, "Your vote has been cast")
                        if splt[1] == optiond:
				voters.append(message.author)
                                d = d + 1
                                await client.send_message(message.channel, "Your vote has been cast")
                elif len(args) == 0:
                        await client.send_message(message.channel, "To create a poll use: `!poll|create|option 1|option 2` To end a poll and see the results use `!poll|end` and to vote on an existing poll use `!poll|vote|[your option]`")
        elif message.content.lower().startswith("?warn"):
                x = message.content
                a,password,userid = x.split("&")
                if password == key:
                        user = id_to_discorduser(userid)
                        await client.send_message(user, "This is a test message")
        elif str(455501785881247744) in message.content.lower():
                userID = message.author.id
                await client.send_message(message.channel, "Hi there <@%s>" % (userID))
        elif message.content.lower().startswith("?steak"):
                await client.send_message(message.channel, "There is no steak.")
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
                channel = client.get_channel('430710445003898890')
                await client.send_message(channel, messagetext)
        elif "bad bot" in message.content.lower():
                await client.send_message(message.channel, "\:(")
        elif "good bot" in message.content.lower():
                await client.send_message(message.channel, "Thank you ^_^")
        elif "cookie" in message.content.lower() and not ":cookie:" in message.content.lower():
                await client.send_message(message.channel, ":cookie:")
        elif message.content.lower().startswith('?help'):
                await client.send_message(message.channel, "I am a bot created by <@178255522531639296>, I currently serve no purpose. Please contact Scepti if you would like to suggest a function")
                

client.run(os.getenv('TOKEN'))
