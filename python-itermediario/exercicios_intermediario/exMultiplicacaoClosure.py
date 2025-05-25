def criar_multiplicador(multiplicador):
    def multiplicacao(numero):
        return numero * multiplicador
    return multiplicacao

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5))