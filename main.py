
import discord
from api_gatos_raposas import gatos_rapoas
import os
from dotenv import load_dotenv
class MyClient(discord.Client):
     
    load_dotenv()
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    api_raposas_gatos = gatos_rapoas()
    @client.event
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    @client.event
    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.startswith("!gr"):
            await self.api_raposas_gatos.comando_gato(message)





intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(os.getenv("TOKEN_DISCORD"))
