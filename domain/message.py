from dataclasses import dataclass

@dataclass
class Message:
    origem: str
    payload: dict
