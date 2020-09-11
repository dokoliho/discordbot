import discord
import os
from dotenv import load_dotenv


client = discord.Client()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print (f"Connected as {client.user.name}/{client.user.id}")

@client.event
async def on_message(message):

    # Keine Reaktion auf Nachrichten, die von uns selbst kommen
    if message.author == client.user:
        return

    # Protokollausgabe
    print(f"{message.author} wrote {message.content} on {message.channel}")

    # Antwort falls Schlüsselwort
    if message.content.startswith("?test"):
        await message.channel.send("Ok")

client.run(TOKEN)
