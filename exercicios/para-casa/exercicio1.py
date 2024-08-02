import pandas as pd
df = pd.read_csv('vendas_ficticias.csv')
print(df.head())

media_vendas = df['Quantidade vendida'].mean()
media_preços = df['Valor da venda'].mean()
print (f"Média das vendas: {media_vendas}")
print ()