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


#2. Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando um automóvel 
# que faz 12 quilômetros por litro. Para o cálculo, o usuário deve fornecer o tempo gasto e a velocidade
#  média durante a viagem. Desta forma, será possível obter a distância percorrida com a fórmula: 
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


#3 Elaborar um programa que calcule e apresente o valor do volume de uma caixa retangular, 
# utilizando a fórmula:
#VOLUME = COMPRIMENTO * LARGURA * ALTURA
# Entrada de dados
comprimento = float(input("Digite o comprimento da caixa (em metros): "))
largura = float(input("Digite a largura da caixa (em metros): "))
altura = float(input("Digite a altura da caixa (em metros): "))
# Cálculo do volume
volume = comprimento * largura * altura 
# Exibição do resultado
print(f"O volume da caixa retangular é: {volume} metros cúbicos")


#4. Faça um programa que solicite o raio de um círculo, calcule e mostre sua área (A = π * r2, 
# #considere π = 3.14). 
# Entrada de dados
raio = float(input("Digite o raio do círculo: "))
# Cálculo da área
area = 3.14 * (raio ** 2)
# Exibição do resultado
print(f"A área do círculo é: {area:.2f}")


#5. Faça um programa que calcule a área de um quadrado, em seguida mostre seu resultado (A=L2).
# Entrada de dados
lado = float(input("Digite o lado do quadrado: "))
# Cálculo da área
area_quadrado = lado ** 2
# Exibição do resultado
print(f"A área do quadrado é: {area_quadrado:.2f}")

#6. Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas 
# por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
#  informar o total a receber no final do mês, com duas casas decimais.
# Entrada de dados
nome_vendedor = input("Digite o nome do vendedor: ")    
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
total_vendas = float(input("Digite o total de vendas efetuadas pelo vendedor no mês (em dinheiro): "))
# Cálculo da comissão e do total a receber
comissao = total_vendas * 0.15
total_receber = salario_fixo + comissao
# Exibição do resultado
print(f"O total a receber no final do mês para o vendedor {nome_vendedor} é: R$ {total_receber:.2f}")   

#Testando o comando GIT revert  







