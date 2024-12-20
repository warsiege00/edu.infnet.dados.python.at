from funcoes.validacoes import validar_produto, validar_quantidade
from tabulate import tabulate

def atender_clientes(produtos):
    clientes = []
    total_vendas = 0
    cliente_num = 1

    while True:
        print(f"\nCliente {cliente_num}")
        opcao = input("Digite 'I' para iniciar atendimento ou 'F' para finalizar o caixa: ").strip().upper()

        if opcao == 'F':
            break
        elif opcao == 'I':
            itens = []
            total_cliente = 0

            while True:
                try:
                    id_produto = int(input("ID do produto: "))
                    quantidade = int(input("Quantidade: "))
                except ValueError:
                    print("Erro: Digite um número válido para ID e Quantidade.")
                    continue

                if not validar_produto(id_produto, produtos):
                    print("Erro: produto não cadastrado.")
                    continue
                if not validar_quantidade(quantidade):
                    print("Erro: quantidade deve ser maior que zero.")
                    continue

                produto = None
                for p in produtos:
                    if p['id'] == id_produto:
                        produto = p
                        break

                if produto is None:
                    print("Erro: produto não encontrado.")
                    continue

                if produto['quantidade'] < quantidade:
                    print("Erro: quantidade em estoque insuficiente.")
                    continue

                preco_total = quantidade * produto['preco']
                itens.append({
                    'id': id_produto,
                    'nome': produto['nome'],
                    'quantidade': quantidade,
                    'preco_unitario': produto['preco'],
                    'preco_total': preco_total
                })

                produto['quantidade'] -= quantidade
                total_cliente += preco_total

                continuar = input("Adicionar mais itens? (S/N): ").strip().upper()
                if continuar == 'N':
                    break

            # Exibe a Nota Fiscal de forma organizada com tabulate
            print(f"\nNota Fiscal do Cliente {cliente_num}")
            headers = ["ID", "Produto", "Quantidade", "Preço Unitário", "Preço Total"]
            table = []
            for item in itens:
                table.append([item['id'], item['nome'], item['quantidade'], f"R$ {item['preco_unitario']:.2f}", f"R$ {item['preco_total']:.2f}"])

            # Usando tabulate para formatar a exibição da tabela
            print(tabulate(table, headers=headers, tablefmt="grid"))
            print(f"\nTotal: R$ {total_cliente:.2f}\n")

            clientes.append({'cliente': cliente_num, 'total': total_cliente})
            total_vendas += total_cliente
            cliente_num += 1
        else:
            print("Opção inválida. Tente novamente.")

    return clientes, total_vendas