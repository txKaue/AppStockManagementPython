# estoque_service/main.py
from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

BASE_URL_PRODUTOS = "http://127.0.0.1:8001/products/"

estoque = []

@app.post("/estoque/add_produto/")
async def add_produto(produto: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL_PRODUTOS, json=produto)
        if response.status_code == 400:
            raise HTTPException(status_code=400, detail="Produto já existe")
        estoque.append(produto['codigo'])
    return produto

@app.delete("/estoque/rem_produto/{codigo}")
async def rem_produto(codigo: int):
    if codigo not in estoque:
        raise HTTPException(status_code=404, detail="Produto não encontrado no estoque")
    estoque.remove(codigo)
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL_PRODUTOS}{codigo}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Erro ao remover o produto")
    return {"detail": "Produto removido do estoque"}

@app.get("/estoque/list_produtos/")
async def list_produtos():
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL_PRODUTOS)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Erro ao listar produtos")
        produtos = response.json()
    return {"produtos": produtos}

@app.get("/estoque/buscar_produto/{codigo}")
async def buscar_produto(codigo: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL_PRODUTOS}{codigo}")
        if response.status_code == 404:
            return {"detail": "Produto não encontrado"}
        return response.json()
