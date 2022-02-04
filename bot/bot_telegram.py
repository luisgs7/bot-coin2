import requests
import time
import json
import os
import dotenv

from bot.messages import menu_message, menu_help, convert_value 

dotenv.load_dotenv(dotenv.find_dotenv())

token = os.getenv("TOKEN") 

from price.app import price_dolar, price_btc, price_eur


class TelegramBot:
    def __init__(self):
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]

            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    message = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]

                    primeira_message = int(dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(message, primeira_message)
                    self.responder(resposta, chat_id)

    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'

        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    def criar_resposta(self, message, primeira_message):
        
        if primeira_message == True or message.lower() in 'menu':
            return menu_message

        if message in '1':
            dolar = price_dolar()
            return f'''Cotação do Dólar{os.linesep}Dólar: R$ {dolar}{os.linesep}'''

        elif message in '2':
            btc = price_btc()
            return f'''Cotação do Bitcoin{os.linesep}Bitcoin: R$ {btc}{os.linesep}'''

        elif message in '3':
           eur = price_eur()
           return f'''Cotação do Euro{os.linesep}Euro: € {eur}'''
        
        elif message in '4':
            return convert_value

        else:
            return menu_help

    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)
