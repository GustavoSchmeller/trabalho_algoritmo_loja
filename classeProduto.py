from valoresGlobais import tamanhos,categorias,produtosArmazenados,idsArmazenados,tamanhosComDesconto

class Produto:

    def __init__( self,produtoID,marca,preco,tamanho,categoria,quantidade,descricao ):
        self.produtoId = produtoID
        self._marca = marca
        self._preco = preco
        self._tamanho = tamanho
        self._categoria = categoria
        self._quantidade = quantidade
        self._descricao = descricao
    
    def __str__( self ):
        return (f"#ID: { self.produtoId }"
                f"\n- Marca: { self.marca }"
                f"\n- Preço: R$ { self.preco }"
                f"\n- Tamanho: { self.tamanho }"
                f"\n- Categoria: { self.categoria }"
                f"\n- Quantidade: { self.quantidade }"
                f"\n- Descrição: { self.descricao }") 
    
    @property
    def produtoId( self ):
        return self._produtoId
    
    @produtoId.setter
    def produtoId( self,inserirId ):
        self._produtoId = inserirId

    def gerarIdProduto():
        if produtosArmazenados:
            proximoId = len(idsArmazenados) + 1
            idsArmazenados.append(proximoId)
            return proximoId
        else:
            idsArmazenados.append(1)
            return 1
            
    @property
    def marca( self ):
        return self._marca

    @marca.setter
    def marca( self,nomeInformado ):
        if len( nomeInformado ) <= 3:
            raise ValueError("O nome do produto deve conter mais do que três caracteres")
        self._marca = nomeInformado.upper()

    @property
    def preco( self ):
        return self._preco

    @preco.setter
    def preco( self,precoInformado ):      
        try:
            precoValidado = float( precoInformado )
        except ValueError:
            raise ValueError("O valor informado não é um numero ou está formatado incorretamente")
        if precoValidado <= 0:
            raise ValueError("O valor informado não pode ser menor ou igual a zero")
        self._preco = round( precoValidado,2 )
    
    @property
    def tamanho( self ):
        return self._tamanho

    @tamanho.setter
    def tamanho( self,tamanhoInformado ):
        try:
            tamanhoValidado = int( tamanhoInformado )
        except ValueError:
            raise ValueError("O valor informado é inválido")
        if tamanhoValidado < 1 or tamanhoValidado > len( tamanhos ):
            raise ValueError("O valor informado deve ser entre 1 e 8")
        for indice,tamanho in enumerate( tamanhos, start=1 ):
            if indice == tamanhoValidado:
                self._tamanho = tamanho

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria( self,categoriaInformada ):
        try:
            categoriaValidada = int( categoriaInformada )
        except ValueError:
            raise ValueError("A categoria deve ser um numero inteiro")
        if categoriaValidada < 1 or categoriaValidada > len( categorias ):
            raise ValueError("A categoria informada não existe")
        for indice,categoriaDeCategorias in enumerate(categorias, start=1):
            if indice == categoriaValidada:
                self._categoria = categoriaDeCategorias
    
    @property
    def quantidade( self ):
        return self._quantidade

    @quantidade.setter
    def quantidade( self,quantidadeInformada ):
        try: 
            quantidadeValidada = int( quantidadeInformada )
        except ValueError:
            raise ValueError("A quantidade deve ser um numero inteiro")
        if quantidadeValidada <= 0:
            raise ValueError("A quantidade deve ser maior que zero")
        self._quantidade = quantidadeValidada

    @property
    def descricao( self ):
        return self._descricao

    @descricao.setter
    def descricao( self,descricaoInformada ):
        if len( descricaoInformada ) == 0 or len( descricaoInformada ) < 4:
            raise ValueError("Nenhuma descrição do produto ou descrição muito pequena")
        elif len(descricaoInformada) > 20:
            raise ValueError("Você excedeu o numero de caracteres")
        self._descricao = descricaoInformada

    def salvarProduto( self ):
        produtosArmazenados.append( self )
        return
    
    def mostrarProdutos():
        for produto in produtosArmazenados:
            print(f"\n{ produto }")
            
    def mostrarItensProduto( self ):
        print(f"(-) - Marca: { self.marca }\n"
            f"(1) - Preço: { self.preco }\n"
            f"(-) - Tamanho: { self.tamanho }\n"
            f"(-) - Categoria: { self.categoria }\n"
            f"(2) - Quantidade: { self.quantidade }\n"
            f"(3) - Descrição: { self.descricao }\n")
            
    
class ProdutoDesconto( Produto ):
    def __init__( self,produtoID,marca,preco,tamanho,categoria,quantidade,descricao ):
        super().__init__( produtoID,marca,preco,tamanho,categoria,quantidade,descricao )
        self.aplicarDesconto()
        
    def aplicarDesconto( self ):
        if self.tamanho in tamanhosComDesconto:
            precoDesconto = self.preco - (self.preco * 0.2) 
            self._preco = round( precoDesconto,2 )
            
    def __str__( self ):
        return (f"#ID: { self.produtoId }"
                f"\n- Marca: { self.marca }"
                f"\n- Preço: R$ { self.preco } (desconto aplicado)"
                f"\n- Tamanho: { self.tamanho } (possui 20% de desconto)"
                f"\n- Categoria: { self.categoria }"
                f"\n- Quantidade: { self.quantidade }"
                f"\n- Descrição: { self.descricao }")