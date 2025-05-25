'''
1 - definir pergunrtas
2 - system cls
3 - criar laco para exibi-las
4 - responder pergunta
5 - exibir a resposta certa
6 - contador para acertos
7 - numerar perguntas e alternativas
'''
import os

perguntas = [
    {
        "pergunta": "Quanto é 12 x 5?",
        "alternativas": ["24", "36", "60", "72"],
        "resposta": "60"
    },
    {
        "pergunta": "Qual a capital do Brasil?",
        "alternativas": ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"],
        "resposta": "Brasília"
    },
    {
        "pergunta": "Quanto é 7 + 8?",
        "alternativas": ["12", "13", "15", "17"],
        "resposta": "15"
    }
]
acertos = 0

for i, pergunta in enumerate(perguntas, start=1):
    print(f"{i}) {pergunta["pergunta"]}\n")

    opcoes = pergunta["alternativas"]
    for j, alternativa in enumerate(opcoes, start=1):
        print(f"{j}) {alternativa}")

    escolha = input("\nDigite a alternativa correta: ")
    correto = False
    escolha_int = None
    qntd_alternativas = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qntd_alternativas:
            if opcoes[escolha_int - 1] == pergunta["resposta"]:
                correto = True

    os.system("cls")

    if correto:
        print("Você acertou!")
        print(f"Resposta correta: {pergunta["resposta"]}\n")
        acertos += 1
    else:
        print("Resposta errada!")
        print(f"Resposta correta: {pergunta["resposta"]}\n")

print(f"Quantidade de acertos: {acertos}/3\n")