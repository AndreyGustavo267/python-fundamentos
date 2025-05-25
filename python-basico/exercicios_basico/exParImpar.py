numero = input("Digite um numero inteiro: ")
if numero.isdigit():
    if int(numero) % 2 == 0:
        print("Numero digitado eh um inteiro par")
    else:
        print("Numero digitado eh um inteiro impar")
else:
    print("Nao eh um numero inteiro")