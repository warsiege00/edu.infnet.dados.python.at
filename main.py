from funcoes.gerenciar_arquivos import carregar_produtos, salvar_produtos
from funcoes.atendimento import atender_clientes
from funcoes.notas_fiscais import fechar_caixa

def main():

    produtos = carregar_produtos("produtos.csv")
    clientes, total_vendas = atender_clientes(produtos)
    fechar_caixa(clientes, total_vendas, produtos)
    salvar_produtos("produtos.csv", produtos)

if __name__ == "__main__":
    main()