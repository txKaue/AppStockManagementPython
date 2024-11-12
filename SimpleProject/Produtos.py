class Produtos:
    
    def __init__ (self, codigo, nome, quantidade, preco):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    
    def __str__(self):
        return f"Cod: {self.codigo} | Nome: {self.nome} | Qntd: {self.quantidade} | Preco: {self.preco}"
    
    def cod(self):
        return self.codigo

    def AddQuantidade(self, quantidade):
        self.quantidade += quantidade

    def RemQuantidade(self, quantidade):
        self.quantidade -= quantidade

    def ApagarItem(self):
        del self