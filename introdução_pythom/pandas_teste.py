import pandas as pd 

dados = {
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor'],
    'Preço': [2500, 50, 150, 800],
    'Estoque': [10, 45, 30, 15]
}

df = pd.DataFrame(dados) #cria uma tabela com os dados

print(df)

preco_medio = df['Preço'].mean() #calcula o preço médio
print(f'\nPreço médio: R$ {preco_medio:.2f}')