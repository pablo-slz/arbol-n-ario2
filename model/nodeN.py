
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
            # Validar que no se intente cambiar el id
            if new_person.id != id:
                raise ValueError("No se puede cambiar el ID de una persona existente.")

            # Validar que no se intente cambiar el parent_id
            current_parent_id = node.parent.person.id if node.parent else None
            if new_person.parent_id != current_parent_id:
                raise ValueError("No se puede cambiar el padre de una persona existente.")

            # Actualizar los demás datos
            node.person.name = new_person.name
            node.person.age = new_person.age
            node.person.gender = new_person.gender
            node.person.location = new_person.location
            node.person.typedoc = new_person.typedoc
            return True
        return False

    def delete_person(self, id: int) -> bool:
        node_to_delete = self.nodes.get(id)
        if not node_to_delete:
            return False

        # Encontrar hijos del nodo a eliminar
        children = [node for node in self.nodes.values() if node.parent == node_to_delete]

        if node_to_delete.parent is None:
            # El nodo es la raíz
            if children:
                # Elegir el hijo mayor para promoverlo como nueva raíz
                new_root = max(children, key=lambda n: n.person.age)
                new_root.parent = None
                new_root.person.parent_id = None

                # Los demás hijos apuntan al nuevo root
                for child in children:
                    if child != new_root:
                        child.parent = new_root
                        child.person.parent_id = new_root.person.id
            # Si no tiene hijos, simplemente se elimina
        else:
            # El nodo no es la raíz: dejar a sus hijos huérfanos
            for child in children:
                child.parent = None
                child.person.parent_id = None  # ← importante

        # Eliminar el nodo del diccionario
        del self.nodes[id]
        return True

    def get_persons_with_adult_daughter(self) -> List[Person]:
        result = []
        for person_id in self.nodes:
            node = self.nodes[person_id]
            if node.person.gender.lower() == "f" and node.person.age >= 18:
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

    def get_root(self) -> Optional[Person]:
        for node in self.nodes.values():
            if node.parent is None:
                return node.person
        return None  # En caso de que el árbol esté vacío



