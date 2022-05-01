import random

numero = random.randrange(1, 10)
number_user = int(input("Digite um número de 1 a 10: "))
if number_user > numero:
    print("O número digitado é maior que o sorteado.")
elif number_user < numero:
    print("O número digitado é menor que o sorteado.")
else:
    print("Você acertou!")

print(f"O número sorteado foi {numero}")