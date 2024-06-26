import pandas as pd

dados_vendas = pd.read_csv('vendas.csv')
df = dados_vendas
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')


def mais_vendidos(mes_desejado):
    df_mes = df[(df['Data'].dt.month == mes_desejado)]

    produtos_vendidos = df_mes.groupby('Produto')['Quantidade'].sum().reset_index()
    produtos_vendidos = produtos_vendidos.sort_values(by='Quantidade', ascending=False)

    print(f'Produtos mais vendidos - Mês {mes_desejado}')
    print(produtos_vendidos)
    return produtos_vendidos

def menos_vendidos(mes_desejado):
    df_mes = df[(df['Data'].dt.month == mes_desejado)]

    produtos_vendidos = df_mes.groupby('Produto')['Quantidade'].sum().reset_index()
    produtos_vendidos = produtos_vendidos.sort_values(by='Quantidade', ascending=True)

    print(f'Produtos menos vendidos - Mês {mes_desejado}')
    print(produtos_vendidos)
    return produtos_vendidos

def meses(ascending):
    df['Ano Mes'] = df['Data'].dt.to_period('M')

    vendas_por_mes = df.groupby('Ano Mes')['Preço Total'].sum().reset_index()

    vendas_por_mes = vendas_por_mes.sort_values(by='Preço Total', ascending=ascending)
    print(vendas_por_mes)
    return vendas_por_mes

def media_vendas():
    df['Ano Mes'] = df['Data'].dt.to_period('M')

    vendas_por_mes = df.groupby('Ano Mes')['Preço Total'].sum().reset_index()
    media_vendas_por_mes = vendas_por_mes['Preço Total'].mean()

    print("Média de vendas por mês: R$ {:.2f}".format(media_vendas_por_mes))
    return media_vendas_por_mes

def metodo_pagamento_vendas(mes):
    if mes:
        df['Ano Mes'] = df['Data'].dt.to_period('M')    
        pagamentos_por_metodo = df.groupby(['Ano Mes', 'Forma Pagamento']).size().reset_index(name='Quantidade')
    
    else:
        pagamentos_por_metodo = df['Forma Pagamento'].value_counts().reset_index()
        pagamentos_por_metodo.columns = ['Forma Pagamento', 'Quantidade']

    print("Quantidade de vendas por método de pagamento:")
    print(pagamentos_por_metodo)
    return pagamentos_por_metodo

def run():
    mais_vendidos(mes_desejado=4)
    menos_vendidos(mes_desejado=2)
    meses(ascending=False)
    media_vendas()
    metodo_pagamento_vendas(mes=True)

def exportar():
    mais_vendidos_df = mais_vendidos(mes_desejado=4)
    menos_vendidos_df = menos_vendidos(mes_desejado=2)
    meses_df = meses(ascending=False)
    media_vendas_valor = media_vendas()
    metodo_pagamento_vendas_df = metodo_pagamento_vendas(mes=True)

    mais_vendidos_df.to_csv('mais_vendidos.csv', index=False)
    menos_vendidos_df.to_csv('menos_vendidos.csv', index=False)
    meses_df.to_csv('vendas_por_mes.csv', index=False)
    
    media_vendas_df = pd.DataFrame({'Média de Vendas por Mês': [media_vendas_valor]})
    media_vendas_df.to_csv('media_vendas.csv', index=False)
    
    metodo_pagamento_vendas_df.to_csv('metodo_pagamento_vendas.csv', index=False)


run()