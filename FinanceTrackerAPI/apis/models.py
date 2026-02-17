from pydantic import BaseModel, StrictStr, StrictFloat, Field, field_validator, StrictInt
from typing import List
import datetime
from enum import Enum

class TypeTransaction(Enum):
    income = "income"
    expense = "expense"

class TypeCategory(Enum):
    income = "income"
    expense = "expense"
    both = "both"

class TransactionModel(BaseModel):
    title : StrictStr = Field(min_length = 3, max_length = 100)
    description : StrictStr = Field(max_length = 500)
    amount : StrictFloat = Field(gt = 0)
    type : TypeTransaction
    category : StrictStr
    date : datetime.date
    tags : List[StrictStr] = List[Field(max_length = 10)]
    created_at : datetime.datetime
    updated_at : datetime.datetime

    class Config:
        orm_mode = True
        use_enum_values = True

    @field_validator("title")
    @classmethod
    def strip_title(cls, value):
        return value.strip()

    @field_validator("category")
    @classmethod
    def validate_category(cls, value):
        if not value:
            raise ValueError("Category cannot be null.")
        return value.lower()

    @field_validator("tags")
    @classmethod
    def validate_tags(cls, value):
        for tag in value:
            if len(tag) > 30:
                raise ValueError("Tags cannot be more than 30 characters.")

class CategoryModel(BaseModel):
    name : StrictStr
    type : TypeCategory
    description : StrictStr = Field(max_length = 500)
    created_at: datetime.datetime

    class Config:
        orm_mode = True
        use_enum_values = True


