# estoque_service/main.py
from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

# URL do serviço de produtos
BASE_URL_PRODUTOS = "http://127.0.0.1:8000/products/"

# Lista para armazenar os produtos no estoque (somente códigos)
estoque = []

# Adiciona um produto ao estoque (deve existir no serviço de produtos)
@app.post("/estoque/add_produto/")
async def add_produto(produto: dict):
    # Verifica se o produto já existe no estoque
    if produto['codigo'] in estoque:
        raise HTTPException(status_code=400, detail="Produto já está no estoque")
    
    # Verifica se o produto existe no serviço de produtos
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL_PRODUTOS}{produto['codigo']}")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Produto não encontrado no serviço de produtos")
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Erro ao verificar o produto no serviço de produtos")
    
    # Se o produto estiver no serviço de produtos, adiciona ao estoque
    estoque.append(produto['codigo'])
    return {"detail": "Produto adicionado ao estoque", "produto": produto}

# Remove um produto do estoque
@app.delete("/estoque/rem_produto/{codigo}")
async def rem_produto(codigo: int):
    if codigo not in estoque:
        raise HTTPException(status_code=404, detail="Produto não encontrado no estoque")
    
    # Remove o produto do estoque
    estoque.remove(codigo)
    
    # Tenta remover o produto também do serviço de produtos
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL_PRODUTOS}{codigo}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Erro ao remover o produto no serviço de produtos")
    
    return {"detail": "Produto removido do estoque"}

# Lista todos os produtos no estoque
@app.get("/estoque/list_produtos/")
async def list_produtos():
    produtos_estoque = []
    for codigo in estoque:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL_PRODUTOS}{codigo}")
            if response.status_code == 404:
                produtos_estoque.append({"codigo": codigo, "detail": "Produto não encontrado"})
            else:
                produtos_estoque.append(response.json())
    return {"produtos": produtos_estoque}

# Busca um produto específico no estoque
@app.get("/estoque/buscar_produto/{codigo}")
async def buscar_produto(codigo: int):
    if codigo not in estoque:
        raise HTTPException(status_code=404, detail="Produto não encontrado no estoque")
    
    # Busca o produto no serviço de produtos
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL_PRODUTOS}{codigo}")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Produto não encontrado no serviço de produtos")
        return response.json()
