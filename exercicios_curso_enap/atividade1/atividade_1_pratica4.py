#------------------------------------Atividade 1 - Prática 4---------------------------

# 1 - Faça um programa que peça 2 números inteiros e um número decimal. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo;
# a soma do triplo do primeiro com o terceiro;
# o terceiro elevado ao cubo.
# Entrada de dados
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = float(input("Digite um número decimal: "))   
# Cálculos
produto = (2 * num1) * (num2 / 2)
soma = (3 * num1) + num3
cubo = num3 ** 3        
# Exibição dos resultados
print(f"O produto do dobro do primeiro com metade do segundo é: {produto}")
print(f"A soma do triplo do primeiro com o terceiro é: {soma}")
print(f"O terceiro elevado ao cubo é: {cubo}")


#2. Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando um automóvel que faz 12 quilômetros por litro. Para o cálculo, o usuário deve fornecer o tempo gasto e a velocidade média durante a viagem. Desta forma, será possível obter a distância percorrida com a fórmula: 
#DISTANCIA ← VELOCIDADE × TEMPO. 
#A partir do valor da distância, basta calcular a quantidade em litros de combustível utilizada na viagem com a fórmula:
#LITROS_USADOS ← DISTÂNCIA / 12. 
#O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizados na viagem.
# Entrada de dados
tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
velocidade = float(input("Digite a velocidade média durante a viagem (em km/h): "))
# Cálculos
distancia = velocidade * tempo
litros_usados = distancia / 12
# Exibição dos resultados
print(f"A velocidade média durante a viagem é: {velocidade} km/h")
print(f"O tempo gasto na viagem é: {tempo} horas")
print(f"A distância percorrida é: {distancia} km")
print(f"A quantidade de litros utilizados na viagem é: {litros_usados} litros")         

