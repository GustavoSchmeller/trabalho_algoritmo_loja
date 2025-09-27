from classe_produto import Produto




def cadastrarProduto():
    print("################# CADASTRAR")
    nome = input("Qual o nome do produto?")
    preco = float(input("Qual o preço do produto?"))
    quantidade = int(input("Qual a quantidade do produto?"))
    
    produto = Produto("","","")
    produto.nome = nome
    produto.preco = preco
    produto.quantidade = quantidade
    
    id = gerarId()
    
    produto.salvar(id)
    return 

def gerarId():
    if Produto.dict_produtos:
        return max(Produto.dict_produtos.keys()) + 1
    else:
        return 1

def verProduto():
    for chave, valor in Produto.dict_produtos.items():
        print(f"Produto ID: {chave}\n- {valor}")
    return


# Iniciando APP

while True:
    print("Escolha uma opção:")
    print("0 - Sair")
    print("1 - Cadastrar produtos")
    print("2 - Ver produtos")
    opcao_selecionada = int(input(": "))
    
    if opcao_selecionada == 0:              # SAIR
        print("\nSaindo do programa...\n")
        break
    elif opcao_selecionada == 1:            # CADASTRAR
        cadastrarProduto()
    elif opcao_selecionada == 2:            # VER PRODUTOS
        verProduto()
    else:
        print("\nOPÇÃO INVÁLIDA.\n")


