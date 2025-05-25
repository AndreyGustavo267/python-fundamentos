nome = input("Digite seu primeiro nome: ")
tamanho = len(nome)

if tamanho > 1:
    if tamanho <= 4:
        print("Seu nome eh curto")
    elif tamanho >= 5 and tamanho <= 6:
        print("Seu nome tem tamanho normal")
    else:
        print("Seu nome eh grande")
else:
    print("Digite mais de uma letra")