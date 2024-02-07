# schemas.py

from pydantic import BaseModel, PositiveInt
from typing import Optional

class PetsSchema(BaseModel):
    id: PositiveInt
    name: str
    species: Optional[str] = None
    age: PositiveInt
    owner: str

class Error(BaseModel):
    detail: str
