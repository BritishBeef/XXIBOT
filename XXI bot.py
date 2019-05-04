import youtube_dl
import discord
import traceback
import sys
import random
import asyncio
import aiohttp
import json
from discord.ext import commands
import discord
import discord.ext

TOKEN = 'NTAxMzEzNjA5ODMwMjM2MTY2.DqXkgg.g5Sjzqlnm_zMaCCuRS0v5Wx7gp4'
newUserDMMessage = "```Welcome to the Twenty-First Predator Legion discord! If you haven't already been instructed to do so, please go to the contract channel and fill out the google form. Then, proceed to the verification channel and do !verify, and follow the prompts provided by the bot.```"
description = "XXI BOT"


bot = commands.Bot(command_prefix='!', description=description)
bot.remove_command('help')


# EVENTS

@bot.event
async def on_ready():
	print('Logged in as: '+bot.user.name)
	print('Bot ID: '+bot.user.id)
	for server in bot.servers:
		print ("Connected to server: {}".format(server))
	print('------')

@bot.event
async def on_resumed():
    print('reconnected')

@bot.event
async def on_member_remove(member):
    channel = member.server.get_channel("422885628473114646")
    fmt = '{0.mention} has left/been kicked from the server.'
    await bot.send_message(channel, fmt.format(member, member.server))

@bot.event
async def on_member_join(member):
    print("Recognized that " + member.name + " joined")
    await bot.send_message(member, newUserDMMessage)
    print("Sent message to " + member.name)
    print("Sent message about " + member.name + " to #CHANNEL")





# HELP COMMAND


@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        color = discord.Colour.orange()
    )

    embed.set_author(name="Help")
    embed.add_field(name="List Of Commands", value= """```

!announce ➜ simply type the command then specify the role to announce to and then the message you want to announce.

!trello ➜ this command will provide you with a link to the current XXI trello.

!creator  ➜ this command will state the creator of the bot.

!castra  ➜ this command will provide you with a link to the current XXI castra.

```

""", inline=False)
    await bot.send_message(author, embed=embed)
    await bot.say(ctx.message.author.mention+", **check your DMs!**" )



# COMMANDS


@bot.command()
async def ping():
    await bot.say("Pong!")

@bot.command(pass_context=True)
@commands.has_role('Announcement Permission')
async def announce(ctx, role: discord.Role, *, message):
    for member in ctx.message.server.members:
        if role in member.roles:
            try:
                await bot.send_message(member, message)
                await bot.process_commands(message)
            except Exception:
                pass

@bot.command(pass_context=True)
@commands.has_role('Announcement Permission')
async def announce2(ctx, role: discord.Role, *, message):
    embed = discord.Embed(
    color = discord.Colour.orange()
    )

    embed.set_author(name="XXI")
    embed.add_field(name="Announcement", value= "```" + message + "```", inline=True)
    
    for member in ctx.message.server.members:
        if role in member.roles:
            try:
                await bot.send_message(member, embed=embed) 
                await bot.process_commands(message)
            except discord.Forbidden:
                print ("")
                print ("Blocked Bot: %s", member.nick)
                a = open('Blocked Bot.txt', 'w')
                a.write("Blocked Bot: " + member.nick)
                a.close()
            except Exception:
                pass

@bot.command(pass_context=True)
async def creator(ctx):
    await bot.say(ctx.message.author.mention+", **This bot was made by R3KT2DAY!**" )


@bot.command(pass_context=True)
async def castra(ctx):
    await bot.say(ctx.message.author.mention+", https://www.roblox.com/games/2277719353/RAPAX-Castra-Vetera" )

@bot.command(pass_context=True)
async def trello(ctx):
    await bot.say(ctx.message.author.mention+", https://trello.com/b/gXwiyXJp/twenty-first-predator-legion" )


# ERROR HANDLER



    @bot.event
    async def on_command_error(ctx, error):
        """The event triggered when an error is raised while invoking a command.
        ctx   : Context
        error : Exception"""

        if hasattr(ctx.command, 'on_error'):
            return
        
        ignored = (commands.CommandNotFound, commands.UserInputError)
        error = getattr(error, 'original', error)
        
        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.DisabledCommand):
            return await ctx.send(f'{ctx.command} has been disabled.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except:
                pass

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
                return await ctx.send('I could not find that member. Please try again.')
            
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
    
    @commands.command(name='repeat', aliases=['mimic', 'copy'])
    async def do_repeat(self, ctx, *, inp: str):
        await ctx.send(inp)

    @do_repeat.error
    async def do_repeat_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'inp':
                await ctx.send("You forgot to give me input to repeat!")      

    






# RUN TOKEN

bot.run(TOKEN, bot=True, reconnect=True)
