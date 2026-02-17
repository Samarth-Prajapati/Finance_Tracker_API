from fastapi import FastAPI, status
from FinanceTrackerAPI.apis import TransactionModel
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