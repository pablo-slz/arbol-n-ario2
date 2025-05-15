from model.nodeN import TreeN
from model.person import Person
from typing import List

tree = TreeN()

def create_person(person: Person):
    return tree.create_person(person)

def list_persons() -> List[Person]:
    return tree.get_persons()

def update_person(person_id: int, new_data: Person) -> bool:
    return tree.update_person(person_id, new_data)

def delete_person(person_id: int) -> bool:
    return tree.delete_person(person_id)

def get_persons_by_conditions(location_code: str, type_doc: str, gender: str) -> List[Person]:
    return tree.filter_by_location_typedoc_gender(location_code, type_doc, gender)

def get_persons_by_location(location_code: str) -> List[Person]:
    return tree.get_persons_by_location(location_code)

def get_parents_with_adult_daughters() -> List[Person]:
    return tree.get_persons_with_adult_daughter()


