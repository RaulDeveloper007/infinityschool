numeros = [ ]
def criar_lista():
    for numero in range(20):
        num = int(input('Insira um número: '))
        numeros.append(num)
lista = criar_lista()

pares = [ ]
intervalo = [ ]
multiplos =  [ ]
def  novas_listas(numeros):
    for item in numeros:
        if item % 2 == 0:
            pares.append(item)
        elif item >= 1 and item <= 9:
            intervalo.append(item)
        elif item % 3 == 0 and item % 5 == 0:
            multiplos.append(item)
novas_listas(numeros)

print(f'Sua lista é: {numeros}')
print(f'A lista de números pares é: {pares}')
print(f'A lista de números múltiplos de 3 e 5: {multiplos}')
print(f'A lista de números entre 1 e 9 é: {intervalo}')