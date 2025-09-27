class Produto:
    dict_produtos = {}
    
    def __init__( self ):
        pass
    
    @property
    def nome( self ):
        return self._nome
    
    @property
    def preco( self ):
        return self._preco
    
    @property
    def quantidade( self ):
        return self._quantidade
    
    @property
    def produtoId( self ):
        return self._produtoId
    
    @nome.setter
    def nome( self,produto_nome ):
        if len( produto_nome ) <= 3:
            raise ValueError("O nome do produto deve conter mais do que três caracteres")
        else:        
            self._nome = produto_nome     
    
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
            
    @produtoId.setter
    def produtoId( self,id ):
        self._produtoId = id
    
    def __str__( self ):
        return f"\n- Nome: { self.nome }\n- Preço: R${ self.preco }\n- Quantidade: { self.quantidade }"

    def salvar( self ):
        Produto.dict_produtos[ self._produtoId ]= self
        return
