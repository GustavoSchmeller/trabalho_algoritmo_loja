from valoresGlobais import tamanhos,categorias,produtosArmazenados,tamanhosComDesconto
from classe_produto import Produto,ProdutoDesconto
from func_validarDesconto import validarDesconto



def adicionarMarca( produto:Produto ):
    while True: # PEGAR E VALIDAR NOME
        marca = input("Qual a marca do produto?\n: ")
        try:
            produto.marca = marca
            break
        except ValueError as erro:
            print(f"ERRO: { erro }")
    return produto.marca

def adicionarPreco( produto:Produto ):
    while True: # PEGAR E VALIDAR PREÇO
        preco = input("Qual o preço do produto?\n: ")
        try:
            if validarDesconto( produto.tamanho ):
                produto.preco = preco
                produto.aplicarDesconto()
            else:
                produto.preco = preco
            break
        except ValueError as erro:
            print(f"ERRO: { erro }")
    return produto.preco
    
def adicionarTamanho( produto:Produto ):
    while True: # PEGAR E VALIDAR TAMANHO
        print("Qual o tamanho do produto?")
        for indice,tamanho in enumerate( tamanhos, start=1 ):
            print(f"({ indice }) - { tamanho }")
        tamanho = input(": ")        
        try:
            produto.tamanho = tamanho
            break
        except ValueError as erro:
            print(f"ERRO: { erro }")
    return produto.tamanho

def adicionarCategoria( produto:Produto ):
    while True:
        print("Qual a categoria do produto?")
        for indice,tamanho in enumerate( categorias, start=1 ):
            print(f"({ indice }) - { tamanho }")
        categoria = input(": ")        
        try: 
            produto.categoria = categoria
            break
        except ValueError as erro:
            print(f"ERRO: { erro }")
    return produto.categoria

def adicionarQuantidade( produto:Produto ):
    while True: # PEGAR E VALIDAR QUANTIDADE
        quantidade = input("Qual a quantidade do produto?\n: ")
        try:
            produto.quantidade = quantidade
            break
        except ValueError as erro:
            print(f"ERRO: { erro }")
    return produto.quantidade

def adicionarDescricao( produto:Produto ):
    while True:
        descricao = input("Dê uma breve descrição do produto. (até 20 caracteres)\n: ")
        try:
            produto.descricao = descricao
            break
        except ValueError as erro:
            print(f"ERRO: { erro }")
    return produto.descricao

def cadastrarProdutos():
    print("==============|CADASTRAR PRODUTOS")
    produto = Produto("","","","","","","")

    marca = adicionarMarca( produto )
    preco = adicionarPreco( produto )
    tamanho = adicionarTamanho( produto )
    categoria = adicionarCategoria( produto )
    quantidade = adicionarQuantidade( produto )
    descricao = adicionarDescricao( produto )
                         
    produto.produtoId = Produto.gerarIdProduto()
    
    if validarDesconto( produto.tamanho ):                                         # DESCONTO NÃO ESTÁ SENDO APLICADO DEPOIS DE EDITAR - VERIFICAR 
        produto = ProdutoDesconto( produto.produtoId,marca,preco,tamanho,categoria,quantidade,descricao )
    else:
        produto = Produto( produto.produtoId,marca,preco,tamanho,categoria,quantidade,descricao )
    
    confirmacao = input("Deseja salvar? (Digite 's' para salvar ou qualquer tecla para sair)\n: ")
    if confirmacao.upper() == "S":
        produto.salvarProduto()
        print("SUCESSO: Produto cadastrado!")
    else:
        print("CANCELADO: Produto não cadastrado.")
        return 

def verProdutos():
    print("==============|VER PRODUTOS")
    if produtosArmazenados:
        for numero,_ in enumerate( produtosArmazenados,start=0 ):
            print(f"\n{produtosArmazenados[numero]}")
        return
    else:
        print("\n(Não há produtos cadastrados)")

def editarProdutos():
    print("==============|EDITAR PRODUTOS")
    if produtosArmazenados:
        for produto in produtosArmazenados:
            print(f"\n{produto}")
        while True:
            try: 
                editarSelecao = int(input("\nQual produto você deseja editar? (Informe o ID)\n: "))
                id = editarSelecao -1
                if editarSelecao < 1 or editarSelecao > len( produtosArmazenados ):
                    print("ERRO: O ID digitado não existe")
                else:
                    while True:
                        print(f"==============|PRODUTO ID #{id+1}\n")
                        try:
                            produtosArmazenados[ id ].mostrarItensProduto()
                            while True:
                                opcao = int(input(f"\nO que deseja editar desse produto? (Digite o numero referente ao item)\n: "))
                                #if opcao == x:
                                #    adicionarMarca( produtosArmazenados[ id ] )  
                                #    break              
                                if opcao == 1:
                                    adicionarPreco( produtosArmazenados[ id ] )
                                    break
                                #elif opcao == x:
                                #    adicionarTamanho( produtosArmazenados[ id ] )
                                #    break
                                #elif opcao == x:
                                #    adicionarCategoria( produtosArmazenados[ id ] )
                                #    break
                                elif opcao == 2:
                                    adicionarQuantidade( produtosArmazenados[ id ] )
                                    break
                                elif opcao == 3:
                                    adicionarDescricao( produtosArmazenados[ id ] )
                                    break
                                else:
                                    print("ERRO: A opção escolhida não existe")                                
                            continuarEditando = str(input("Deseja editar mais algum item do seu produto? (Digite 's' para continuar ou qualquer tecla para sair)\n: "))
                            if continuarEditando.upper() == "S":
                                pass
                            else:
                                print("SUCESSO: Produto editado!")
                                break 
                        except ValueError:
                            print("ERRO: O valor digitado não é um inteiro")
                break
            except ValueError:
                print("ERRO: O valor digitado não é um inteiro")
        
        
        
    else:
        print("\n(Não há produtos cadastrados)")

# Iniciando APP - Loja de roupa

while True:
    print("\nEscolha uma opção:")
    print("0 - Sair")
    print("1 - Cadastrar Produtos")
    print("2 - Ver Produtos")
    print("3 - Editar Produtos")
    
    try:
        opcaoSelecionada = int(input(": "))      
        if opcaoSelecionada == 0:              # SAIR
            print("\nSaindo do programa...\n")
            break
        elif opcaoSelecionada == 1:            # CADASTRAR
            cadastrarProdutos()
        elif opcaoSelecionada == 2:            # VER PRODUTOS
            verProdutos()
        elif opcaoSelecionada == 3:            # EDITAR PRODUTOS
            editarProdutos()
        else:
            print("\nERRO: opção inválida.\n")
        
    except ValueError:
        print("\nERRO: opção inválida.\n")
    



