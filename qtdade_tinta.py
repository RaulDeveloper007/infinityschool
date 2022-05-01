tamanho = int(input('Quantos m² serão pintados?'))
import math
litros = tamanho / 3
latas = litros // 18
custo = latas * 80
print(f'Para pintar {tamanho}m², serão necessárias {math.ceil(latas)} latas de tinta que custarão {custo:.2f} R$.')
