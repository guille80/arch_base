from .base import AlgoritmoBase

class AlgoritmoB():
    def __init__(self, number: int = 10):
        self.number = number

    def doble(self) -> int:
        """Devuelve el doble del número."""
        return self.number * 2

    def run(self, data):
        return f"Procesado por AlgoritmoB: {data}"    