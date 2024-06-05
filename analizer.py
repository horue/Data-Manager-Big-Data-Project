import pandas as pd

dados_vendas = pd.read_csv('dados.csv')
df = dados_vendas


def mais_vendidos(mes_desejado):
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

    df_mes = df[(df['Data'].dt.month == mes_desejado)]

    produtos_vendidos = df_mes.groupby('Produto')['Quantidade'].sum().reset_index()
    produtos_vendidos = produtos_vendidos.sort_values(by='Quantidade', ascending=False)

    print(f'Produtos mais vendidos - Mês {mes_desejado}')
    print(produtos_vendidos)

mais_vendidos(mes_desejado=4)