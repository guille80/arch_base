# Arquitectura para probar el registro de plugins de manera automática  

## Paquete externo que registra algoritmos en eco.algoritmos

Para que un paquete externo pueda integrarse con el sistema de entry points y añadir algoritmos, debe declarar en su propio pyproject.toml el grupo eco.algoritmos con sus algoritmos.

## Estructura del paquete externo

paquete-externo/  
├── src/  
│   └── paquete_externo/  
│       ├── __init__.py  
│       └── algoritmo_externo.py  
├── pyproject.toml  
└── README.md  

## Código del paquete a integrar

src/paquete_externo/algoritmo_externo.py
```python 
class AlgoritmoExterno:
    def run(self, data):
        return f"Procesado por AlgoritmoExterno: {data}"
```

## pyproject.toml del paquete externo
```python 
[project]
name = "paquete-externo"
version = "0.1.0"
description = "Paquete externo que añade algoritmos al grupo eco.algoritmos"
authors = [{ name="Guillermo", email="guillermo@example.com" }]
dependencies = []

[tool.setuptools.packages.find]
where = ["src"]

[tool.setuptools]
package-dir = {"" = "src"}

[project.entry-points."eco.algoritmos"]
algoritmo_externo = "eco_externo.algoritmo_externo:AlgoritmoExterno"
```

## Uso conjunto

Cuando instales ambos paquetes (eco y eco-externo) en el mismo entorno, la función cargar_algoritmos() del paquete eco cargará automáticamente los algoritmos internos y externos registrados en el grupo eco.algoritmos.

Así, desde main.py podrás ejecutar todos los algoritmos sin preocuparte por su origen.