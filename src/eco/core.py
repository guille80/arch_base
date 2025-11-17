# class EcoPlugin:
#     def __init__(self, message: str):
#         self.message = message

#     def echo(self) -> str:
#         """Devuelve el mensaje original."""
#         return self.message

#     def shout(self) -> str:
#         """Devuelve el mensaje en mayúsculas."""
#         return self.message.upper()
    
import importlib.metadata

from eco.algoritmos.algoritmo_a import AlgoritmoA
from eco.algoritmos.algoritmo_b import AlgoritmoB


def cargar_algoritmos():
    algoritmos = {}
    # Carga dinámica de entry points registrados en eco.algoritmos
    eps = importlib.metadata.entry_points()
    for entry_point in eps.select(group="eco.algoritmos"):
        cls = entry_point.load()
        algoritmos[entry_point.name] = cls()

    # Asegurar que algoritmo_a y algoritmo_b siempre estén presentes
    if "algoritmo_a" not in algoritmos:
        algoritmos["algoritmo_a"] = AlgoritmoA()
    if "algoritmo_b" not in algoritmos:
        algoritmos["algoritmo_b"] = AlgoritmoB()

    return algoritmos