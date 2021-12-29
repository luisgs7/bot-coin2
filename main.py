from bot.bot_telegram import TelegramBot
from price.app import price_eth

if __name__ == '__main__':
  price_eth()
  bot = TelegramBot()
  bot.Iniciar()

'''
USD-BRL
ETH
BTC
'''
