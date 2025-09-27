class Produto:
    def __init__( self,nome,preco,quantidade ):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    @property
    def nome( self ):
        return self._nome

    @nome.setter
    def nome( self,produto_nome ):
        self._nome = produto_nome

    @property
    def preco( self ):
        return self._preco
    
    @preco.setter
    def preco( self,produto_preco ):
        self._preco = produto_preco

    @property
    def quantidade( self ):
        return self._preco
    
    @quantidade.setter
    def quantidade( self,produto_quantidade ):
        self._quantidade = produto_quantidade
    

    