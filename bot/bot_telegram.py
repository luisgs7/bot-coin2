import requests
import time
import json
import os

from price.app import price_dolar, price_btc, price_eur


class TelegramBot:
    def __init__(self):
        token = my_secret = os.environ['TOKEN']
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]

            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]

                    primeira_mensagem = int(dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(mensagem, primeira_mensagem)
                    self.responder(resposta, chat_id)

    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'

        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    def criar_resposta(self, mensagem, primeira_mensagem):
        ## Resposta do usuário
        time.sleep(1)
        if primeira_mensagem == True or mensagem.lower() in 'menu':
            return f'''Olá bem vindo ao BotCoin, digite a opção desejada:{os.linesep}
      1 - Cotação do Dólar Americano {os.linesep}
      2 - Cotação do Bitcoin {os.linesep}
      3 - Cotação do Euro {os.linesep}   
      '''
        if mensagem in '1':
            dolar = price_dolar()
            return f'''Cotação do Dólar{os.linesep}Dólar: R$ {dolar}{os.linesep}'''

        elif mensagem in '2':
            btc = price_btc()
            return f'''Cotação do Bitcoin{os.linesep}Bitcoin: R$ {btc}{os.linesep}'''

        elif mensagem in '3':
           eur = price_eur()
           return f'''Cotação do Euro{os.linesep}Euro: € {eur}'''

        else:
            return 'Gostaria de acessar o menu? Digite "menu"'

    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)
