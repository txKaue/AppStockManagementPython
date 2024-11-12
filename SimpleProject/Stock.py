class Stock:

    def __init__ (self):
        self.produtos = []
    
    def AddProduto(self, Produto):
        self.produtos.append(Produto)

    def RemProduto(self, Produto):
        self.produtos.append(Produto)

    def ListProdutos(self):
        for i in self.produtos:
            print(i)

    def BuscarProduto(self, codigo):
        for i in self.produtos:
            if i.cod() == codigo:
                print(i)
                return i
        print("Item não encontrado")