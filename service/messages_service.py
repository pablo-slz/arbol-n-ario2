import json

class MessageService:
    def __init__(self, file_path="messages.json"):
        with open(file_path, "r", encoding="utf-8") as file:
            self.messages = json.load(file)

    def get(self, key: str) -> str:
        return self.messages.get(key, f"Mensaje no encontrado para: {key}")
