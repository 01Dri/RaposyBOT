
import requests
import discord
import random

class gatos_rapoas:

    def url_imagem_gato(self):

        API_GATIS_URL = "https://api.thecatapi.com/v1/images/search"

        response = requests.get(API_GATIS_URL)

        if response.status_code == 200:

            response_json = response.json()
            url_gato = response_json[0]['url']

            return url_gato
        
    def url_imagem_raposa(self):
        API_RAPOSA_URL = "https://randomfox.ca/floof/"
        response = requests.get(API_RAPOSA_URL)
        if response.status_code == 200:

            response_json = response.json()
            url_raposa = response_json['image']

            return url_raposa
        


    async def comando_gato(self, message):

        imagem_raposa = self.url_imagem_raposa()
        imagem_gato = self.url_imagem_gato()

        imagens = [imagem_gato, imagem_raposa]
        imagem_aleatoria_animais = random.choice(imagens)

        embed = discord.Embed(
            title="Gatinhos e Raposas", description="Imagens de gatinhos e raposas fofinhas"
        )

        embed.set_image(url=imagem_aleatoria_animais)

        await message.reply(embed=embed)


