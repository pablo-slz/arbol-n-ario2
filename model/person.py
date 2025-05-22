from pydantic import BaseModel
from typing import Optional

from model.typedoc import TypeDoc
from model.location import Location

class Person(BaseModel):
    id: int
    name: str
    last_name: str
    age: int
    gender: str
    typedoc: TypeDoc
    location: Location
    parent_id: Optional[int] = None
