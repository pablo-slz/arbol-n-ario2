
from typing import Optional, Dict, List
from model.person import Person

class NodeN:
    def __init__(self, person: Person):
        self.person = person
        self.parent: Optional['NodeN'] = None

class TreeN:
    def __init__(self):
        self.nodes: Dict[int, NodeN] = {}

    def create_person(self, person: Person) -> NodeN:
        if person.id in self.nodes:
            raise ValueError(f"Ya existe una persona con id={person.id}")

        new_node = NodeN(person)

        if person.parent_id is not None:
            parent_node = self.nodes.get(person.parent_id)
            if not parent_node:
                raise ValueError(f"Padre con id={person.parent_id} no encontrado.")
            new_node.parent = parent_node

        self.nodes[person.id] = new_node
        return new_node

    def get_persons(self) -> List[Person]:
        return [node.person for node in self.nodes.values()]

    def update_person(self, id: int, new_person: Person) -> bool:
        node = self.nodes.get(id)
        if node:
            node.person = new_person
            return True
        return False

    def delete_person(self, id: int) -> bool:
        node_to_delete = self.nodes.get(id)
        if node_to_delete:
            # Quitar referencias desde otros nodos
            for node in self.nodes.values():
                if node.parent and node.parent.person.id == id:
                    node.parent = None
            del self.nodes[id]
            return True
        return False

    def get_persons_with_adult_daughter(self) -> List[Person]:
        result = []
        for node in self.nodes.values():
            if node.person.gender.upper() == "F" and node.person.age >= 18:
                if node.parent:
                    result.append(node.parent.person)
        return result

    def filter_by_location_typedoc_gender(self, loc: str, td: str, gr: str) -> List[Person]:
        return [
            node.person for node in self.nodes.values()
            if node.person.location.code == loc
            and node.person.typedoc.value.lower() == td.lower()
            and node.person.gender.lower() == gr.lower()
        ]

    def get_persons_by_location(self, location_code: str) -> List[Person]:
        return [node.person for node in self.nodes.values() if node.person.location.code == location_code]

    def is_empty(self) -> bool:
        return len(self.nodes) == 0



