def multiplicar(*args):
    total = 1
    for num in args:
        total *= num
    return total

def par_impar(x):
    multiplo_de_dois = x % 2 == 0
    if multiplo_de_dois:
        return f"{x} é par"
    return f"{x} é ímpar"  # else não é necessário

multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(multiplicacao)
print(par_impar(3))
