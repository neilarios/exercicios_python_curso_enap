#------------------------Atividade 1 - Prática 1----------------------------

# 1 - Faça um programa que exiba a mensagem “Olá, seja bem-vinda!”. 

print("Olá, seja bem vinda!")

# 2 - Faça um programa que exiba na tela o seu nome e o setor em que você atua.

print ( "Meu nome é Neila Rios e trabalho na CGTI ENAP")

#------------------------Atividade 1 - Prática 2-----------------------------

# 1 - Faça um programa que solicite o salário de uma servidora e então mostre a mensagem
# “O salário informado foi” seguido do valor obtido como entrada. 

salario = float(input("Informe o salário da servidora: "))
print("O salário informado foi: ", salario)
print(f"O salário informado foi, {salario}")

#2 - Fazer um programa para ler dois números inteiros, calcular e imprimir:
a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))
# a) A soma dos dois números
print(f"A soma dos dois números é: {a + b}")
# b) A subtração do primeiro pelo segundo
print(f"A subtração do primeiro pelo segundo é: {a - b}")
# c) A multiplicação dos dois números
print(f"A multiplicação dos dois números é: {a * b}")
# d) A divisão do primeiro número pelo segundo
print(f"A divisão do primeiro número pelo segundo é: {a / b}")
# e) O resto da divisão do primeiro pelo segundo
print(f"O resto da divisão do primeiro pelo segundo é: {a % b}")
# f) O primeiro número elevado ao quadrado 
print(f"O Primeiro número ao quadrado: {a ** 2}")

# 3. Faça um programa que solicite o salário de três servidoras e mostre a média de salário delas. 
salario1 = float(input("Informe o salário da primeira servidora: "))
salario2 = float(input("Informe o salário da segunda servidora: "))
salario3 = float(input("Informe o salário da terceira servidora: "))
media = (salario1 + salario2 + salario3) / 3
print(f"A média dos salários é: {media:.2f}")