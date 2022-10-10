import discord
from discord.ext import tasks, commands
import os
import asyncio
from msg import message
from channel import channel_id
from timer import hours,minutes,seconds
from creds import TOKEN
from keep_alive import keep_alive




intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)




@tasks.loop(seconds=seconds)
async def on_ready():
    print("ready")
    await client.wait_until_ready()
    user = client.get_channel(channel_id)
    await user.send(message)

  

async def main():
   # async with client:
    on_ready.start()
    await client.start(TOKEN)
keep_alive()
asyncio.run(main())
