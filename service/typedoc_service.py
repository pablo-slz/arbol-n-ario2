from model.typedoc import TypeDoc
from typing import List

class TypeDocService:
    def get_all(self) -> List[TypeDoc]:
        return list(TypeDoc)