tf = input("Informe uma temperatura em Fahrenheit:")
tf = float(tf)
tc = (tf-32)*5/9
print(f"{tf}º Fahrenheit, equivale a: {tc:.2f}º Celsius")