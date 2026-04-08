# --- FASE 1: Leitura e Armazenamento ---

# 1. Leitura do nome e do preço de cada produto
# É necessário ler o nome E o preço de cada produto
nome1 = input('Digite o nome do 1º produto:\n').strip()
preco1 = float(input(f'Digite o preço de {nome1}:\n').strip())

nome2 = input('Digite o nome do 2º produto:\n').strip()
preco2 = float(input(f'Digite o preço de {nome2}:\n').strip())

nome3 = input('Digite o nome do 3º produto:\n').strip()
preco3 = float(input(f'Digite o preço de {nome3}:\n').strip())

# 2. Armazene os dados em um dicionário (Chave: nome, Valor: preço)
# Correção: Usar as variáveis lidas (nomeN, precoN) para criar o dicionário
produtos = {
    nome1: preco1,
    nome2: preco2,
    nome3: preco3
}

# --- FASE 2: Impressões e Cálculos ---

# 3. Imprima: O dicionário completo.
print(produtos)

#4. Imprima: O produto mais caro.
#Usamos a função nativa max() com o argumento 'key' para ordenar pelos VALORES.
produto_mais_caro = max(produtos, key=produtos.get)
print(produto_mais_caro)

# 5. Imprima: A média dos preços.
# Correção: É preciso somar os valores (preços) e dividir pela quantidade.
precos = produtos.values() # Pega todos os valores (preços) do dicionário
soma_precos = sum(precos)
quantidade = len(precos)

media = soma_precos / quantidade
# Formata para duas casas decimais, como no exemplo
print(f'{media:.2f}')


