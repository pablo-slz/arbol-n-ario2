import csv
from model.location import Location
from typing import List, Dict

class LocationService:
    def __init__(self):
        self.locations: List[Location] = []
        self._load_locations_from_csv()

    def _load_locations_from_csv(self):
        import os
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(base_dir, "docs", "DIVIPOLA-_C_digos_municipios_20250430.csv")

        with open(csv_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                code = row["Código Municipio"]
                description = f"{row['Nombre Municipio']} ({row['Nombre Departamento']})"
                self.locations.append(Location(code=code, description=description))

    def get_states(self) -> Dict[str, str]:
        states = {}
        for loc in self.locations:
            state_code = loc.code[:2]
            if state_code not in states:
                states[state_code] = loc.description.split(" (")[1][:-1]
        return states

    def get_location_by_code(self, code: str) -> Location:
        for loc in self.locations:
            if loc.code == code:
                return loc
        return None

    def get_locations_by_state_code(self, state_code: str) -> List[Location]:
        return [loc for loc in self.locations if loc.code.startswith(state_code)]

    def get_capitals(self) -> List[Location]:
        return [loc for loc in self.locations if loc.code.endswith("001")]


