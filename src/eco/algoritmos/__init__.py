from .loader import cargar_algoritmos

__all__ = ["cargar_algoritmos"]
# import importlib.metadata

# def cargar_algoritmos():
#     algoritmos = {}
#     for entry_point in importlib.metadata.entry_points(group="eco.algoritmos"):
#         cls = entry_point.load()
#         algoritmos[entry_point.name] = cls()
#     return algoritmos