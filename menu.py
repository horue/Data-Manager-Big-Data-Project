import webbrowser as wb
import sys
import os
from analizer import *

def principal_menu():
    option = input("> ")
    if option == "1":
        sys.exit()
    elif option == "2":
        analisar()
    elif option == "3":
        exportar_dados()
    elif option == "4":
        ajuda()
    else:
        print("Por favor, entre um comando válido.")
        principal_menu()

def analisar_menu():
    option = input('> ')
    if option == '1':
        media_vendas()
    elif option == '2':
        analisar_vendas()
    elif option == '3':
        principal()
    elif option == '4':
        sys.exit()
    else:
        print('Por favor, entre um comando válido.')
        analisar_menu()

def analisar_vendas_menu():
    option = input('> ')
    if option == '1':
        print('Produtos mais vendidos.')
        mes = int(input('Digite o mês desejado (1-12): '))
        mais_vendidos(mes_desejado=mes)
    elif option == '2':
        print('Produtos menos vendidos.')
        mes = int(input('Digite o mês desejado (1-12): '))
        menos_vendidos(mes_desejado=mes)
    elif option == '3':
        meses(ascending=False)
    elif option == '4':
        analisar()
    elif option == '5':
        sys.exit()
    else:
        print('Por favor, entre um comando válido.')
        analisar_vendas_menu()

def ajuda_menu():
    option = input("> ")
    if option.lower() == 'mais':
        wb.open('https://github.com/horue')
        principal()
    elif option.lower() == '':
        principal()
    else:
        print('Por favor, entre um comando válido.')
        ajuda_menu()

def principal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#" * 35)
    print('# Data Manager - Tela Inicial #')
    print("#" * 35)
    print('1 — Sair')
    print('2 — Analisar dados')
    print('3 — Exportar dados')
    print('4 — Ajuda')
    print('Feito por Jorge Magno e Matheus Binder.')
    principal_menu()

def ajuda():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#" * 35)
    print('# Data Manager - Tela de Ajuda #')
    print("#" * 35)
    print('— Use comandos para acessar, alterar ou apagar dados no banco de dados.')
    print("— Caso ainda tenha alguma dúvida, use o comando 'Mais' para ser redirecionado à documentação do programa.")
    print("— Para voltar à tela anterior, aperte Enter.")
    print('Feito por Jorge Magno e Matheus Binder.')
    ajuda_menu()

def analisar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#" * 35)
    print('# Data Manager - Tela de Análise #')
    print("#" * 35)
    print('1 — Analisar Renda')
    print('2 — Analisar Vendas')
    print('3 — Voltar')
    print('4 — Sair')
    print('Feito por Jorge Magno e Matheus Binder.')
    analisar_menu()

def analisar_vendas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#" * 35)
    print('# Data Manager - Tela de Análise de Vendas #')
    print("#" * 35)
    print('1 — Produtos mais vendidos')
    print('2 — Produtos menos vendidos')
    print('3 — Meses com mais vendas')
    print('4 — Voltar')
    print('5 — Sair')
    print('Feito por Jorge Magno e Matheus Binder.')
    analisar_vendas_menu()

def exportar_dados():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#" * 35)
    print('# Data Manager - Tela de Exportação #')
    print("#" * 35)
    print("Funcionalidade de exportação ainda não implementada.")
    principal()