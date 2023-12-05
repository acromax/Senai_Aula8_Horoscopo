# Exercício 8 de Python - Senai Turma 21
# programa para retornar o Signo do usuário

# Apresentação
print('\nDescubra seu signo do zodíaco com base na sua data de nascimento.')

# Processamento
def determinar_signo(mes, dia):
    if (mes == 3 and dia >= 21) or (4 <= mes <= 4 and dia <= 19):
        return "Áries"
    elif (mes == 4 and dia >= 20) or (5 <= mes <= 5 and dia <= 20):
        return "Touro"
    elif (mes == 5 and dia >= 21) or (6 <= mes <= 6 and dia <= 20):
        return "Gêmeos"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 7 and dia <= 22):
        return "Câncer"
    elif (mes == 7 and dia >= 23) or (8 <= mes <= 8 and dia <= 22):
        return "Leão"
    elif (mes == 8 and dia >= 23) or (9 <= mes <= 9 and dia <= 22):
        return "Virgem"
    elif (mes == 9 and dia >= 23) or (10 <= mes <= 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (11 <= mes <= 11 and dia <= 21):
        return "Escorpião"
    elif (mes == 11 and dia >= 22) or (12 <= mes <= 12 and dia <= 21):
        return "Sagitário"
    elif (mes == 12 and dia >= 22) or (1 <= mes <= 1 and dia <= 19):
        return "Capricórnio"
    elif (mes == 1 and dia >= 20) or (2 <= mes <= 2 and dia <= 18):
        return "Aquário"
    else:
        return "Peixes"

# Entrada
dia = int(input("Digite o dia de seu aniversário (1 a 31): "))
mes = int(input("Agora digite o mês de seu aniversário (1 a 12): "))

# Saída
print(f"Você é do signo de {determinar_signo(mes, dia)}")
