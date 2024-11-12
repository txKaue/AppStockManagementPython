# App Stock Management Using Python and Microservices

I made an simple app to manage stock using Python.
The project actually is two projects. First i made an OOP normal project just to manage stock, then the second project I made it using microservices.

## SimpleProject folder:

This is the folder of the OOP project. We have 3 files:

- main.py : The main file that have to be executed.
- Produtos.py: My class and methods to create and manage a product.
- Stock.py: My class and methods to create and manage a stock.

## Microservices folder:

This is the folder of the Microservices project. We have 3 folder and 1 file at root.

- api_gateway (folder): Folder with the main file of project.
- estoque_service (folder): Folder with the stock services and class.
- produtos_service (folder): Folder with the products services and class.
- requirements.txt: File that have the requirements to be installed.

 To run the microservices you have to run this comand at cmd:

 ```bash
    uvicorn <FolderNameOfService>.main:app --reload
```
### URLs to request:

PRODUTCS:

- Create a product (POST) : http://localhost:8000/products/ and the JSON with a Produto (object)
- Get a product by code (GET) :  http://localhost:8000/products/{item code}
- Add quantity to a product (PUT) : http://localhost:8000/products/add_quantidade?quantidade={quantity you want to add}
- Decrease quantity to a product (PUT) : http://localhost:8000/products/rem_quantidade?quantidade={quantity you want to decrease}
- Delete a product (DELETE) : http://localhost:8000/products/{item code}

STOCK:

- Add a product to stock (POST) : http://localhost:8001/estoque/add_produto/ and a JSON with a item code ( A Produto have to exist )
- List all itens in stock (GET) : http://localhost:8001/estoque/list_produtos/
- Get a product at stock by code (GET) : http://localhost:8001/estoque/buscar_produto/{item code}
- Remove a product from stock (DELETE) : http://localhost:8001/estoque/rem_produto/{item code}









