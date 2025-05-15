from pydantic import BaseModel

class FilterPerson(BaseModel):
    code: str
    typedoc: str
    gender: str
