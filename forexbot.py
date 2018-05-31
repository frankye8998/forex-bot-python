import random
import os
import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import time
from random import randint
from forex_python.converter import CurrencyRates

###########

c = CurrencyRates()

emptylist = [''] * 32

currencies = ['IDR','BGN','ILS','GBP','DKK','CAD','JPY','HUF','RON','MYR','SEK','SGD','HKD','AUD','CHF','KRW','CNY','TRY','HRK','NZD','THB','EUR','NOK','RUB','INR','MXN','CZK','BRL','PLN','PHP','ZAR','USD']

############

debug = True

############

def RepresentsInt(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False


Client = discord.Client()
client = commands.Bot(command_prefix = "?")

@client.event
async def on_ready():
	print("Ready")
@client.event
async def on_message(message):
	if debug:
		print(message.content.split(" "))
		try:
			print(message.content.split(" ")[2][0:3])
			print(message.content.split(" ")[2][3:])
		except:
			pass
	if message.content.split(" ")[0] == '!buy' and RepresentsInt(message.content.split(" ")[1]) and message.content.split(" ")[2][0:3] in currencies and message.content.split(" ")[2][3:] in currencies:		
		print("Successed")
		tobuy = message.content.split(" ")[2][0:3].upper()
		tosell = message.content.split(" ")[2][3:].upper()
		tradeamount = message.content.split()[1]
		trade = round(c.convert(message.content.split(" ")[2][0:3], message.content.split(" ")[2][3:], float(message.content.split(" ")[1])),2)
		playerfile = './playerfiles/' +  message.author.id + '.txt'
		try:
			with open(playerfile, 'r') as file:
				money = file.readlines()
			if debug:
				print(playerfile + " exists!")
				print(money)
			money[currencies.index(tobuy)] = float(money[currencies.index(tobuy)]) + float(tradeamount)
			if debug:
				print(money)
		except IOError:
			with open(playerfile, 'w+') as file:
				file.writelines(emptylist)
				file.close()
			if debug:
				print("Created new file " + playerfile)
		fp.write(str(trade))
		if debug:
			print(trade)

	if message.content == "!exit" and message.author.id == '273608800823672833':
		await client.close()

client.run("")
