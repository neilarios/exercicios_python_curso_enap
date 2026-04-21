#Atividade 2 - Prática 1 

#1. Faça um programa que leia o número de pessoas a serem atendidas em um dia na USF.
#Seu programa deve indicar para o médico qual será o tempo total da sua atividade de trabalho, 
#considerando que cada paciente terá em média 30 minutos para atendimento. Caso a CH de trabalho
#ultrapasse 8h, calcule a hora extra a ser recebida (valor da hora extra: R$ 100,00).
#Caso não ultrapasse 8h, mostre uma mensagem indicando que todos os pacientes serão atendidos.
num_pacientes = int(input("Digite o número de pessoas a serem atendidas em um dia na USF: "))
tempo_total_atendimento = num_pacientes * 30  # tempo total em minutos  
tempo_total_horas = tempo_total_atendimento / 60  # convertendo para horas
if tempo_total_horas > 8:
    horas_extras = tempo_total_horas - 8
    valor_hora_extra = 100
    valor_total_hora_extra = horas_extras * valor_hora_extra
    print(f"O tempo total de trabalho é: {tempo_total_horas:.2f} horas")
    print(f"Hora extra a ser recebida: R$ {valor_total_hora_extra:.2f}")    
else:
    print(f"O tempo total de trabalho é: {tempo_total_horas:.2f} horas")
    print("Todos os pacientes serão atendidos dentro do horário normal de trabalho.") 

#2. Faça um programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize o 
# operador módulo (resto da divisão). 
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
