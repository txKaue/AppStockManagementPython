from Produtos import *
from Stock import *

# Criando o estoque

stk = Stock()

# Criando alguns produtos

p1 = Produtos(1, "Camisa", 12, 35.90)
p2 = Produtos(2, "Bermuda", 6, 20.80)
p3 = Produtos(3, "Tenis", 21, 120.99)
p4 = Produtos(4, "Meia", 16, 12.50)

# Adicionando no estoque

stk.AddProduto(p1)
stk.AddProduto(p2)
stk.AddProduto(p3)
stk.AddProduto(p4)

# Mostrando o estoque

stk.ListProdutos()

# Buscando um produto pelo codigo

stk.BuscarProduto(2) #Vai encontrar
stk.BuscarProduto(5) #Não vai encontrar

