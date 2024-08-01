# importando a biblioteca pandas
import pandas as pd

# Criar um DataFrame com dados fictícios

dados = {'id': [1001, 1002, 1003, 1004, 1005], #Qualitativo
             'uf': ['SP', 'SP', 'DF', 'DF','MG'], #Qualitativo
             'idade': [35, 45, 23, 25, 37], #Quantitativo Discreto
             'trabalha_como_jornalista': ['N', 'S', 'N', 'N', 'S'], #Qualitativo
             'escolaridade': ['4', '3', '5', '5', '5'], #Qualitativo
             'salario': [4200.00, 4500, 4500, 5340.00, 50000] #Quantitativo Continuo (quebrado)
            }
dados_df = pd.DataFrame(dados)
print(dados_df)

# cálculo manual = média
media = (35 + 45 + 23 + 25 + 37)/5
print(f'media python: {media}')

# cálculo usando a função mean
media_idade = dados_df['idade'].mean() #média com pandas
print(f'media pandas: {media_idade}')

# cálculo usando a função median
mediana_idade = dados_df['idade'].median() #mediana com pandas
print(f'mediana pandas: {mediana_idade}')

# cálculo usando a função mode
moda_idade = dados_df['idade'].mode()
print(f'moda pandas: {moda_idade}')

# função describe Pandas
dados_df.describe().T #traz apenas as informacoes quantativas

# função describe Pandas
dados_df.describe(include ='object').T #traz apenas as informacoes qualitativas

# função describe Pandas
print(dados_df.describe(include ='all').T) #traz apenas as informacoes qualitativas

media_salario = dados_df['salario'].mean()
print(f'A media dos salarios: {media_salario}')

mediana_salario = dados_df['salario'].median()
print(f'A mediana dos salarios: `{mediana_salario}')

moda_salario = dados_df['salario'].mode()
print(f'A moda dos salarios: {moda_salario}')
