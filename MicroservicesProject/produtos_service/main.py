# produtos_service/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modelo Pydantic para o Produto
class Produto(BaseModel):
    codigo: int
    nome: str
    quantidade: int
    preco: float

# Dicionário para armazenar os produtos
products = {}

# Criação de um produto
@app.post("/products/")
def create_product(produto: Produto):
    """Cria um produto, se não existir já"""
    if produto.codigo in products:
        raise HTTPException(status_code=400, detail="Produto já existe")
    products[produto.codigo] = produto
    return produto

# Adiciona quantidade ao produto existente
@app.put("/products/{codigo}/add_quantidade")
def add_quantidade(codigo: int, quantidade: int):
    """Adiciona a quantidade especificada ao produto"""
    if codigo not in products:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    products[codigo].quantidade += quantidade
    return products[codigo]

# Remove quantidade do produto existente
@app.put("/products/{codigo}/rem_quantidade")
def rem_quantidade(codigo: int, quantidade: int):
    """Remove a quantidade especificada do produto"""
    if codigo not in products:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    produto = products[codigo]  # Verifique o produto
    print(f"Produto antes de remover: {produto}")
    if produto.quantidade < quantidade:
        raise HTTPException(status_code=400, detail="Quantidade insuficiente")
    produto.quantidade -= quantidade
    print(f"Produto depois de remover: {produto}")
    return produto


# Deleta o produto pelo código
@app.delete("/products/{codigo}")
def delete_product(codigo: int):
    """Deleta um produto pelo código"""
    if codigo not in products:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    del products[codigo]
    return {"detail": "Produto excluído com sucesso"}

