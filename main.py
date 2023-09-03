
import discord
import os
import requests
import random
from dotenv import load_dotenv
from discord import app_commands
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name="gr", description="O comando envia aleatoriamente uma imagem de um gatinho ou de uma raposa para o canal de texto!")
async def gr_command(interaction:discord.Interaction):
    imagem_raposa = url_imagem_raposa()
    imagem_gato = url_imagem_gato()
    imagens = [imagem_gato, imagem_raposa]
    imagem_aleatoria_animais = random.choice(imagens)
    #embed = discord.Embed(
     ##  description="Imagens de gatinhos e raposas fofinhas"
    #)
    #embed.set_image(url=imagem_aleatoria_animais)
    await interaction.response.send_message(imagem_aleatoria_animais)

def url_imagem_gato():
    API_GATOS_URL = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(API_GATOS_URL)
    if response.status_code == 200:
        response_json = response.json()
        url_gato = response_json[0]['url']
        return url_gato

def url_imagem_raposa():
    API_RAPOSA_URL = "https://randomfox.ca/floof/"
    response = requests.get(API_RAPOSA_URL)
    if response.status_code == 200:
        response_json = response.json()
        url_raposa = response_json['image']
        return url_raposa
    
@client.event
async def on_ready():
    print(f'Bot está online como {client.user.name}')
    try:
        synced = await tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)
client.run(os.getenv("TOKEN_DISCORD"))
