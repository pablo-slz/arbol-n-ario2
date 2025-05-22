from pydantic import BaseModel

class Location(BaseModel):
    code: str
    description: str