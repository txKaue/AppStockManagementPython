# api_gateway/main.py
from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

BASE_URL_PRODUTOS = "http://127.0.0.1:8001"
BASE_URL_ESTOQUE = "http://127.0.0.1:8002"

# Rotas de Produtos
@app.post("/products/")
async def create_product(produto: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL_PRODUTOS}/products/", json=produto)
        return response.json()

@app.put("/products/{codigo}/add_quantidade")
async def add_quantidade(codigo: int, quantidade: int):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BASE_URL_PRODUTOS}/products/{codigo}/add_quantidade", json={"quantidade": quantidade})
        return response.json()

@app.put("/products/{codigo}/rem_quantidade")
async def rem_quantidade(codigo: int, quantidade: int):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BASE_URL_PRODUTOS}/products/{codigo}/rem_quantidade", json={"quantidade": quantidade})
        return response.json()

@app.delete("/products/{codigo}")
async def delete_product(codigo: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL_PRODUTOS}/products/{codigo}")
        return response.json()

# Rotas de Estoque
@app.post("/estoque/add_produto/")
async def add_produto(produto: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL_ESTOQUE}/estoque/add_produto/", json=produto)
        return response.json()

@app.delete("/estoque/rem_produto/{codigo}")
async def rem_produto(codigo: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL_ESTOQUE}/estoque/rem_produto/{codigo}")
        return response.json()

@app.get("/estoque/list_produtos/")
async def list_produtos():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL_ESTOQUE}/estoque/list_produtos/")
        return response.json()

@app.get("/estoque/buscar_produto/{codigo}")
async def buscar_produto(codigo: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL_ESTOQUE}/estoque/buscar_produto/{codigo}")
        return response.json()
