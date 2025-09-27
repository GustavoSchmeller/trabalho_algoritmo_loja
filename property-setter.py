#self é uma referência ao objeto atual da classe.
# É usado para acessar variáveis que pertencem à classe.
#property é um decorador que transforma um método em um atributo.
#setter é um decorador que define um método para definir o valor de um atributo.

#Proteção de atributos com _ (convenção)
#Atributos com _ são considerados "protegidos" e não devem ser acessados diretamente fora da classe.

#atributo - público

#_atributo  protegido (use só dentro da classe ou subclasses)

#__atributo  privado (não acessa direto de fora, somente na classe”).


class Pessoa():
    def __init__(self, nome,idade,email,celular):
        self._nome = nome
        self._idade = idade
        self._email = email
        self._celular = celular
        
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):    
            self._nome = novo_nome

    @property
    def idade(self):
         return self._idade

    @idade.setter
    def idade(self, nova_idade):  
         if nova_idade < 0:
            print("Idade não pode ser negativa.")   
         else:
            self._idade = nova_idade

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):    
            self._email = novo_email

    @property
    def celular(self):
          return self._celular
    
    @celular.setter
    def celular(self, novo_celular):
        self._celular = novo_celular

    def exibir_dados(self):
        print("Exibindo dados da pessoa:")
        print(f'Nome: {self._nome}')
        print(f'Idade: {self._idade}')
        print(f'E-mail: {self._email}')
        print(f'Celular: {self._celular}')   

            
#Criando o objeto pessoa1
nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))
email = input("Digite o e-mail da pessoa: ")
celular = input("Digite o celular da pessoa: ")


pessoa1 = Pessoa(nome, idade, email, celular)

pessoa1.nome = nome
pessoa1.idade = idade
pessoa1.email = email   
pessoa1.celular = celular

print("\nExibindo os dados da pessoa1:")

pessoa1.exibir_dados()


