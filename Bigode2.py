
import requests
import time
import json
import os
# esse codigo foi tirado completim do github eu to entendendo como que ele funciona e adaptando ele né
# da uma olhada ae mum sei
# dica -> seja sempre mais esperto que o seu antigo eu!

class TelegramBot:
    def __init__(self):
        token = '1533440818:AAHM4nJxPorDEMjIBjdjdxmJh-So_v4yBco' # token do telegram do bigode2
        self.url_base = f'https://api.telegram.org/bot{token}/' # t.me/Bigode2_Bot // numero do bot pode testar ali, mas tem q testar com o codigo rodando né//


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
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100' # n meche nesse timeout se n da merda
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content) # Parnasianismo classico não faz sentido nenhum mas é bem legal ao mesmo tempo.

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem): # {os.linesep} = espaço para o telegram
        if eh_primeira_mensagem == False:
            return f'''Olá, Meu nome é Rogerim, mas todos me chamam de bigode.{os.linesep}, Vou te dar o menu e qualquer coisa me chama!{os.linesep}'''
        elif mensagem == ('menu', 'Menu') or mensagem == ('Bigode','Rogerim','bigode', 'garçom','rogerim'):
            return f'''Diga ae meu chegado, seguinte hoje a brahma ta geladinha, se quiser a brahma é so dizer 'brama'.{os.linesep}, se quiser outra, temos aqui no estoque deixa eu ver...{os.linesep}{os.linesep}Temos: Skol, Heineken e Antártida!'''
        elif mensagem == ('Brahma', 'brahma'):
            return f'''Pode deixar, uma bem gelada pra chefia{os.linesep}Posso pedir?(s/n)
            '''
        elif mensagem == ('Skol','skol'):
            return f'''Pode deixar, uma bem gelada pra chefia{os.linesep}Posso pedir?(s/n)
            '''
        elif mensagem == ('Antártida','antártida'):
            return f'''Pode deixar, uma bem gelada pra chefia{os.linesep}Posso pedir?(s/n)'''
        elif mensagem == ('Heineken', 'heineken'):
            return f'''Pode deixar, uma bem gelada pra chefia{os.linesep}Posso pedir?(s/n)'''

        elif mensagem.lower() in ('s', 'sim'):
            return ''' Ta aqui chefia '''
        elif mensagem.lower() in ('n', 'não'):
            return ''' Então decide logo né '''
        else:
            return 'Da uma boa olhada no cardapio ai senhor pq quem ganha dinheiro sem fazer nada é filosofo.'

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot() # Sábio é aquele que conhece os limites da própria ignorância. - Sócrates frasesparaface.com.br/frases-intelectuais
bot.Iniciar()