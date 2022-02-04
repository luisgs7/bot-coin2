###  Bot Coin
O Bot Coin é um projeto <strong>Open Source</strong> de um bot para o Telegram, que possibilita informar a cotação do Dólar, Bitcoin e Euro, a partir de uma API.
#
Está em desenvolvimento a funcionalidade de  converter valores informados pelo usuário.

## Stack
<li>
<a  href="https://www.python.org/">Python</a>
</li>

<li>
<a  href="https://python-poetry.org/">Poetry</a>
</li>

<li>
<a  href="https://docs.pytest.org/en/latest/">Pytest</a> (A ser desenvolvido)
</li>

<li>
<a  href="https://docs.python-requests.org/en/latest/">Requests</a>
</li>

<li>
<a  href="https://hgbrasil.com/status/finance">Hgbrasil</a> (Api de dados)
</li>

<li>
<a  href="https://core.telegram.org/bots">Telegram Bot</a>
</li>

<li>
<a href="https://docs.github.com/pt/actions">GitHub Actions</a>
</li>

<li>
<a href="https://www.heroku.com/">Heroku</a> (Deploy ainda a ser realizado)
</li>

## Bot Screens
<br/>

## 01 - Start Bot
<p><img alt="Image" title="icon" src="https://raw.githubusercontent.com/luisgs7/bot-coin/main/screens-bot/01.jpg" width="200" height="400" ></p>


## 02 - Acessando o Menu do Bot
<p><img alt="Image" title="icon" src="https://raw.githubusercontent.com/luisgs7/bot-coin/main/screens-bot/02.jpg" width="200" height="400"></p>


## 03 - Acessando as Cotações do Dólar, Bitcoin e Euro
<img alt="Image" title="icon" src="https://raw.githubusercontent.com/luisgs7/bot-coin/main/screens-bot/03.jpg" width="200" height="400">
<br/>
<br/>
<img alt="Image" title="icon" src="https://raw.githubusercontent.com/luisgs7/bot-coin/main/screens-bot/04.jpg" width="200" height="400">
<br/>

# Start the project

01 - Primeiro realize o clone do repositório, ou um fork para o seu usuário no github.

02 - Em seguida <a href="https://core.telegram.org/bots">crie um bot no telegram</a>, utilize a documentação do telegram com todas as instruções necessárias. 

03 - Adiante crie uma conta na <a  href="https://hgbrasil.com/status/finance">Hgbrasil</a>, este site fornece uma apikye que possibilita acessar  a api em um plano gratuito, que fornece todas as cotações das moedas que o bot necessita. 

04 - Na raiz do projeto crie um arquivo chamado <strong>.env</strong> e adicione as duas variáveis de ambiente, assim como apresentado abaixo:
```yaml
TOKEN=12345 # TOKEN do bot do telegram
APIKYE=4321 # APIKYE da Hgbrasil

```

03 - Crie um ambiente virtual com o <a href="https://python-poetry.org/">Poetry</a> e instale as dependências do projeto.

04 - Para inicializar o bot basta executar o seguinte comando, na raiz do projeto: 

```yaml
python3 main.py

```
05 - Agora você já pode utilizar o seu bot :) 

# Importante
Este projeto é para a comunidade Python, sintasse a vontade para utilizá-lo, tendo qualquer dúvida ou sugestão basta adicionar uma mensagem nas issues, ou me adicionar no linkedin, link para o perfil na página inicial do github.

Além disso, sintasse a vontade para mandar um <i>pullrequest</i>, com uma correção ou nova feature, não se esqueça de antes adicionar uma <i>issue</i> com a funcionalidade que você irá corrigir ou criar.

### Se você gostou do projeto, compartilhe com os seus amigos, com a sua comunidade, adicione uma <i>Star</i> no repositório.
 
