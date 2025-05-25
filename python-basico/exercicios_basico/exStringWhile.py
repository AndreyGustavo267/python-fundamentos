nome = "Luiz Henrique"
tamanho = len(nome)
i = 0
novo_nome = "*"
while i < tamanho:
    novo_nome += nome[i] + "*"
    i += 1
print(novo_nome)