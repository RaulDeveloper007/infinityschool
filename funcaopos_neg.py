n=0
def pos_neg():
    n= float(input('Informe um número: '))
    if n < 0:
        print('Esse número é negativo.')
    else:
        print('Esse número é positivo.')

while n == 0:
    pos_neg()