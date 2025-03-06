# 1. Análise de Vendas
#Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.

#Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam.

meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]

for vendedor, qtde in vendas:
    if qtde > meta:
        print(f"{vendedor} bateu a meta, vendeu {qtde} unidades.")


#Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano de 2022 mais vendas do que no ano de 2023, para reportar isso para a diretoria.

# Sua resposta pode ser um print de cada produto, qual foi a venda de 2023, a venda de 2024 e o % de crescimento de 2020 para 2023.

# Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer: (vendas_produto2024/vendas_produto2013 - 1)

# A lógica da tupla é: (produto, vendas2023, vendas2024)

vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]

#seu código aqui
for produto, vendas2023,vendas2024 in vendas_produtos:
    if vendas2024 > vendas2023:
        crescimento = vendas2024 / vendas2023 - 1
        print(f"{produto} teve {vendas2023} vendas em 2023, é {vendas2024} vendas em 2024. teve um Crescimento de {crescimento:.1%}")