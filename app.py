from valoresGlobais import tamanhos,categorias,produtosArmazenados,idsArmazenados,usuarios
from classeProduto import Produto,ProdutoDesconto
from funcValidarDesconto import validarDesconto
import os

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
    limparTerminal()
    print("==============|CADASTRAR PRODUTOS")
    produto = Produto("","","","","","","")

    marca = adicionarMarca( produto )
    preco = adicionarPreco( produto )
    tamanho = adicionarTamanho( produto )
    
    categoria = adicionarCategoria( produto )
    quantidade = adicionarQuantidade( produto )
    descricao = adicionarDescricao( produto )
    
    confirmacaoParaSalvar = input("Deseja salvar? (Digite 's' para salvar ou qualquer tecla para sair)\n: ")
    if confirmacaoParaSalvar.upper() == "S":
        produto.produtoId = Produto.gerarIdProduto()
        if validarDesconto( produto.tamanho ):     
            produto = ProdutoDesconto( produto.produtoId,marca,preco,tamanho,categoria,quantidade,descricao )
        else:
            produto = Produto( produto.produtoId,marca,preco,tamanho,categoria,quantidade,descricao )
        produto.salvarProduto()
        print("SUCESSO: Produto cadastrado!")
    else:
        print("CANCELADO: Produto não cadastrado.")
        return 

# MOSTRA TODOS PRODUTOS CADASTRADOS PARA O USUÁRIO
def verProdutos():
    limparTerminal()
    print("==============|VER PRODUTOS")
    if produtosArmazenados:
        for produto in produtosArmazenados:
            print(f"\n{ produto }")
        return
    else:
        print("\n(Não há produtos cadastrados)")

# POSSIBILITA O USUÁRIO EDITAR OS ITENS DOS PRODUTOS
def editarProdutos():
    limparTerminal()
    print("==============|EDITAR PRODUTOS")
    if produtosArmazenados:
        continuarEditando = True

        while continuarEditando == True:
            try: 
                for produto in produtosArmazenados:
                    print(f"\n{produto}")
                    
                idSelecionado = int(input("\nQual produto você deseja editar? (Informe o ID)\n: "))
                produtoExistente = False
                produtoSelecionado = ""
                
                for produto in produtosArmazenados:
                    if produto.produtoId == idSelecionado:
                        produtoSelecionado = produto
                        produtoExistente = True
                    else:
                        produtoExistente = False
    
                if not produtoExistente:
                    print("ERRO: O ID digitado não existe")
                else:
                    print(f"==============|PRODUTO ID #{produtoSelecionado.produtoId}\n")
                    while True:
                        try:
                            while True:
                                produtoSelecionado.mostrarItensProduto()
                                opcao = int(input(f"\nO que deseja editar desse produto? (Digite o numero referente ao item)\n: "))             
                                if opcao == 1:
                                    adicionarPreco( produtoSelecionado )
                                    break
                                elif opcao == 2:
                                    adicionarQuantidade( produtoSelecionado )
                                    break
                                elif opcao == 3:
                                    adicionarDescricao( produtoSelecionado )
                                    break
                                else:
                                    print("ERRO: A opção escolhida não existe")                                
                            continuarEditando = str(input("Deseja editar mais algum item do seu produto? (Digite 's' para continuar ou qualquer tecla para sair)\n: "))
                            if continuarEditando.upper() == "S":
                                pass
                            else:
                                print("SUCESSO: Produto editado!")
                                continuarEditando = False 
                                break
                        except ValueError:
                            print("ERRO: O valor digitado não é um inteiro")
                #break
            except ValueError:
                print("ERRO: O valor digitado não é um inteiro")        
    else:
        print("\n(Não há produtos cadastrados)")
        
# POSSIBILITA O USUÁRIO APAGAR OS PRODUTOS
def apagarProdutos():
    limparTerminal()
    print("==============|APAGAR PRODUTOS")
    if produtosArmazenados:

        while True:
            for produto in produtosArmazenados:
                print(f"\n{ produto }")
            idParaApagar = input("Qual produto deseja apagar? (Digite o ID do produto)\n: ")
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

# FAZ A LIMPEZA DO TERMINAL
def limparTerminal():
    os.system('cls')



#------------------ Iniciando APP - Loja de roupa

limparTerminal()
# ADICIONADO UM PRODUTO PARA INICIO
produtosArmazenados.append(ProdutoDesconto(1,"Vans",119.99,"M","Camiseta",43,"Camiseta preta com figuras"))
idsArmazenados.append(1)
continuarNoApp = True

while continuarNoApp == True:
    print("==============|LOGIN")
    usuarioInput = input("Usuário: ")
    senhaInput = input("Senha: ")
    usuarioNaoExiste = False
    
    for usuario,senha in usuarios.items():
        if usuarioInput == usuario:
            if senhaInput == senha:
                usuarioNaoExiste = False
                limparTerminal()
                print(f"Olá, { usuario }. Seja bem-vindo!")
                while True:
                    print("\n==============|MENU\n")
                    print("Escolha uma opção:")
                    print("0 - Sair")
                    print("1 - Cadastrar Produtos")
                    print("2 - Ver Produtos")
                    print("3 - Editar Produtos")
                    print("4 - Apagar Produtos")
                    
                    try:
                        opcaoSelecionada = int(input(": "))      
                        if opcaoSelecionada == 0:              # SAIR
                            print("\nSaindo do programa...\n")
                            continuarNoApp = False
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
        else:
            usuarioNaoExiste = True
        
        if usuarioNaoExiste:
            limparTerminal()
            print("ERRO: Usuário não existe ou senha incorreta")


    



