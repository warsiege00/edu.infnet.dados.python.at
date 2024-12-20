def validar_produto(id_produto, produtos):
    for produto in produtos:
        if produto['id'] == id_produto:
            return True
    return False

def validar_quantidade(quantidade):
    if quantidade > 0:
        return True
    return False