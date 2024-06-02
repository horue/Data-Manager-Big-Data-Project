import webbrowser as wb
import sys
import os




def principal_menu():
    option=input("> ")
    if option == ("1"):
        print(1)
    elif option == ('2'):
        analisar()
    elif option ==  ('3'):
        ajuda()
    elif option == ("4"):
        sys.exit()
    else:
        print("Por favor, entre um comando válido.")
        principal_menu()

def analisar_menu():
    option=input('> ')
    if option == ('1'):
        print(1)
    elif option == ('2'):
        analisar_vendas()
    elif option == ('3'):
        principal()
    elif option == ('4'):
        sys.exit
    else:
        print('Por favor, entre um comando válido.')
        analisar_menu()
        
def analisar_vendas_menu():
    option=input('> ')
    if option == ('1'):
        print('Produtos mais vendidos.')
    elif option == ('2'):
        print('Produtos menos vendidos.')
    elif option == ('3'):
        principal()
    elif option == ('4'):
        sys.exit()
    else:
        print('Por favor, entre um comando válido.')
        analisar_vendas_menu()

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
    analisar_menu()

def analisar_vendas():
    os.system('cls')
    print("#" * 35)
    print('# Data Manager - Tela de Análise #')
    print("#" * 35)
    print('1 — Produtos mais vendidos')
    print('2 — Analisar menos vendidos')
    print('3 — Voltar')
    print('4 — Sair')
    print('Feito por Jorge Magno e Matheus Binder.')
    analisar_vendas_menu()