import requests
from bs4 import BeautifulSoup
import time
import discord
from discord.ext import commands

# Configurações
url_login = 'URL_DO_LOGIN'
url_chamados = 'URL_DOS_CHAMADOS'
username = 'SEU_USUARIO'
password = 'SUA_SENHA'
discord_token = 'SEU_TOKEN_DO_BOT_DISCORD'
discord_channel_id = 'SEU_CANAL_ID'

def login():
    session = requests.Session()
    payload = {
        'username': username,
        'password': password
    }
    session.post(url_login, data=payload)
    return session

def verificar_chamados(session, chamados_antigos):
    response = session.get(url_chamados)
    soup = BeautifulSoup(response.content, 'html.parser')
    chamados = soup.find_all('div', class_='chamado')  # ajuste de acordo com a estrutura do site
    novos_chamados = [chamado for chamado in chamados if chamado not in chamados_antigos]
    return novos_chamados

async def enviar_notificacao(chamado, bot):
    canal = bot.get_channel(discord_channel_id)
    mensagem = f'Novo chamado: {chamado.text}'
    await canal.send(mensagem)

async def monitorar_chamados(bot):
    session = login()
    chamados_antigos = []
    
    while True:
        novos_chamados = verificar_chamados(session, chamados_antigos)
        if novos_chamados:
            for chamado in novos_chamados:
                await enviar_notificacao(chamado, bot)
            chamados_antigos.extend(novos_chamados)
        await asyncio.sleep(60)  # Verifica a cada 60 segundos
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logado como {bot.user}')
    await monitorar_chamados(bot)

bot.run(discord_token)
