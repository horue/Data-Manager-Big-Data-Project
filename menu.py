import webbrowser as wb
import sys
import os
from analizer import *




def principal_menu():
    option=input("> ")
    if option.lower() == ("1"):
        print(1)
    elif option.lower() == ('2'):
        print(1)
    elif option.lower() ==  ('3'):
        ajuda()
    elif option.lower() == ("4"):
        sys.exit
    while option.lower() not in ['1', '2', '3', '4', '5']:
        print("Por favor, entre um comando válido.")
        option=input("> ")



def ajuda_menu():
    option=input("> ")
    if option.lower() ==  ('mais'):
        wb.open('https://github.com/horue')
        principal()
    if option.lower() == (''):
        principal()
    while option.lower() not in ['']:
        print('Por favor, entre um comando válido. ')
        option=input("> ")
        return ajuda_menu()

    
def principal():
    os.system('cls')
    print("#" * 35)
    print('# Data Manager - Tela Inicial #')
    print("#" * 35)
    print('1 — Buscar dados')
    print('2 — Analisar dados')
    print('3 — Exportar dados')
    print('3 — Ajuda')
    print('4 — Sair')
    print('Feito por Jorge Magno e Matheus Binder.')
    principal_menu()


def ajuda():
    os.system('cls')
    print("#" * 35)
    print('# Data Manager - Tela de Ajuda #')
    print("#" * 35)
    print('— Use comandos para acessar, alterar ou apagar dados no banco de dados.')
    print("— Caso ainda tenha alguma dúvida, use o comando 'Mais' para ser redirecionado à docmuentação do programa.")
    print("— Para voltar à tela anterior, aperte Enter.")
    print('Feito por Jorge Magno e Matheus Binder.')
    ajuda_menu()
    return(principal)


def analisar():
    os.system('cls')
    print("#" * 35)
    print('# Data Manager - Tela de Análise #')
    print("#" * 35)
    print('1 — Analisar Renda')
    print('2 — Analisar Vendas')
    print('3 — Voltar')
    print('4 — Sair')
    print('Feito por Jorge Magno e Matheus Binder.')
    principal_menu()