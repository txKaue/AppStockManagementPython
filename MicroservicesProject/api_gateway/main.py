# api_gateway/main.py
from fastapi import FastAPI, HTTPException
import httpx
from pydantic import BaseModel

app = FastAPI()

# URLs dos microsserviços
BASE_URL_PRODUTOS = "http://127.0.0.1:8001/products/"
BASE_URL_ESTOQUE = "http://localhost:8002"

# Modelo Pydantic para o Produto
class Produto(BaseModel):
    codigo: int
    nome: str
    quantidade: int
    preco: float

# Rotas de Produtos
@app.post("/products/")
async def create_product(produto: Produto):
    """Cria um novo produto no microsserviço de Produtos"""
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL_PRODUTOS}/products/", json=produto.dict())
        return response.json()

@app.put("/products/{codigo}/add_quantidade")
async def add_quantidade(codigo: int, quantidade: int):
    """Adiciona quantidade ao produto"""
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BASE_URL_PRODUTOS}/products/{codigo}/add_quantidade", json={"quantidade": quantidade})
        return response.json()
    
# exemplo: http://127.0.0.1:8000/products/3/add_quantidade?quantidade=5

@app.put("/products/{codigo}/rem_quantidade")
async def rem_quantidade(codigo: int, quantidade: int):
    """Remove quantidade do produto"""
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BASE_URL_PRODUTOS}/products/{codigo}/rem_quantidade", json={"quantidade": quantidade})
        return response.json()
    
# exemplo: http://127.0.0.1:8001/products/3/rem_quantidade?quantidade=5

@app.delete("/products/{codigo}")
async def delete_product(codigo: int):
    """Deleta um produto pelo código"""
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL_PRODUTOS}/products/{codigo}")
        return response.json()

# Rotas de Estoque
@app.post("/estoque/add_produto/")
async def add_produto(produto: Produto):
    """Adiciona um produto ao estoque"""
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL_ESTOQUE}/estoque/add_produto/", json=produto.dict())
        return response.json()

@app.delete("/estoque/rem_produto/{codigo}")
async def rem_produto(codigo: int):
    """Remove um produto do estoque pelo código"""
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL_ESTOQUE}/estoque/rem_produto/{codigo}")
        return response.json()

@app.get("/estoque/list_produtos/")
async def list_produtos():
    """Lista todos os produtos no estoque"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL_ESTOQUE}/estoque/list_produtos/")
        return response.json()

@app.get("/estoque/buscar_produto/{codigo}")
async def buscar_produto(codigo: int):
    """Busca um produto no estoque pelo código"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL_ESTOQUE}/estoque/buscar_produto/{codigo}")
        return response.json()
