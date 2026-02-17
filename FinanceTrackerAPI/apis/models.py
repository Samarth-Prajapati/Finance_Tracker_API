from pydantic import BaseModel, StrictStr, StrictFloat, Field, field_validator
from typing import List, Optional
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
    title : StrictStr = Field(..., min_length = 3, max_length = 100)
    description : StrictStr = Field(..., max_length = 500)
    amount : StrictFloat = Field(..., gt = 0)
    type : TypeTransaction
    category : StrictStr
    date : datetime.date
    tags : List[str] = Field(..., max_length = 10)
    created_at : datetime.datetime
    updated_at : None

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
    description : StrictStr = Field(..., max_length = 500)
    created_at: datetime.datetime

    class Config:
        orm_mode = True
        use_enum_values = True

class DeleteBulk(BaseModel):
    category : str

    class Config:
        orm_mode = True

    @field_validator("category")
    @classmethod
    def validate_category(cls, value : str):
        if not value.strip():
            raise ValueError("Category cannot be null.")
        return value.lower().strip()

class TransactionModelPatch(BaseModel):
    title : Optional[str] = Field(None, min_length = 3, max_length = 100)
    description : Optional[str] = Field(None, max_length = 500)
    amount : Optional[float] = Field(None, gt = 0)
    type : Optional[TypeTransaction] = None
    category : Optional[str] = None
    tags : Optional[List[str]] = Field(None, max_length = 10)
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

