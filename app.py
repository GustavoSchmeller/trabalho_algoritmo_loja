from valoresGlobais import tamanhos,categorias,produtosArmazenados
from classeProduto import Produto,ProdutoDesconto
from funcValidarDesconto import validarDesconto

# SOLICITA O NOME E FAZ VALIDAÇÕES NO METÓDO
def adicionarMarca( produto:Produto ):
    while True: 
        marcaInformada = input("Qual a marca do produto?\n: ")
        try:
            produto.marca = marcaInformada
            break
        except ValueError as erro:
            print(f"ERRO: { erro }")
    return produto.marca

# SOLICITA O PREÇO E FAZ VALIDAÇÕES NO METÓDO
def adicionarPreco( produto:Produto ):
    while True: 
        precoInformado = input("Qual o preço do produto?\n: ")
        try:
            if validarDesconto( produto.tamanho ):
                produto.preco = precoInformado
                produto.aplicarDesconto()
            else:
                produto.preco = precoInformado
            break
        except ValueError as erro:
            print(f"ERRO: { erro }")
    return produto.preco
    
# SOLICITA O TAMANHO E FAZ VALIDAÇÕES NO METÓDO
def adicionarTamanho( produto:Produto ):
    while True: 
        print("Qual o tamanho do produto?")
        for indice,tamanho in enumerate( tamanhos, start=1 ):
            print(f"({ indice }) - { tamanho }")
        tamanhoInformado = input(": ")        
        try:
            produto.tamanho = tamanhoInformado
            break
        except ValueError as erro:
            print(f"ERRO: { erro }")
    return produto.tamanho

# SOLICITA A CATEGORIA E FAZ VALIDAÇÕES NO METÓDO
def adicionarCategoria( produto:Produto ):
    while True:
        print("Qual a categoria do produto?")
        for indice,tamanho in enumerate( categorias, start=1 ):
            print(f"({ indice }) - { tamanho }")
        categoriaInformada = input(": ")        
        try: 
            produto.categoria = categoriaInformada
            break
        except ValueError as erro:
            print(f"ERRO: { erro }")
    return produto.categoria

# SOLICITA A QUANTIDADE E FAZ VALIDAÇÕES NO METÓDO
def adicionarQuantidade( produto:Produto ):
    while True: 
        quantidadeInformada = input("Qual a quantidade do produto?\n: ")
        try:
            produto.quantidade = quantidadeInformada
            break
        except ValueError as erro:
            print(f"ERRO: { erro }")
    return produto.quantidade

# SOLICITA A DESCRIÇÃO E FAZ VALIDAÇÕES NO METÓDO
def adicionarDescricao( produto:Produto ):
    while True:
        descricaoInformada = input("Dê uma breve descrição do produto. (até 20 caracteres)\n: ")
        try:
            produto.descricao = descricaoInformada
            break
        except ValueError as erro:
            print(f"ERRO: { erro }")
    return produto.descricao

# INICIA O CADASTRO E CHAMA FUNÇÕES PARA VALIDAR
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
    
    if validarDesconto( produto.tamanho ):  
        produto = ProdutoDesconto( produto.produtoId,marca,preco,tamanho,categoria,quantidade,descricao )
    else:
        produto = Produto( produto.produtoId,marca,preco,tamanho,categoria,quantidade,descricao )
    
    confirmacaoParaSalvar = input("Deseja salvar? (Digite 's' para salvar ou qualquer tecla para sair)\n: ")
    if confirmacaoParaSalvar.upper() == "S":
        produto.salvarProduto()
        print("SUCESSO: Produto cadastrado!")
    else:
        print("CANCELADO: Produto não cadastrado.")
        return 

def verProdutos():
    print("==============|VER PRODUTOS")
    if produtosArmazenados:
        for numero,_ in enumerate( produtosArmazenados,start=0 ):
            print(f"\n{ produtosArmazenados[ numero ] }")
        return
    else:
        print("\n(Não há produtos cadastrados)")

def editarProdutos1():                          
    print("==============|EDITAR PRODUTOS")
    if produtosArmazenados:
        while True:

            
                produtoEncontrado = ""
                while True:
                    try: 
                        editarSelecao = int(input("\nQual produto você deseja editar? (Informe o ID)\n: "))
                        idSelecionado = editarSelecao
                        break
                    except ValueError:
                        print("ERRO: O valor digitado não é um inteiro") 
                
                # Caso o ID for um numero valido...
                if idSelecionado:   
                    # Valida se o ID é referente a um produtoID que existe
                    for produto in produtosArmazenados:
                        if produto.produtoId == idSelecionado:
                            produtoEncontrado = produto
                    # Caso o produto for encontrado...
                    if produtoEncontrado:
                            while True:
                                print(f"==============|PRODUTO ID #{ idSelecionado }\n")
                                produtoEncontrado.mostrarItensProduto()
                                try:
                                    print(f"==============|PRODUTO ID #{ idSelecionado }\n")
                                    produtoEncontrado.mostrarItensProduto()
                                    opcao = int(input(f"\nO que deseja editar desse produto? (Digite o numero referente ao item)\n: "))
                                    if opcao == 1:
                                        adicionarPreco( produtoEncontrado )
                                        break
                                    elif opcao == 2:
                                        adicionarQuantidade( produtoEncontrado )
                                        break
                                    elif opcao == 3:
                                        adicionarDescricao( produtoEncontrado )
                                        break
                                    else:
                                        print("ERRO: A opção escolhida não existe\n") 
                                        break
                                except:
                                    print("ERRO: O valor digitado não é um numero inteiro") 
                            print("SUCESSO: Item editado com sucesso!")

                            continuarEditando = str(input("Deseja editar mais algum item do seu produto? (Digite 's' para continuar ou qualquer tecla para sair)\n: "))
                            if continuarEditando.upper() == "S":
                                pass
                            else:
                                break
                            
                    # Caso o produto referente ao ID não for encontrado...
                    else:
                        print("ERRO: O ID digitado não existe")
                else:
                    print("ERRO: O ID digitado não existe")
            #break

    else:
        print("\n(Não há produtos cadastrados)")

def editarProdutos():
    print("==============|EDITAR PRODUTOS")
    if produtosArmazenados:
        continuarEditando = True
        produtoSelecionado = ""
        produtoEncontrado = ""

        while continuarEditando == True:
            for produto in produtosArmazenados:
                print(f"\n{ produto }")

            while True:
                try:
                    produtoSelecionado = int(input("Qual produto deseja editar? (Digite o ID)\n: ")) 
                    break
                except:
                    print("ERRO: O valor digitado não é um numero inteiro")

            
            for produto in produtosArmazenados:
                if produto.produtoId == produtoSelecionado:
                    produtoEncontrado = produto
            
            if produtoEncontrado:
                print(f"==============|PRODUTO ID SELECIONADO = #{ produtoEncontrado.produtoId }\n")
                produtoEncontrado.mostrarItensProduto()

                opcao = int(input(f"\nO que deseja editar desse produto? (Digite o numero referente ao item)\n: "))
                if opcao == 1:
                    adicionarPreco( produtoEncontrado )
                elif opcao == 2:
                    adicionarQuantidade( produtoEncontrado )
                elif opcao == 3:
                    adicionarDescricao( produtoEncontrado )
                else:
                    print("ERRO: A opção escolhida não existe\n")

                continuarEditando = str(input("Deseja editar mais algum item do seu produto? (Digite 's' para continuar ou qualquer tecla para sair)\n: "))
                if continuarEditando.upper() == "S":
                    pass
                else:
                    continuarEditando = False
            else:
                print("ERRO: O ID selecionado não é referente a um produto")



            
            

    else:
       print("\n(Não há produtos cadastrados)") 

def apagarProdutos():
    print("==============|APAGAR PRODUTOS")
    if produtosArmazenados:
        for produto in produtosArmazenados:
            print(f"\n{ produto }")
        while True:
            idParaApagar = input("Qual produto deseja apagar?\n: ")
            try:
                idParaApagarInt = int(idParaApagar)
                for produto in produtosArmazenados:
                    if produto.produtoId == idParaApagarInt:
                        produtosArmazenados.remove(produto)
                        produtoApagado = True
                        break
                    else:
                        produtoApagado = False
                if produtoApagado: 
                    print("SUCESSO: Produto apagado com sucesso!")
                    continuarEditando = str(input("Deseja apagar mais algum produto? (Digite 's' para continuar ou qualquer tecla para sair)\n: "))
                    if continuarEditando.upper() == "S":
                        if not produtosArmazenados:
                            print("ERRO: Não há mais produtos para apagar.")
                            break
                        pass
                    else:
                        break 
                else:
                    print("ERRO: Produto não encontrado.")
            except ValueError:
                print("ERRO: O valor digitado não é um inteiro")
    else:
        print("\n(Não há produtos cadastrados para apagar)")


# Iniciando APP - Loja de roupa

while True:
    print("\nEscolha uma opção:")
    print("0 - Sair")
    print("1 - Cadastrar Produtos")
    print("2 - Ver Produtos")
    print("3 - Editar Produtos   --   AJUSTAR ESTÁ EM LOOPING")
    print("4 - Apagar Produtos")
    
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
        elif opcaoSelecionada == 4:
            apagarProdutos()
        else:
            print("\nERRO: opção inválida.\n")
        
    except ValueError:
        print("\nERRO: opção inválida.\n")
    



