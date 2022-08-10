from fileinput import close
from imp import SEARCH_ERROR
from urllib.parse import uses_query
import discord
import os 
from translate import translate
from search import search


#import dotenv to get the token for the bot.
from dotenv import load_dotenv

load_dotenv('./token.env')
# Grab the API token from the .env file.
token = os.getenv('discord_Token')


#get the client information from discord package

bot = discord.Client()



#Event listener

@bot.event

async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
userString = ""

@bot.event

async def on_message(message):
    
	#check if the user enters the call that wakes the bot
	if message.content == "!yo":
		# send the following thing back to the user
		await message.channel.send("Wassup, what do you wanna do? type !info to find out how I can help you!")
  
	if message.content.startswith("!info"):
		await message.channel.send(" | I can translate a sentence you can't understand with !translate - example: --- !translate  english \"आपका नाम क्या है\" --- returns the sentence in english \n | I can search the web with !find \n | or just say !yo")
 
	if message.content.startswith("!translate"):
		global userString
		userString = message.content
		userString = userString[11:]
		try: await message.channel.send(translate(userString))

		except IndexError as e: 
			await message.channel.send("Please add the text to be translated in quotes")
	
		#"In English this is: " + translate(userString) +
	
	
	if message.content.startswith( "!find" ):
		
		global userQuery
		userQuery = message.content
		userQuery = userQuery[5:]
		
		index = 0;
		limit = 5;
		
		for index, links in search(userQuery):
			await message.channel.send(links)
			if index == limit:
				break

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. 
bot.run(token)