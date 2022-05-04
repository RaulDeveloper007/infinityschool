lista = [ ]
lista_pares = [ ]
lista_impares = [ ]

def criar_lista():
    for i in range(20):
        i = int(input('Insira um número: '))
        lista.append(i)
criar_lista()

def  par_impar(lista):
    par = 0
    impar = 0
    for num in lista:
        if num % 2 == 0:
            par += 1
            lista_pares.append(num)
        else:
            impar += 1
            lista_impares.append(num)
par_impar(lista)

print(f'A lista de números é: {lista}')
print(f'A lista de números pares é: {lista_pares}')
print(f'A lista de número ímpares é: {lista_impares}')
