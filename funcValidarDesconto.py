from valoresGlobais import tamanhoseDescontos

def validarDesconto( validarTamanho ):
    for tamanho,_ in tamanhoseDescontos.items():
        if tamanho == validarTamanho:
            return True
    return False