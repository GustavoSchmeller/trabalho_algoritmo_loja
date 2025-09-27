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

    while True: # PEGAR E VALIDAR TAMANHO
        tamanhos = ("PP", "P", "M", "G", "GG", "XG", "XGG", "EG")
        print("Qual o tamanho do produto?")
        for indice,tamanho in enumerate( tamanhos, start=1 ):
            print(f"({ indice }) - { tamanho }")
        tamanho = input(": ")        
        try:
            produto.tamanho = tamanho
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
    
    confirmacao = input("Deseja salvar? (Digite 'sim' para salvar ou qualquer tecla para sair)\n:")
    if confirmacao.upper() == "SIM":
        produto.salvar()
        print("SUCESSO: Produto cadastrado!")
    else:
        print("CANCELADO: Produto não cadastrado.")
        return 

def gerarId():
    if Produto.produtosArmazenados:
        return len(Produto.produtosArmazenados) + 1
    else:
        return 1

def verProdutos():
    print("==============|PRODUTOS")
    if Produto.produtosArmazenados:
        for produto in Produto.produtosArmazenados:
            print(f"\n{ produto }")
        return
    else:
        print("\n(Não há produtos cadastrados)")


# Iniciando APP - Loja de roupa

while True:
    print("\nEscolha uma opção:")
    print("0 - Sair")
    print("1 - Cadastrar Produtos")
    print("2 - Ver Produtos")
    
    try:
        opcaoSelecionada = int(input(": "))      
        if opcaoSelecionada == 0:              # SAIR
            print("\nSaindo do programa...\n")
            break
        elif opcaoSelecionada == 1:            # CADASTRAR
            cadastrarProduto()
        elif opcaoSelecionada == 2:            # VER PRODUTOS
            verProdutos()
        else:
            print("\nOPÇÃO INVÁLIDA.\n")
        
    except ValueError:
        print("\nOPÇÃO INVÁLIDA.\n")
    



