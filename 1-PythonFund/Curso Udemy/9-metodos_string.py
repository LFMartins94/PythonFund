gameName = 'Fifa 25'
gameDescription = '''
Fifa 25 e um jogo de futebol, desenvolvido pela EA Sports, 
é que pode ser jogado online ou offline!
'''


print(gameName.upper()) # Retornar string em maiúsculo
print(gameName.lower()) # Retornar string em minúsculo
print(gameName.capitalize()) # Apenas a primeira letra em maiúsculo
print(gameName.title()) # Apenas a primeira letra em maiúsculo
print(gameName.center(10, '-')) # Retorna a string centralizada com caractere de preenchimento
print(gameName.find('a')) # Retorna a posição de um determinado caractere, o primeiro e contado como zero '0'
print(gameDescription.count('a')) # Conta caracteres
print(gameDescription.count('f')) # Conta caracteres
print(gameDescription.count('F')) # Conta caracteres
print(gameName.replace('Fifa', 'Pes')) # Altera um elemento por outro
print(gameDescription.replace('Fifa', 'pes',))
print(gameDescription.split(','))
