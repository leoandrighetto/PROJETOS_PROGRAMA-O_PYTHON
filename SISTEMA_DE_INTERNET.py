#PRIMEIRO PASSO PARA CRIAR UM SITE:

#ESCREVER O PASSO A PASSO DO SITE INTEIRO:

#TELA INICIAL
    #TÍTULO: LEROYZAP
    #BOTÃO: INICIAR CHAT
        #QUANDO CLICAR NO BOTÃO:
        #ABRIR UM POPUP\ALERTA\MODAL
            #TÍTULO: BEM VINDO AO LEROYZAP
            #CAIXA DE TEXTO: ESCREVA SEU NOME
            #BOTÃO: ENTRAR NO CHAT
                #QUANDO CLICAR NO BOTÃO
                # SUMIR COM O TÍTULO
                # SUMIR COM O BOTÃO INICIAR CHAT
                    #CARREGAR CHAT
                    #CARREGAR O CAMPO DE ENVIAR MENSAGEM: DIGITE SUA MENSAGEM
                    # BOTÃO ENVIAR
                        #QUANDO CLICAR NO BOTÃO ENVIAR
                        #ENVIAR MENSAGEM
                        #LIMPAR A CAIXA DE MENSAGEM

#PARA A CRIAÇÃO DESTE APLICATIVO, USAREI A FERRAMENTA FLET
#SEMPRE QUE EU FOR COSTRUIR UM APLICATIVO USANDO FLET, EU SEGUIREI TRÊS ETAPAS:

'''
# 1- IMPORTAR O FLET

#pip install flet (no terminal do vs code)
import flet as ft

# 2- CRIAR UMA FUNÇÃO PRINCIPAL PARA RODAR MEU APLICATIVO

def main():



# 3- EXECUTAR ESTA FUNÇÃO SOM O FLET
ft.app(main)
'''

import flet as ft



def main(pagina): #USUALMENTE USAREI O NOME 'MAIN' COMO NOME, E COMO PARÂMETRO A PAGINA ONDE OS ELEMENTOS IRÃO APARECER.
    
    #Nesta página inicial haverá o titulo, e o botão de iniciar o chat
    #porém também devo criar o código do pop_up.

    titulo = ft.Text('LeroyZAP')            #cria o título
    pagina.add(titulo)                      #adiciona na pagina

    #PARA CRIAR O POP_UP NA PRÓXIMA FUNÇÃO, EU ADICIONO TÍTULO, CAIXA DE TEXTO, E O BOTÃO.
    titulo_pop_up = ft.Text('Bem-vindo ao LeroyZAP')
    caixa_de_nome = ft.TextField('Digite seu nome') #FT.TEXTFIEL é uma caixa com um texto de orientação.
    botao_pop_up = ft.ElevatedButton('Entrar no Chat')

    # USANDO 'ESTE COMANDO ', ADICIONO OS PARÂMETROS ACIMA, DENTRO DO POP_UP.
    pop_up = ft.AlertDialog(title=titulo_pop_up, content= caixa_de_nome, actions=[botao_pop_up]) # SEMPRE NO PLURAL = LISTA.
                                #título              conteúdo                parâmetros
        
    #CRIO A FUNÇÃO DO POP_UP
    def abrir_popup(evento):   #SEMPRE ADICIONO O PARÂMETRO EVENTO QUANDO O USUÁRIO DEVE "CLICAR" NA TELA. "CLICAR = EVENTO = PARÂMETRO"
        pagina.dialog = pop_up #PARA O PUP_UP APARECER NA FRENTE DA TELA, A PÁGINA O RECEBE COMO DIÁLOGO.
        pop_up.open = True  #VALIDA A ABERTURA DO POP_UP
        pagina.update() #ATUALIZA SEMPRE A PÁGINA PARA O USUÁRIO (SÓ DECORA, PORQUE É OBRIGATÓRIO)
        #minha função SE CHAMA página. Mas eu poderia ter dado qualquer outro nome.

        


    botao = ft.ElevatedButton('Iniciar Chat', on_click = abrir_popup)               #cria o botão
    pagina.add(botao)                                       #adiciona na pagina

