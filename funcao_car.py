caracteres = [ ]

def inserir_lista():
    for i in range (10):
        i = input('Insira um caracter: ')
        caracteres.append(i)
    print(caracteres)

inserir_lista()

def ler_consoantes(caracteres):
    cons = 0
    for item in caracteres:
        if item.lower() not in 'aeiou':
            cons = cons + 1
    print(f'A quantidade de consoantes é: {cons}')

ler_consoantes(caracteres)

