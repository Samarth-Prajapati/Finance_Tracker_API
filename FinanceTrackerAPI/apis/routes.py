from fastapi import FastAPI, status, HTTPException
from FinanceTrackerAPI.apis import TransactionModel, DeleteBulk, TransactionModelPatch
from FinanceTrackerAPI.utils import transactions_commands

app = FastAPI()

@app.post("/transactions", status_code = status.HTTP_201_CREATED, tags = ["Transactions"])
def create_transactions(data : TransactionModel):
    transactions_commands.create_transactions(data.model_dump(mode = "json"))
    return {"message" : "Transactions created successfully."}

@app.get("/transactions", status_code = status.HTTP_200_OK, tags = ["Transactions"])
def get_transactions():
    data = transactions_commands.get_transactions()
    return [transaction for transaction in data]

@app.get("/transactions/{id}", status_code = status.HTTP_200_OK, tags = ["Transactions"])
def get_transactions_id(obj_id):
    data = transactions_commands.get_transactions_id(obj_id)
    return data

@app.delete("/transactions/bulk", status_code = status.HTTP_204_NO_CONTENT, tags = ["Transactions"])
def delete_transaction_bulk(model : DeleteBulk):
    transactions_commands.delete_transaction_bulk(model.category)
    return None

@app.delete("/transactions/{id}", status_code = status.HTTP_204_NO_CONTENT, tags = ["Transactions"])
def delete_transaction(obj_id):
    transactions_commands.delete_transaction(obj_id)
    return None

@app.patch("/transactions/{id}", status_code = status.HTTP_202_ACCEPTED, tags = ["Transactions"])
def update_transaction(obj_id, data : TransactionModelPatch):
    updated_data = data.model_dump(exclude_unset = True)

    if not updated_data:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST)

    updated = transactions_commands.update_transaction(obj_id, updated_data)
    return updated
