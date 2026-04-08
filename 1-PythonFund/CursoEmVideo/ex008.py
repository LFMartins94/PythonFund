# Converter metros em km, hm, dam, m, dm ,cm e mm

# Leitura da distância em metros. O .strip() é boa prática, mas
# para float, é mais comum a leitura direta, já que espaços são removidos.
medida_m = float(input('Uma distância em metros:\n').strip())

# Conversões (A partir de 1 metro):
# Para CIMA (Dividir)
km = medida_m / 1000  # 3 casas à esquerda (m -> dam -> hm -> km)
hm = medida_m / 100   # 2 casas à esquerda
dam = medida_m / 10   # 1 casa à esquerda

# Para BAIXO (Multiplicar)
dm = medida_m * 10    # 1 casa à direita
cm = medida_m * 100   # 2 casas à direita
mm = medida_m * 1000  # 3 casas à direita

# Imprimindo os resultados
print("-" * 30)
print(f'A medida de {medida_m} metros equivale a:')
print(f'| Quilômetro (Km): {km} Km')
print(f'| Hectômetro (Hm): {hm} Hm')
print(f'| Decâmetro (Dam): {dam} Dam')
print(f'| Decímetro (Dm): {dm} Dm')
print(f'| Centímetro (Cm): {cm} Cm')
print(f'| Milímetro (Mm): {mm} Mm')
print("-" * 30) 