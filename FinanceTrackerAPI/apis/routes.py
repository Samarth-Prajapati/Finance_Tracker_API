from fastapi import FastAPI, status, HTTPException
from FinanceTrackerAPI.apis import TransactionModel, DeleteBulk, TransactionModelPatch, CategoryModel, CategoryModelPatch
from FinanceTrackerAPI.utils import transactions_commands, categories_commands

app = FastAPI()

@app.post("/transactions", status_code = status.HTTP_201_CREATED, tags = ["Transactions"])
def create_transactions(data : TransactionModel):
    transactions_commands.create_transactions(data.model_dump())
    return {"message" : "Transactions created successfully."}

@app.get("/transactions/search", status_code = status.HTTP_200_OK, tags = ["Transactions"])
def search_transactions_list(query: str):
    if not query:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST)

    data = transactions_commands.search_transactions(query)
    if not data:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST)

    return [transaction for transaction in data]

@app.get("/transactions", status_code = status.HTTP_200_OK, tags = ["Transactions"])
def get_transactions():
    data = transactions_commands.get_transactions()
    return [transaction for transaction in data]

@app.delete("/transactions/bulk", status_code = status.HTTP_204_NO_CONTENT, tags = ["Transactions"])
def delete_transaction_bulk(model : DeleteBulk):
    transactions_commands.delete_transaction_bulk(model.category)
    return None

@app.post("/categories", status_code = status.HTTP_201_CREATED, tags = ["Categories"])
def create_categories(data : CategoryModel):
    categories_commands.create_categories(data.model_dump(mode = "json"))
    return {"message" : "Categories created successfully."}

@app.get("/categories", status_code = status.HTTP_200_OK, tags = ["Categories"])
def get_categories():
    data = categories_commands.get_categories()
    return [category for category in data]

@app.get("/transactions/{id}", status_code = status.HTTP_200_OK, tags = ["Transactions"])
def get_transactions_id(obj_id):
    data = transactions_commands.get_transactions_id(obj_id)
    return data

@app.patch("/transactions/{id}", status_code = status.HTTP_202_ACCEPTED, tags = ["Transactions"])
def update_transaction(obj_id, data : TransactionModelPatch):
    updated_data = data.model_dump(exclude_unset = True, mode = "json")

    if not updated_data:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST)

    updated = transactions_commands.update_transaction(obj_id, updated_data)
    return updated

@app.delete("/transactions/{id}", status_code = status.HTTP_204_NO_CONTENT, tags = ["Transactions"])
def delete_transaction(obj_id):
    transactions_commands.delete_transaction(obj_id)
    return None

@app.delete("/categories/{name}", status_code = status.HTTP_204_NO_CONTENT, tags = ["Categories"])
def delete_categories(name):
    categories_commands.delete_category(name)
    return None

@app.patch("/categories/{name}", status_code = status.HTTP_202_ACCEPTED, tags = ["Categories"])
def update_categories(name, data : CategoryModelPatch):
    updated_data = data.model_dump(exclude_unset = True)

    if not updated_data:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST)

    updated = categories_commands.update_category(name, updated_data)
    return updated