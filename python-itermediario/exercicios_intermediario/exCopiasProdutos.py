import copy

# Lista dos produtos
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
def alterar_precos(produtos, chave_preco):
    novos_produtos = copy.deepcopy(produtos)
    for p in novos_produtos:
        p[chave_preco] *= 1.10
    return novos_produtos

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
def ordenar_nome_decrescente(produtos, chave_nome):
    produtos_ordenados_por_nome = copy.deepcopy(produtos)
    produtos_ordenados_por_nome.sort(key=lambda p: p[chave_nome], reverse=True)
    return produtos_ordenados_por_nome

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
def ordenar_preco_crescente(produtos, chave_preco):
    produtos_ordenados_por_preco = copy.deepcopy(produtos)
    produtos_ordenados_por_preco.sort(key=lambda p: p[chave_preco])
    return produtos_ordenados_por_preco

# Função para exibição dos produtos
def exibir_lista(produtos):
    for p in produtos:
        print(f"Nome: {p["nome"]}, Preço: R$ {p["preco"]:.2f}")
    print("\n")

# Chamada das funções
novos_produtos = alterar_precos(produtos, "preco")
exibir_lista(novos_produtos)

produtos_ordenados_por_nome = ordenar_nome_decrescente(produtos, "nome")
exibir_lista(produtos_ordenados_por_nome)

produtos_ordenados_por_preco = ordenar_preco_crescente(produtos, "preco")
exibir_lista(produtos_ordenados_por_preco)