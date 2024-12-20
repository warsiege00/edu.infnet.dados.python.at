from tabulate import tabulate

def fechar_caixa(clientes, total_vendas, produtos):
    # Relatório de Vendas
    print("\n--- Relatório de Vendas ---")
    vendas_tabela = []
    for cliente in clientes:
        vendas_tabela.append([f"Cliente {cliente['cliente']}", f"R$ {cliente['total']:.2f}"])

    print(tabulate(vendas_tabela, headers=["Cliente", "Total de Compra"], tablefmt="grid"))
    print(f"\nTotal de vendas: R$ {total_vendas:.2f}")

    # Produtos sem Estoque
    print("\n--- Produtos sem Estoque ---")
    sem_estoque = []
    for produto in produtos:
        if produto['quantidade'] == 0:
            sem_estoque.append([produto['id'], produto['nome']])

    print(tabulate(sem_estoque, headers=["ID", "Nome do Produto"], tablefmt="grid"))