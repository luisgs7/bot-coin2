import os

menu_message = f'''Olá bem vindo ao BotCoin, digite a opção desejada:{os.linesep}
      1 - Cotação do Dólar Americano {os.linesep}
      2 - Cotação do Bitcoin {os.linesep}
      3 - Cotação do Euro {os.linesep}
      4 - Converter Valores {os.linesep}   
      '''

menu_help = f'Gostaria de acessar o menu? Digite "menu"'

convert_value = f''' Escolha a opção desejada para realizar a conversão: {os.linesep}
    1 - Converter de Dólar    -> Real
    2 - Converter de Euro     -> Real
    3 - Converter de Bitcoin -> Real{os.linesep}  
    4 - Converter de Real     -> Dólar
    5 - Converter de Real     -> Euro
    6 - Converter de Real     -> Bitcoin            
'''