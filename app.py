from classe_produto import Produto


def cadastrarProduto():
    print("==============|CADASTRAR")
    produto = Produto()

    while True: # PEGAR E VALIDAR NOME
        nome = input("Qual o nome do produto?\n: ")
        try:
            produto.nome = nome
            break
        except ValueError as erro:
            print(f"ERRO: { erro }")

    while True: # PEGAR E VALIDAR PREÇO
        preco = input("Qual o preço do produto?\n: ")
        try:
            produto.preco = preco
            break
        except ValueError as erro:
            print(f"ERRO: { erro }")

    
    while True: # PEGAR E VALIDAR QUANTIDADE
        quantidade = input("Qual a quantidade do produto?\n: ")
        try:
            produto.quantidade = quantidade
            break
        except ValueError as erro:
            print(f"ERRO: { erro }")
            
    produto.produtoId = gerarId()
    produto.salvar()
    return 

def gerarId():
    if Produto.dict_produtos:
        return max(Produto.dict_produtos.keys()) + 1
    else:
        return 1

def verProduto():
    for chave, valor in Produto.dict_produtos.items():
        print(f"Produto ID: { chave }{ valor }")
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


