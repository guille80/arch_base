from eco import *
from eco.avanzadas.estadisticas import cuadrado, suma_secreta

s = reverse_text("eco")
print(s)

print(suma(3, 5))

print(resta(10, 4))

# import sys
# print(sys.path)

print("Cuadrado de 6:", cuadrado(6))
print("Suma secreta de 7 y 8:", suma_secreta(7, 8))

print("algoritmos disponibles:")    
from eco.algoritmos.loader import *
algoritmos = cargar_algoritmos()
for nombre, algoritmo in algoritmos.items():
    print(f"Algoritmo cargado: {nombre} -> {algoritmo}")