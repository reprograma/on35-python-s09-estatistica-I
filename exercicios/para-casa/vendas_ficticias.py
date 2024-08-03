#Exercício de Casa 🏠 Realizar uma análise estatística descritiva dos dados de vendas.
#Conjunto de Dados em formato csv (‘vendas_ficticias.csv’), com as seguintes informações para cada venda:

#Data da venda
#Valor da venda
#Vendedor
#Quantidade vendida
#Produto

#Responder:
#1-Calcular a média, mediana, mínimo, máximo e desvio padrão dos valores das vendas e quantidade vendida.
#2-Qual produto que mais vendeu? (Usar a moda para identificar).

#importar a biblioteca pandas 
import pandas as pd
#importar a biblioteca tabulate para melhor organização da tabela
from tabulate import tabulate

# Carregar o arquivo CSV
file_path = 'vendas_ficticias.csv'  # Atualize o caminho se necessário
df = pd.read_csv(file_path)

# Calcular estatísticas descritivas
estatisticas = {
    'Estatística': ['Média', 'Mediana', 'Mínimo', 'Máximo', 'Desvio Padrão'],
    'Valor da Venda': [
        df['Valor da venda'].mean(),
        df['Valor da venda'].median(),
        df['Valor da venda'].min(),
        df['Valor da venda'].max(),
        df['Valor da venda'].std()
    ],
    'Quantidade Vendida': [
        df['Quantidade vendida'].mean(),
        df['Quantidade vendida'].median(),
        df['Quantidade vendida'].min(),
        df['Quantidade vendida'].max(),
        df['Quantidade vendida'].std()
    ]
}

# Identificar o produto que mais vendeu (usando a moda)
produto_mais_vendido = df['Produto'].mode()[0]

# Imprimir a tabela completa do CSV usando o tabulate
print("Tabela de Vendas:")
print(tabulate(df, headers='keys', tablefmt='grid'))

# Exibir as estatísticas em uma tabela formatada
print("\nEstatísticas Descritivas:")
print(tabulate(estatisticas, headers='keys', tablefmt='grid'))

# Exibir o produto que mais vendeu
print(f"\nProduto que mais vendeu: {produto_mais_vendido}")