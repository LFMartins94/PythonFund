name = input('Digite o nome do Jogo\n')
yearLaunch = int(input('digite o ano de lançamento:\n'))
gamePrice = float(input('Digite o valor do Jogo:\n'))
planIncluded = (input('O jogo esta incluso no pacote?\n'))

print('###Dados do jogo###')
print('===================')
#Alternativa 1
# print('Nome do Jogo:', name)
# print('Ano do Jogo:', yearLaunch)
# print('Preço do Jogo:', gamePrice)
# print('Esta incluido no plano?', planIncluded)

#Alternativa 2
# print('Nome do Jogo:', name, '\n Ano do Jogo:', yearLaunch, '\n Preço do Jogo:', gamePrice, 
#     '\n Esta incluso no plano?', planIncluded)

#Alternativa 3
print(f'Nome do Jogo: {name} \nAno do Jogo: {yearLaunch} \nPreço do Jogo: {gamePrice} \nEsta incluido no plano? {planIncluded}')

#Teste
# print(f'Nome do Jogo: {name} Ano do Jogo: {yearLaunch} Preço do Jogo: {gamePrice} Esta incluido no plano? {planIncluded}')