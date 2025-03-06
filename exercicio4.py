"""
Exerecicio: Escreve uma função que receber uma lista de tuplas.
Cada tupla contém dois itens: um nome de produto e seu preço.
A função deve retorna o nome do produto mais cara e o mais barato.
"""
def econtra_produto_min_max(lista_produtos):
    produto_min = produto_max = lista_produtos[0]

    for produto in lista_produtos[1:]:
        if produto[1] < produto_min[1]:
            produto_min = produto
        if produto[1] > produto_max[1]:
            produto_max = produto
    return produto_min , produto_max

produtos = [("arroz", 10),("feijão",5),("macarrão",3),("carne",20)]
print(econtra_produto_min_max(produtos))