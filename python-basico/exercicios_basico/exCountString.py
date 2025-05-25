frase = "Frase de teste para o exercício, objetivando calcular a frequência de cada caractere nessa String, por meio do método count"
i = 0
qntd_max = 0
letra_max = ""

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == " ":
        i += 1
        continue

    qntd_max_atual = frase.count(letra_atual)

    if qntd_max <= qntd_max_atual:
        qntd_max =  qntd_max_atual
        letra_max = letra_atual

    i += 1

print(f'A letra mais frequente foi "{letra_max}", aparecendo um total de {qntd_max} vezes.')
