notas = [ ]

def media():
    for i in range (3):
        i = float(input('Insira uma nota: '))
        notas.append(i)
    print(f'A média das notas digitadas é: {(notas[0] + notas[1] + notas[2]) / 3 }')

media()
