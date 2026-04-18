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

#3. Faça um programa que receba o número de habitantes de uma população e o número de habitantes que
#  possuem acesso à internet. 
# Calcule a porcentagem de habitantes com acesso à internet (PA = habitantes com acesso à internet / número total de habitantes * 100).     
habitantes_total = int(input("Digite o número total de habitantes: "))
habitantes_acesso_internet = int(input("Digite o número de habitantes que possuem acesso à internet: "))
porcentagem_acesso_internet = (habitantes_acesso_internet / habitantes_total) * 100
print(f"A porcentagem de habitantes com acesso à internet é: {porcentagem_acesso_internet:.2f}%")           
