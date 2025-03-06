#Exemplo:
#Digamos que você está analisando as vendas do Banco de Dados de um e-commerce.
#Em um determinado dia, você extraiu as vendas do Banco de Dados e elas vieram nesse formato:
vendas = [
    ('20/08/2024', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2024', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2024', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2024', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2024', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2024', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2024', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2024', 'ipad', 'prata', '128gb', 4000, 5000),
]
# Qual foi o faturamento de IPhone no dia 20/08/2024?

faturamento = 0

for venda in vendas:
    data,produto,cor,capacidade, unidades,valor_unitario = venda
    if produto == "iphone x" and data == "20/08/2024":
        faturamento += unidades * valor_unitario
#print(f"O faturamento de iphone no dia 20/08/2024 foi de {faturamento:.2f}")

# Qual foi o produto mais vendido (em unidades) no dia 21/08/2024?

produto_mais_vendido = ''
qtde_produto_mais_vendido = 0
cor_produto_mais_vendida = ''
capacidade_produto_mais_vendida = ''
for venda in vendas:
    data,produto,cor,capacidade, unidades,valor_unitario = venda
    if data == "21/08/2024" and unidades > qtde_produto_mais_vendido:
        produto_mais_vendido = produto
        qtde_produto_mais_vendido = unidades
        cor_produto_mais_vendida = cor
        capacidade_produto_mais_vendida = capacidade

print(f"Meu produto mais vendido no dia 21/08/2024 foi {produto} com {unidades} unidades. Cor: {cor}, Capacidade: {capacidade}")