from .base import AlgoritmoBase

class AlgoritmoA(AlgoritmoBase):
    def __init__(self, message: str = "Hola desde Algoritmo A"):
        self.message = message

    def echo(self) -> str:
        """Devuelve el mensaje original."""
        return self.message
    
    def run(self, data):
        return data

