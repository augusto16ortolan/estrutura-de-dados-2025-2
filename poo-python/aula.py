
class Pessoa:

    _teste = "Teste"

    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def apresentar(self):
        print(f"Oi, meu nome é {self.nome} e tenho {self.idade} anos.")

    def retornarAnoDeNascimento(self):
        return 2025 - self.idade
    
    def getTeste(self):
        return self._teste
    
    def setGenero(self, genero):
        self.genero = genero

class Marca:

    def __init__(self, nome):
        self.nome = nome 

class Produto:

    def __init__(self, nome, preco, marca):
        self.nome = nome
        self.preco = preco
        self.marca = marca

    def retornarMarca(self):
        return self.marca
    
produto = Produto("Notebook", 2000, Marca("Dell"))
marca = produto.retornarMarca()
print(marca.nome)

produto2 = Produto("Notebook", 10000, Marca("Avell"))
marca2 = produto2.retornarMarca()
print(marca2)


pessoa1 = Pessoa("Augusto", 20, "Masculino")
pessoa1.apresentar()
print(pessoa1.getTeste())
print(pessoa1.genero)
anoNascimento = pessoa1.retornarAnoDeNascimento()
print(anoNascimento)
pessoa1.genero = "M"
print(pessoa1.genero)