# i must admit that I literally copied this code from the previous repository, and modified it (named "CreateAPrefixCommandBot")

import discord # importing the Discord library, use "pip install discord" or "conda install discord" to install it
from discord.ext import commands

intents = discord.Intents.default() # setting the intents the bot will be able to use, check it in the Discord Developers Portal so that the bot can send messages, etc.
intents.message_content = True # allowing the bot to send messages

bot = commands.Bot(
  command_prefix="?", # the "command_prefix" parameter is the prefix of our commands
  intents=intents # assign intents to the bot
) # creating a bot instance, it is responsible for the application

@bot.event # decorator "@bot.event" allows you to listen for events
async def on_ready(): # we use an asynchronous "on_ready" function, it is executed when the bot is ready
   print("bot is ready") # sending a log, you can do anything else here, but if you want to do something related to the Discord API, use "await" before the command

@bot.command(name="avatar") # creating a command called "avatar", it will be called like this: "?avatar"
async def pingCommand(ctx: commands.Context, member: discord.Member = None): # for the explanation of "commands.Context" check the documentation discord.py, or go to my repository called "CreateAPrefixCommandBot"
   # object "discord.Member" is an instance that accepts a user's mention or ID. We give "= None" here to make this argument optional.
   if member: # checking if the user has given the user
      await ctx.send(f"{member.avatar}") # sending a URL (or a photo, depending on Discord and the server) of the user's avatar, but the bot will probably just send the photo.
   else:
      await ctx.send(f"{ctx.author.avatar}") # object "ctx.author" refers to the caller of the command, and object "avatar" returns the URL of the avatar. In this case, the bot sends the author's avatar.
   # after executing the "?avatar @user" command, the bot responds with avatar of user, if it has "message_content" intentions assigned.

@bot.run("token") # replace the "token" with your token from the "Bot" tab in the Discord Developers Portal, and give it here (as a string), remember not to share it with ANYONE
