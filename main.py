import discord
import random
import asyncio

# Import config data
import config
import interpretation.check as check


client = discord.Client()


# Whenever a message is sent.
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    temp_msg = []

    welcome_channel = client.get_channel(config.welcome_channel)

    isAdmin = False
    if message.guild == welcome_channel.guild:
        if config.administrator in [y.id for y in message.channel.guild.get_member(message.author.id).roles]:
            isAdmin = True

    # Type your commands here
    #
    #
    #

    # Delete all temporary messages after "five" seconds.
    await asyncio.sleep(120)
    for msg in temp_msg:
        await msg.delete()


# Whenever the bot regains his connection with the Discord API.
@client.event
async def on_ready():
    print(' --> Logged in as')
    print('   | > ' + client.user.name)
    print('   | > ' + str(client.user.id))
    await client.get_channel(config.welcome_channel).send('Beep boop! I just went online!')

try:
    client.run(config.TOKEN)
except:
    print('   | > Error logging in. Check your token is valid and you are connected to the Internet.')
