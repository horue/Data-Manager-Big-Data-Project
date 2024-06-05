import pandas as pd

dados_vendas = pd.read_csv('dados.csv')
df = dados_vendas
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')



def mais_vendidos(mes_desejado):
    df_mes = df[(df['Data'].dt.month == mes_desejado)]

    produtos_vendidos = df_mes.groupby('Produto')['Quantidade'].sum().reset_index()
    produtos_vendidos = produtos_vendidos.sort_values(by='Quantidade', ascending=False)

    print(f'Produtos mais vendidos - Mês {mes_desejado}')
    print(produtos_vendidos)


def menos_vendidos(mes_desejado):
    df_mes = df[(df['Data'].dt.month == mes_desejado)]

    produtos_vendidos = df_mes.groupby('Produto')['Quantidade'].sum().reset_index()
    produtos_vendidos = produtos_vendidos.sort_values(by='Quantidade', ascending=True)

    print(f'Produtos menos vendidos - Mês {mes_desejado}')
    print(produtos_vendidos)

def meses():
    df['Ano Mes'] = df['Data'].dt.to_period('M')

    vendas_por_mes = df.groupby('Ano Mes')['Preço Total'].sum().reset_index()

    vendas_por_mes = vendas_por_mes.sort_values(by='Preço Total')
    print(vendas_por_mes)

mais_vendidos(mes_desejado=4)
menos_vendidos(mes_desejado=2)
meses()