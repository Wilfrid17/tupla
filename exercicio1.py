

vendas = [1000, 2000, 300, 400]
funcionarios = ["Cris","Mariane","Rose","João"]

for i, venda in enumerate(vendas):
    print("{} vendeu {} unidades".format(funcionarios[i],vendas[i]))