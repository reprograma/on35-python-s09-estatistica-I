# # Exercício de Casa 🏠 

# ## Objetivo

# Realizar uma análise estatística descritiva dos dados de vendas.

# ## Descrição do Desafio

# Suponha que você trabalhe em uma equipe de vendas e recebeu uma lista de vendas fictícias de diferentes produtos ao longo de vários meses. Seu objetivo é realizar uma análise estatística descritiva dos valores das vendas.

# ## Conjunto de Dados
# Os dados estão disponíveis em formato csv (‘vendas_ficticias.csv’) e contêm as seguintes informações para cada venda:

#   •	Data da venda
#   •	Valor da venda
#   •	Vendedor
#   •	Quantidade vendida
#   •	Produto

# ## Perguntas para responder
# #1.	Calcular a média, mediana, mínimo, máximo e desvio padrão dos valores das vendas e quantidade vendida.
# # 2.	Qual produto que mais vendeu? (Usar a moda para identificar).


import pandas as pd #importar biblioteca pandas
from tabulate import tabulate #importar biblioteca para estilizar os dados

datas = pd.read_csv('vendas_ficticias.csv') #lendo os dados do arquivo vendas_ficticias.csv 

#Imprimindo os dados da tabela
print(tabulate(datas, headers='keys', tablefmt='fancy_grid'))

def dados_estatisticos(x,y,z):#declarando função com os parametros os 3 parametros utilizados
    print("\n-------------------------Valores das Vendas-------------------------\n")
    #1. Média, mediana, máximo, mínimo e desvio padrão dos valores das vendas
    avg_sales = round(x.mean(),2)
    median_sales = round(x.median(),2)
    max_sales = round(x.max(),2)
    min_sales = round(x.min(),2)
    standard_deviation_sales = round(x.var() ** 0.5,2)

    print(f'Média Valor da Venda: R${avg_sales}')
    print(f'Mediana Valor da Venda: R${median_sales}')
    print(f'Máximo Valor de Venda: R${max_sales}')
    print(f'Mínimo Valor de Venda: R${min_sales}')
    print(f'Desvio Padrão das Vendas: R${standard_deviation_sales}')

    print("\n-------------------------Quantidade Vendida-------------------------\n")

    #1. Média, mediana, máximo, mínimo e desvio padrão das quantidades vendidas
    avg_amount = round(y.mean(),2)
    median_amount = round(y.median(),2)
    max_amount = round(y.max(),2)
    min_amount = round(y.min(),2)
    standard_deviation_amount = round(y.var() ** 0.5,2)

    print(f'Média Qtd Vendida: {avg_amount}')
    print(f'Mediana Qtd Vendida: {median_amount}')
    print(f'Qtd Máxima Vendida: {max_amount}')
    print(f'Qtd Mínima Vendida: {min_amount}')
    print(f'Desvio Padrão das Qtds Vendidas: {standard_deviation_amount}')

    print("\n-------------------------Produto + Vendido-------------------------\n")
    #2. Qual produto mais vendeu?
    best_sold = round(z.mode(),2)
    print(f'Produto mais vendido: {best_sold}')

dados_estatisticos(datas['Valor da venda'],datas['Quantidade vendida'],datas['Produto'])#chamando a funcao e passando os parametros
