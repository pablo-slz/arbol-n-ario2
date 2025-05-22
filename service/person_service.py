from model.nodeN import TreeN
from model.person import Person
from typing import List
from typing import Optional

tree = TreeN()

def create_person(person: Person):
    return tree.create_person(person)

def list_persons() -> List[Person]:
    return tree.get_persons()

def update_person(person_id: int, new_data: Person) -> bool:
    return tree.update_person(person_id, new_data)

def delete_person(person_id: int) -> bool:
    return tree.delete_person(person_id)

def get_persons_by_conditions(location_code: Optional[str], typedoc_code: Optional[str], gender: Optional[str]) -> List[Person]:
    return tree.filter_by_location_typedoc_gender(location_code, typedoc_code, gender)

def get_persons_by_location(location_code: str) -> List[Person]:
    return tree.get_persons_by_location(location_code)

def get_parents_with_adult_daughters() -> List[Person]:
    return tree.get_persons_with_adult_daughter()

def get_root_person() -> Optional[Person]:
    return tree.get_root()

def get_persons_by_typedoc(typedoc: str) -> List[Person]:
    persons = tree.get_persons()
    return [p for p in persons if p.typedoc.value.lower() == typedoc.lower()]


