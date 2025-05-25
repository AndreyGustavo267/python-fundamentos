hora = input("Digite o horário: ")

try:
    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print("Bom dia!")

    elif hora >= 12 and hora <= 17:
        print("Bom tarde!")

    elif hora >= 18 and hora <= 23:
        print("Bom noite!")
    else:
        print("Horario invalido")
except:
    print("Por favor, digite apenas numeros inteiros.")