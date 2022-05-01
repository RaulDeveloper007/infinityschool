numero = contador = soma = media = 0
numero = int(input("Informe um número(999 para parar) :"))

while numero != 999:
    soma += numero
    contador += 1
    numero = int(input("Informe um número(999 para parar) :"))

media = soma / contador

print(f"Você digitou {contador} números. A soma entre eles foi {soma} e a média dos números digitados foi {media:.3}.")