# Exercícios Python - Manipulação de Dados

Este repositório contém uma coleção de scripts Python que demonstram diferentes técnicas de manipulação de dados, estruturas de dados e análise de informações comerciais. Os exercícios são voltados para iniciantes e intermediários em Python, com foco em aplicações práticas de conceitos fundamentais.

## Estrutura do Projeto

O projeto contém quatro arquivos principais:

- `exercicio.py`: Demonstra manipulação básica de tuplas
- `exercicio1.py`: Demonstra o uso de listas e a função `enumerate()`
- `exercicio2.py`: Análise de dados de vendas de e-commerce com desempacotamento de tuplas
- `exercicio3.py`: Análise de metas de vendas e comparação de vendas entre períodos

## Detalhamento dos Exercícios

### exercicio.py

Este script demonstra como acessar elementos individuais de uma tupla. A tupla `vendas` contém informações de um funcionário:

```python
vendas = ('Massouco','24/02/2025','13/02/1993', 2000,'Estagio')
```

O script extrai e atribui cada elemento da tupla a variáveis específicas (nome, data de contratação, data de nascimento, salário e cargo) e imprime o cargo.

### exercicio1.py

Este exercício demonstra como iterar através de duas listas simultaneamente usando a função `enumerate()`:

```python
vendas = [1000, 2000, 300, 400]
funcionarios = ["Cris","Mariane","Rose","João"]
```

O script associa cada funcionário com sua respectiva venda e imprime uma mensagem formatada para cada par.

### exercicio2.py

Este script realiza análise de dados de vendas de um e-commerce. Os dados estão estruturados como uma lista de tuplas, onde cada tupla contém informações de uma venda:

```python
vendas = [
    ('20/08/2024', 'iphone x', 'azul', '128gb', 350, 4000),
    # mais entradas...
]
```

O script realiza duas análises:
1. Calcula o faturamento total de iPhones em uma data específica
2. Identifica o produto mais vendido em uma data específica, incluindo detalhes como cor e capacidade

### exercicio3.py

Este exercício contém duas análises de vendas:

1. **Análise de Meta de Vendedores**: Identifica quais vendedores ultrapassaram uma meta de vendas predefinida.
   ```python
   meta = 10000
   vendas = [
       ('João', 15000),
       # mais vendedores...
   ]
   ```

2. **Comparação de Vendas Anuais**: Compara as vendas de produtos entre 2023 e 2024, calculando o percentual de crescimento para produtos que tiveram aumento nas vendas.
   ```python
   vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ...]
   ```

## Como Usar

1. Clone este repositório:
   ```
   git clone https://github.com/seu-usuario/python-exercises.git
   ```

2. Navegue até o diretório do projeto:
   ```
   cd python-exercises
   ```

3. Execute qualquer um dos scripts:
   ```
   python exercicio.py
   python exercicio1.py
   python exercicio2.py
   python exercicio3.py
   ```

## Conceitos Demonstrados

- Manipulação de tuplas e listas
- Estruturas de iteração com `for`
- Desempacotamento de tuplas
- Função `enumerate()`
- Formatação de strings com f-strings
- Formatação de números para exibição de porcentagens
- Condicionais com `if`
- Cálculos básicos (soma, multiplicação, divisão)
- Análise simples de dados

## Contexto de Aplicação

Estes exercícios simulam cenários comuns de análise de dados em um ambiente de negócios, como:
- Gestão de informações de funcionários
- Acompanhamento de vendas por vendedor
- Análise de performance de produtos em e-commerce
- Comparação de desempenho entre períodos
- Verificação de metas comerciais

## Requisitos

- Python 3.6 ou superior
