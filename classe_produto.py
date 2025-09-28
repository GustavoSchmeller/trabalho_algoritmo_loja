class Produto:
    produtosArmazenados = []
    categorias = ("Camiseta", "Camisa", "Blusa", "Regata")

    def __init__( self,produtoID,marca,preco,tamanho,categoria,quantidade,descricao ):
        self.produtoId = produtoID
        self._marca = marca
        self._preco = preco
        self._tamanho = tamanho
        self._categoria = categoria
        self._quantidade = quantidade
        self._descricao = descricao
    
    @property
    def marca( self ):
        return self._marca
    
    @property
    def preco( self ):
        return self._preco
    
    @property
    def tamanho( self ):
        return self._tamanho
    
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def quantidade( self ):
        return self._quantidade
    
    @property
    def produtoId( self ):
        return self._produtoId
    
    @property
    def descricao( self ):
        return self._descricao
    
    @property
    def precoDesconto( self ):
        return self._precoDesconto
    
    @marca.setter
    def marca( self,produto_marca ):
        if len( produto_marca ) <= 3:
            raise ValueError("O nome do produto deve conter mais do que três caracteres")
        else:        
            self._marca = produto_marca.upper()
    
    @preco.setter
    def preco( self,produto_preco ):
        try:
            precoValido = float( produto_preco )
        except ValueError:
            raise ValueError("O valor informado não é um numero ou está formatado incorretamente")
        if precoValido <= 0:
            raise ValueError("O valor informado não pode ser menor ou igual a zero")
        else:
            self._preco = precoValido
    
    @tamanho.setter
    def tamanho( self,produto_tamanho ):
        tamanhos = ("PP", "P", "M", "G", "GG", "XG", "XGG", "EG")
        try:
            tamanhoValido = int( produto_tamanho )
            if tamanhoValido < 1 or tamanhoValido > len( tamanhos ):
                raise ValueError("O valor informado deve ser entre 1 e 8")
            else:
                for indice,tamanho in enumerate( tamanhos, start=1 ):
                    if indice == tamanhoValido:
                        self._tamanho = tamanho
        except ValueError:
            raise ValueError("O valor informado é inválido")
    
    @categoria.setter
    def categoria( self,produto_categoria ):
        categorias = ("Camiseta", "Camisa", "Blusa", "Regata")
        try:
            categoriaValido = int( produto_categoria )
            if categoriaValido < 1 or categoriaValido > len( categorias ):
                raise ValueError("")
            else:
                for indice,categor in enumerate(categorias, start=1):
                    if indice == categoriaValido:
                        self._categoria = categor
        except ValueError:
            raise ValueError("A categoria deve ser um numero inteiro")
    
    @quantidade.setter
    def quantidade( self,produto_quantidade ):
        try: 
            quantidadeValido = int( produto_quantidade )
        except ValueError:
            raise ValueError("A quantidade deve ser um numero inteiro")
        if quantidadeValido <= 0:
            raise ValueError("A quantidade deve ser maior que zero")
        else:
            self._quantidade = quantidadeValido
            
    @descricao.setter
    def descricao( self, produto_descricao ):
        if len(produto_descricao) == 0 or len(produto_descricao) < 4:
            raise ValueError("Nenhuma descrição do produto ou descrição muito pequena")
        elif len(produto_descricao) > 20:
            raise ValueError("Você excedeu o numero de caracteres")
        else:
            self._descricao = produto_descricao
            
    @produtoId.setter
    def produtoId( self,produto_id ):
        self._produtoId = produto_id
    
    def __str__( self ):
        return (f"#ID: { self.produtoId }"
                f"\n- Marca: { self.marca }"
                f"\n- Preço: R$ { self.preco }"
                f"\n- Tamanho: { self.tamanho }"
                f"\n- Categoria: { self.categoria }"
                f"\n- Quantidade: { self.quantidade }"
                f"\n- Descrição: { self.descricao }")
    
    def gerarIdProduto():
        if Produto.produtosArmazenados:
            return len(Produto.produtosArmazenados) + 1
        else:
            return 1

    def salvarProduto( self ):
        Produto.produtosArmazenados.append( self )
        return
    
    def mostrarProdutos():
        for produto in Produto.produtosArmazenados:
            print(f"\n{ produto }")
            
    def mostrarItensProduto( self ):
        print(f"(1) - Marca: { self.marca }\n"
            f"(2) - Preço: { self.preco }\n"
            f"(3) - Tamanho: { self.tamanho }\n"
            f"(4) - Categoria: { self.categoria }\n"
            f"(5) - Quantidade: { self.quantidade }\n"
            f"(6) - Descrição: { self.descricao }")

    
class ProdutoDesconto(Produto):
    def __init__( self,produtoID,marca,preco,tamanho,categoria,quantidade,descricao ):
        super().__init__( produtoID,marca,preco,tamanho,categoria,quantidade,descricao )
        self.aplicarDesconto()
        
    def aplicarDesconto( self ):
        if self.tamanho == "PP":
            self._preco = self.preco - (self.preco * 0.2) 
            
    def __str__( self ):
        return (f"#ID: { self.produtoId }"
                f"\n- Marca: { self.marca }"
                f"\n- Preço: R$ { self.preco } (desconto aplicado)"
                f"\n- Tamanho: { self.tamanho } (possui 20% de desconto)"
                f"\n- Categoria: { self.categoria }"
                f"\n- Quantidade: { self.quantidade }"
                f"\n- Descrição: { self.descricao }")