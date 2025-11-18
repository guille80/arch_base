from eco import *
from eco.avanzadas.estadisticas import cuadrado, suma_secreta

# Pruebas de visibilidad de funciones importadas desde eco
# Prueba de reverse_text (descomentada para evitar error de importación)
# s = reverse_text("eco")
# print(s)
# Prueba de suma y resta sí deben funcionar
print(suma(3, 5))
print(resta(10, 4))

# Pruebas de funciones previendo referencias circulares
print("Cuadrado de 6:", cuadrado(6))
print("Suma secreta de 7 y 8:", suma_secreta(7, 8))

# # Pruebas de importación del paquete eco
# import eco
# print(eco.__file__)
# print(eco.__path__)

# # imprime la ruta de búsqueda de módulos
# import sys
# print(sys.path)


# print("algoritmos disponibles:")    
# from eco.algoritmos.loader import *
# algoritmos = cargar_algoritmos()
# for nombre, algoritmo in algoritmos.items():
#     print(f"Algoritmo cargado: {nombre} -> {algoritmo}")

from importlib.metadata import entry_points

def load(name):
    ep = next(e for e in entry_points(group="eco.algos") if e.name == name)
    mod, obj = ep.value.split(":")
    return getattr(__import__(mod, fromlist=[obj]), obj)

from eco.core import cargar_algoritmos


def main():
    algoritmos = cargar_algoritmos()
    data = "datos de prueba"

    for nombre, algoritmo in algoritmos.items():
        resultado = algoritmo.run(data)
        print(f"{nombre}: {resultado}")

    # print(load("doble_suma")(3, 4))

if __name__ == "__main__":
    main()