# produtos_service/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Produto(BaseModel):
    codigo: int
    nome: str
    quantidade: int
    preco: float

products = {}

@app.post("/products/")
def create_product(produto: Produto):
    if produto.codigo in products:
        raise HTTPException(status_code=400, detail="Produto já existe")
    products[produto.codigo] = produto
    return produto

@app.put("/products/{codigo}/add_quantidade")
def add_quantidade(codigo: int, quantidade: int):
    if codigo not in products:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    products[codigo].quantidade += quantidade
    return products[codigo]

@app.put("/products/{codigo}/rem_quantidade")
def rem_quantidade(codigo: int, quantidade: int):
    if codigo not in products:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    if products[codigo].quantidade < quantidade:
        raise HTTPException(status_code=400, detail="Quantidade insuficiente")
    products[codigo].quantidade -= quantidade
    return products[codigo]

@app.delete("/products/{codigo}")
def delete_product(codigo: int):
    if codigo not in products:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    del products[codigo]
    return {"detail": "Produto excluído com sucesso"}
