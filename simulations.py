import pandas as pd

dados_vendas = pd.read_csv('dados.csv')
df = dados_vendas
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

def nova_receita(meta):
    receita_atual = df['Preço Total'].sum()
    print(f"Receita atual: R$ {receita_atual:.2f}")

    meta_receita = receita_atual * meta
    print(f"Meta de receita: R$ {meta_receita:.2f}")

    vendas_necessarias = meta_receita - receita_atual
    print(f"Vendas adicionais necessárias: R$ {vendas_necessarias:.2f}")

    df['Vendas Proporcionais'] = (df['Preço Total'] / receita_atual) * vendas_necessarias

    df['Vendas Simuladas'] = df['Preço Total'] + df['Vendas Proporcionais']

    nova_receita_simulada = df['Vendas Simuladas'].sum()
    print(f"Nova receita simulado: R$ {nova_receita_simulada:.2f}")

    print("\nVendas simuladas por produto:")
    print(df[['Produto', 'Vendas Simuladas']])

nova_receita(meta=2)