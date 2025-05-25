# ===== Validacao do primeiro digito =====
import sys
import random

print("======= Validação de CPF =======")
cpf = input("Digite o CPF: ")
# 746.824.890-70
# 390.886.600-69

'''
===== Gerar CPF =====
nove_digitos = ""
for j in range(9):
    nove_digitos += str(random.randint(0, 9))
'''

num_cpf = ""
soma_1 = 0
regressivo_1 = 10

# Remove caracteres que nao sejam numeros
for i in cpf:
    if i.isdigit():
        num_cpf += i
nove_cpf = num_cpf[:9]

# Verifica se há repetição de dígitos
repetido = num_cpf == num_cpf[0] * len(num_cpf)
if repetido:
    print("Você enviou dados sequenciais. CPF inválido.")
    sys.exit()

# Realiza o algoritmo de multiplicacao e soma
for numero_1 in nove_cpf:
    soma_1 += int(numero_1) * regressivo_1
    regressivo_1 -= 1

# Descobre o primeiro digito
digito_1 = (soma_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# ===== Validacao do segundo digito =====
dez_cpf = num_cpf[:9] + str(digito_1)
regressivo_2 = 11
soma_2 = 0

for numero_2 in dez_cpf:
    soma_2 += int(numero_2) * regressivo_2
    regressivo_2 -= 1

digito_2 = (soma_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

# ===== Exibir resultado =====
if digito_1 == int(num_cpf[9]) and digito_2 == int(num_cpf[10]):
    print(f"1° e 2° digitos VALIDADOS, final do CPF é {digito_1}{digito_2}")
else:
    print(f"O CPF eh INVÁLIDO, posto que os digitos finais estão incorretos")