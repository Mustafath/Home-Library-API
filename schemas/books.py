from pydantic import BaseModel, Field
from datetime import date


class SBookBase(BaseModel):
    title: str = Field(max_length=50)
    author: str = Field(max_length=50)
    description: str = Field(None, max_length=300)
    publication_date: date
    pages: int = Field(..., lt=3500)
    is_read: bool = False


class SBookAdd(SBookBase):
    ...


class SBook(SBookBase):
    id: int


class SBookUpdate(BaseModel):
    title: str = Field(..., max_length=50)
    author: str = Field(..., max_length=50)
    description: str = Field(..., max_length=300)
    publication_date: date
    pages: int = Field(..., lt=3500)
    is_read: bool = False


class SBookPatch(BaseModel):
    title: str = Field(None, max_length=50)
    author: str = Field(None, max_length=50)
    description: str = Field(None, max_length=300)
    publication_date: date = None
    pages: int = Field(None, lt=3500)
    is_read: bool = None