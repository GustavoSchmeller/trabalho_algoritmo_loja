from valoresGlobais import tamanhosComDesconto

def validarDesconto( validarTamanho ):
    if validarTamanho in tamanhosComDesconto:
        return True
    return False