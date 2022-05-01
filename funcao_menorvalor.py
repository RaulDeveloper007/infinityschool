def menor (valor_1, valor2):
    valor1 = int(input('Informe um valor: '))
    valor2 = int(input('Informe outro valor: '))
    if valor1 < valor2:
        print(f'O número {valor1}, é menor')
    elif valor2 < valor1:
        print(f'O número {valor2}, é menor')
    elif valor1 == valor2:
        print(f'Os números são iguais.')

menor(0, 0)

