# Monitoramento de Chamados com Notificações via API BOT do Telegram e Discord.

Este projeto é um script Python que monitora chamados de um sistema de suporte de TI e envia notificações via Telegram ou Discord quando novos chamados são detectados.
São dois scripts, um para Telegram e outro para Discord. A escolha da aplicação fica a critério do usuário. 

# VIA TELEGRAM
## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `requests`
  - `beautifulsoup4`
  - `python-telegram-bot`

Você pode instalar as bibliotecas necessárias com o seguinte comando:
```
pip install requests beautifulsoup4 python-telegram-bot
```
## Configuração
- Clone este repositório ou copie os arquivos para o seu ambiente local.
Atualize as configurações no script com suas credenciais e informações específicas:
  - url_login: URL da página de login do seu sistema de chamados.
  - url_chamados: URL da página de chamados.
  - username: Seu nome de usuário.
  - password: Sua senha.
  - telegram_token: Token do seu bot no Telegram.
  - telegram_chat_id: ID do chat onde você quer receber as notificações.
  
## Uso
Crie um bot no Telegram e obtenha o token. Adicione o bot ao seu chat e obtenha o chat_id.
Execute o script `telegram_bot.py`.

## Estrutura do Código
- Importações e Configurações: Importa as bibliotecas necessárias e define as configurações.
- Função de Login: Faz login no site e retorna uma sessão autenticada.
- Função para Verificar Chamados: Verifica novos chamados na página e retorna uma lista de novos chamados.
- Função para Enviar Notificações via Telegram: Envia uma notificação para o chat do Telegram.
- Função Principal: Monitora os chamados continuamente e envia notificações quando novos chamados são detectados.


# VIA DICORD

## Requisitos
- Python 3.x
- Bibliotecas Python:
  - `requests`
  - `beautifulsoup4`
  - `discord.py`

Você pode instalar as bibliotecas necessárias com o seguinte comando:
```
pip install requests beautifulsoup4 discord.py
````

## Configuração
- Clone este repositório ou copie os arquivos para o seu ambiente local.
- Atualize as configurações no script com suas credenciais e informações específicas:
  - url_login: URL da página de login do seu sistema de chamados.
  - url_chamados: URL da página de chamados.
  - username: Seu nome de usuário.
  - password: Sua senha.
  - discord_token: Token do seu bot no Discord.
  - discord_channel_id: ID do canal onde você quer receber as notificações.
  
## Uso
- Crie um bot no Discord, adicione-o ao seu servidor e obtenha o token do bot.
- Obtenha o ID do canal onde você quer receber as notificações.
- Execute o script `discord_bot.py`.

## Estrutura do Código
- Importações e Configurações: Importa as bibliotecas necessárias e define as configurações.
- Função de Login: Faz login no site e retorna uma sessão autenticada.
- Função para Verificar Chamados: Verifica novos chamados na página e retorna uma lista de novos chamados.
- Função para Enviar Notificações via Discord: Envia uma notificação para o canal do Discord.
- Função Principal: Monitora os chamados continuamente e envia notificações quando novos chamados são detectados.
- Execução do Bot: Configura e executa o bot do Discord.
