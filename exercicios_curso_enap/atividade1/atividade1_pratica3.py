#------------------------Atividade 1 - Prática 3----------------------------


#1.Faça um programa que receba o número de habitantes e 
# o número de leitos de UTI existentes em uma cidade.
#  Em seguida, calcule a quantidade de leitos de UTI por mil habitantes.


habitantes = int(input("Digite o número de habitantes: "))
leitos_uti = int(input("Digite o número de leitos de UTI: "))

#leitos_por_mil_habitantes = (leitos_uti / habitantes) * 1000
leitos_por_mil_habitantes = leitos_uti/(habitantes/1000)
print(f"A quantidade de leitos de UTI por mil habitantes é: {leitos_por_mil_habitantes:.2f}")


#2. Faça um programa que receba o número de habitantes de uma população
#  que tem permissão para trabalhar (maiores de 14 anos) e o número de habitantes desempregados.
#  Calcule a taxa de desemprego para esta população (TD = Desempregados/n° de habitantes).

habitantes_trabalhadores = int(input("Digite o número de habitantes que têm permissão para trabalhar: "))
habitantes_desempregados = int(input("Digite o número de habitantes desempregados: "))
taxa_desemprego = habitantes_desempregados / habitantes_trabalhadores
print(f"A taxa de desemprego para esta população é: {taxa_desemprego:.2f}")

#3. Faça um programa que pergunte quanto você ganha por hora e
#  o número de horas trabalhadas por semana. Calcule e mostre seu salário por semana.
ganho_por_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas_semana = int(input("Digite o número de horas trabalhadas por semana: "))
salario_semana = ganho_por_hora * horas_trabalhadas_semana
print(f"Seu salário por semana é: R$ {salario_semana:.2f}")

#4 Elaborar um programa que apresente o valor da conversão em real (R$) de um valor lido em dólar
# (US$). O programa deve solicitar o valor da cotação do dólar e também a quantidade de dólares 
# disponíveis com o usuário.
cotacao_dolar = float(input("Digite a cotação do dólar: "))
quantidade_dolares = float(input("Digite a quantidade de dólares disponíveis: "))
valor_em_reais = cotacao_dolar * quantidade_dolares
print(f"O valor da conversão em real (R$) é: R$ {valor_em_reais:.2f}")  

#5 Uma servidora do Ibama constatou que em uma determinada área de 35.000 ha,
#  foram desmatados 700 ha. Faça um programa que imprima na tela o percentual de desmatamento.
area_total = 35000
area_desmatada = 700
percentual_desmatamento = (area_desmatada / area_total) * 100
print(f"O percentual de desmatamento é: {percentual_desmatamento:.2f}%")

#6 Faça um programa que receba a quantidade de pessoas vacinadas no primeiro dia do mês
#  e  calcule a estimativa de vacinação mensal (OBS: considere o mês com 22 dias úteis). 

pessoas_vacinadas_dia = int(input("Digite a quantidade de pessoas vacinadas no primeiro dia do mês: "))
estimativa_vacinacao_mensal = pessoas_vacinadas_dia * 22
print(f"A estimativa de vacinação mensal é: {estimativa_vacinacao_mensal} pessoas")

#7 Faça um programa que receba o valor do salário de um funcionário
#  e o valor do salário mínimo, calcule e imprima quantos salários mínimos o funcionário recebe.
salario_funcionario = float(input("Digite o valor do salário do funcionário: "))
salario_minimo = float(input("Digite o valor do salário mínimo: "))
salarios_minimos = salario_funcionario / salario_minimo
print(f"O funcionário recebe {salarios_minimos:.2f} salários mínimos")