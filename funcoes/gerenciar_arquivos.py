import csv

def carregar_produtos(caminho):
    produtos = []
    arquivo = open(caminho, newline='', encoding='utf-8')
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        produto = {
            'id': int(linha['id']),
            'nome': linha['nome'],
            'quantidade': int(linha['quantidade']),
            'preco': float(linha['preco'])
        }
        produtos.append(produto)
    arquivo.close()
    return produtos

def salvar_produtos(caminho, produtos):
    arquivo = open(caminho, mode='w', newline='', encoding='utf-8')
    escritor = csv.DictWriter(arquivo, fieldnames=['id', 'nome', 'quantidade', 'preco'])
    escritor.writeheader()
    for produto in produtos:
        escritor.writerow(produto)
    arquivo.close()