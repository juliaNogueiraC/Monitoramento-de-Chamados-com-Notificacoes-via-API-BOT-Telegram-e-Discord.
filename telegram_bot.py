import requests
from bs4 import BeautifulSoup
import time
from telegram import Bot

# Configurações
url_login = 'URL_DO_LOGIN'
url_chamados = 'URL_DOS_CHAMADOS'
username = 'SEU_USUARIO'
password = 'SUA_SENHA'
telegram_token = 'SEU_TOKEN_DO_BOT_TELEGRAM'
telegram_chat_id = 'SEU_CHAT_ID'

# Função para fazer login no site
def login():
    session = requests.Session()
    payload = {
        'username': username,
        'password': password
    }
    session.post(url_login, data=payload)
    return session

# Função para verificar novos chamados
def verificar_chamados(session, chamados_antigos):
    response = session.get(url_chamados)
    soup = BeautifulSoup(response.content, 'html.parser')
    chamados = soup.find_all('div', class_='chamado')  # ajuste de acordo com a estrutura do site
    novos_chamados = [chamado for chamado in chamados if chamado not in chamados_antigos]
    return novos_chamados

# Função para enviar notificações via Telegram
def enviar_notificacao(chamado):
    bot = Bot(token=telegram_token)
    mensagem = f'Novo chamado: {chamado.text}'
    bot.send_message(chat_id=telegram_chat_id, text=mensagem)

# Função principal
def monitorar_chamados():
    session = login()
    chamados_antigos = []
    
    while True:
        novos_chamados = verificar_chamados(session, chamados_antigos)
        if novos_chamados:
            for chamado in novos_chamados:
                enviar_notificacao(chamado)
            chamados_antigos.extend(novos_chamados)
        time.sleep(60)  # Verifica a cada 60 segundos

if _name_ == "__main__":
    monitorar_chamados()
