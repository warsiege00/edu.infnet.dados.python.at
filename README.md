# Sistema de caixa de supermercado

O AT proposto deve implementar um caixa de supermercado de forma que o operador do caixa insira os produtos e as quantidades e, ao final, exiba uma “nota fiscal” com os itens comprados e o total da compra. Ao final do programa, deverá ser exibido um extrato com o total das vendas do caixa. Considere que existe apenas um caixa operando no supermercado

## Funcionalidades

- Atendimento ao cliente, registrando os produtos comprados.
- Geração de nota fiscal com detalhes da compra.
- Relatório de vendas com o total acumulado e produtos sem estoque.

## Tecnologias

- **Python**
- **Tabulate** para exibir dados em formato de tabela.
- **CSV** para carregar e salvar produtos.

## Como Usar

1. Instale as dependências:  
   ```bash
   pip3 install tabulate
2.	Inicie o atendimento digitando ‘I’ e registre os produtos comprados.
3.	Finalize o caixa digitando ‘F’ para ver o relatório de vendas.


## Melhorias

1. Problema com múltiplos caixas

- Se mais de um caixa estiver operando, pode haver inconsistências no estoque devido ao acesso simultâneo ao arquivo.

2. Solução

- Implementar persistência em um banco de dados com controle de concorrência.