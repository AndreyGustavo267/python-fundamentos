nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"Seu nome eh {nome}")
    print(f"Seu nome invertido eh {nome[::-1]}")
    if " " in nome:
        print("Seu nome contem espacos")
    else:
        print("Seu nome nao contem espacos")
    tamanho = len(nome)
    print(f"Seu nome contem {tamanho} letras")
    print(f"A primeira letra do seu nome eh {nome[0]}")
    print(f"A ultima letra do seu nome eh {nome[-1]}")
else:
    print("Desculpa, voce deixou campos vaazios")