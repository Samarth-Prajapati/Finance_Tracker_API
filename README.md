# Personal Finance Tracker API

A FastAPI and MongoDB-based API for managing personal finances.

---
## Features
- **CRUD Operations**: Manage transactions and categories.
- **Search**: Full-text search on transaction titles and descriptions.

---
## Project Structure
```text
FinanceTrackerAPI/
├── .venv/                            # Virtual Environment
├── FinanceTrackerAPI/
│   ├── __init__.py                   # Entry point & FastAPI app
│   ├── apis                          
│   │   ├── __init__.py               # Entry point for FastAPI app
│   │   ├── models.py                 # Pydantic BaseModel
│   │   └── routes.py                 # All API's
│   └── utils                                          
│       ├── __init__.py               # Entry point for db collections
│       ├── db_commands.py            # MongoDB commands for collections
│       └── db_connection.py          # MongoDB connection & client
├── .env                              # Environment variables
├── .gitignore 
├── main.py                           # Main File
├── poetry.lock
├── pyproject.toml 
├── requirements.txt                  # Dependencies                   
└── README.md                         # Documentation
```

---
## Tech Stack

**Python**: 3.13\
**Framework**: [FastAPI](https://fastapi.tiangolo.com)\
**Database**: [MongoDB](https://www.mongodb.com)\
**Validation**: [Pydantic v2](https://docs.pydantic.dev)\
**Server**: Uvicorn

---
## Schema Design & Justification

### Transactions Collection
Chosen for high write throughput and flexible metadata (tags).
- `amount`: Stored as float/decimal to ensure precision.

### Categories Collection
- `name`: Unique index enforced to prevent logical duplicates.
- `type`: Categorized to help frontend UI filter appropriate categories based on the transaction type (Income/Expense/Both).

## Database Indexes

| Index | Type | Purpose |
| :--- | :--- | :--- |
| `date: -1` | Single Field | Optimized for chronological listing (latest first). |
| `{category: 1, date: -1}` | Compound | Optimizes filtering by category while maintaining sort order. |
| `{type: 1, date: -1}` | Compound | Optimizes filtering by income/expense while maintaining sort order. |
| `{title: "text", description: "text"}` | Text | Power `GET /transactions/search` for keyword matching. |
| `name: 1` (Unique) | Single Field | Ensures category names are distinct and allows fast O(1) lookups. |

---
## Getting Started

1.  **Setup Environment**:
    Create a .env file in the root directory:

```env
    MONGO_URI=mongodb://localhost:27017
    DATABASE_NAME=finance_tracker
```
   

2.  **Install Dependencies**:
   
```bash
    poetry install
```   

3.  **Run Application**:
   
```bash
    uvicorn main:app --reload
```  

4.  **API Documentation**:
    View the interactive Swagger UI at [http://127.0.0.1](http://127.0.0.1)
---


## Conclusion
The **Personal Finance Tracker API** is built with a focus on data integrity, high-performance querying, and scalability. By leveraging **MongoDB's Framework** for real-time reporting, this API provides a robust foundation for modern financial applications. 
