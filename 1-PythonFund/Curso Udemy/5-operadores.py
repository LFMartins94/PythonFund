n1 = int(input('Digite o primeiro número\n'))
n2 = int(input('Digite o segundo número\n'))

#Aritméticos
s = n1 + n2 
sub = n1 - n2
div = n1 / n2
mult = n1 * n2
mod = n1 % n2
exp = n1 ** n2
print(f'Soma de {n1} mais {n2} e igual a {s}')
print(f'A subtração de {n1} menos {n2} e igual a {sub}')
print(f'A divisão de {n1} por {n2} e igual a {div}')
print(f'A multiplicação de {n1} por {n2} e igual a {mult}')
print(f'O resto da divisão entre {n1} por {n2} e {mod}')
print(f'Potencia do número {n1} por {n2} e {exp}')

#Comparação
bigger = n1 > n2 #Sinal de maior: >
smaller = n1 < n2 #Sinal de menor: <
equal = n1 == n2 #Sinal de comparação: ==
different = n1 != n2 #Sinal de diferente: != 
bigger_equal = n1 >= n2 #Sinal de maior ou igual á: >=
smaller_equal = n1 <= n2 #Sinal de menor ou igual á: <=

print(f'Os números {n1} e {n2} são igual? {equal}')
print(f'Os números {n1} e {n2} são diferentes? {different}')
print(f'O número {n1} e maior que {n2}? {bigger}')
print(f'O número {n1} e menor que {n2}? {smaller}')
print(f'O número {n1} e maior ou igual a {n2}? {bigger_equal}')
print(f'O númeor {n1} e menor ou igual a {n2}? {smaller_equal}')

#Atribuição
n1 += 1 # n1 = n1 + 1
n1 -= 1 # n1 = n1 - 1
n1 *= 1 # n1 = n1 * 1
n1 /= 1 # n1 = n1 / 1