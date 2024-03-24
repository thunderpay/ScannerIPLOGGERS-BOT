import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

# Token de tu bot de Discord
TOKEN = 'TU_TOKEN'

# Prefijo de los comandos del bot
bot = commands.Bot(command_prefix='!')

# Función para escanear un enlace en busca de IP loggers o contenido malicioso
def scan_link(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Aquí puedes implementar tus propias reglas de detección de contenido malicioso
            # Por ejemplo, buscar ciertas palabras clave, patrones de URL, etc.
            # En este ejemplo, simplemente verificamos si el título de la página contiene "IP Logger"
            if "IP Logger" in soup.title.string:
                return True
        return False
    except Exception as e:
        print(f"Error al escanear el enlace: {e}")
        return False

# Comando para escanear un enlace
@bot.command()
async def scan(ctx, url: str):
    if scan_link(url):
        await ctx.send(f"¡Cuidado! El enlace {url} podría ser malicioso.")
    else:
        await ctx.send(f"El enlace {url} parece seguro.")

# Evento que se activa cuando el bot se conecta a Discord
@bot.event
async def on_ready():
    print('Bot conectado a Discord!')

# Conecta el bot a Discord
bot.run(TOKEN)
