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


# def load_config_yaml() :
#     from yaml_loader.loader import load_yaml, validar_tipo_yaml

#     data = load_yaml("config.yaml")
#     print("Datos cargados desde YAML:", data)

#     # Ejemplos de uso
#     # print(validar_tipo_yaml("hola", "str"))     # True
#     # print(validar_tipo_yaml(42, "int"))         # True
#     # print(validar_tipo_yaml(3.14, "float"))     # True
#     # print(validar_tipo_yaml(True, "bool"))      # True
#     # print(validar_tipo_yaml(None, "null"))      # True
#     # print(validar_tipo_yaml([1, 2, 3], "list")) # True
#     # print(validar_tipo_yaml({"a": 1}, "dict"))  # True    

#     if validar_tipo_yaml(data['rounds'], "int") :
#         print("El valor de 'rounds' es un entero:", data['rounds'])
#     else :
#         print("El valor de 'rounds' no es un entero:", data['rounds'])

#     if validar_tipo_yaml(data['logging']['level'], "str") :
#         print("El valor de 'logging.level' es una cadena:", data['logging']['level'])
#     else :  
#         print("El valor de 'logging.level' NO es una cadena:", data['logging']['level'])

#     if validar_tipo_yaml(data['clients'], "dict") :
#         print("El valor de 'clients' es un diccionario:", data['clients'])
#     else :
#         print("El valor de 'clients' no es un diccionario:", data['clients'])

#     if validar_tipo_yaml(data['algorithm']['params'], "dict") :
#         print("El valor de 'algorithm.params' es un diccionario:", data['algorithm']['params'])
#     else :
#         print("El valor de 'algorithm.params' no es un diccionario:", data['algorithm']['params'])

def main():
    algoritmos = cargar_algoritmos()
    data = "datos de prueba"

    for nombre, algoritmo in algoritmos.items():
        resultado = algoritmo.run(data)
        print(f"{nombre}: {resultado}")

    # print(load("doble_suma")(3, 4))

    # Ejemplo de uso de carga de YAML
    from yaml_loader.loader import load_config_yaml
    load_config_yaml()


if __name__ == "__main__":
    main()