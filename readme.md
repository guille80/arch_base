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

#· Uso conjunto

Cuando instales ambos paquetes (eco y eco-externo) en el mismo entorno, la función cargar_algoritmos() del paquete eco cargará automáticamente los algoritmos internos y externos registrados en el grupo eco.algoritmos.

Así, desde main.py podrás ejecutar todos los algoritmos sin preocuparte por su origen.

# Estructura para integrar varios plugins en un solo proyecto

Para tener ambos plugins, `eco_plugin` (con los algoritmos internos) y `eco_externo` (con algoritmos externos), dentro del mismo proyecto pero separados, lo ideal es organizar un monorepo con subdirectorios independientes para cada paquete. Así mantienes modularidad y facilitas el desarrollo y mantenimiento.

## Una estructura recomendada sería:

```
mi_proyecto_eco/  
├── eco_plugin/           # Paquete principal con algoritmos internos  
│   ├── src/  
│   │   └── eco/  
│   │       ├── __init__.py  
│   │       ├── core.py  
│   │       └── algoritmos/  
│   │           ├── __init__.py  
│   │           ├── base.py  
│   │           ├── algoritmo_a.py  
│   │           └── algoritmo_b.py  
│   ├── pyproject.toml  
│   └── README.md  
│  
├── eco_externo/          # Paquete externo con algoritmos adicionales  
│   ├── src/  
│   │   └── eco_externo/  
│   │       ├── __init__.py  
│   │       └── algoritmo_externo.py  
│   ├── pyproject.toml  
│   └── README.md  
│  
└── main.py               # Script raíz para ejecutar todo  
```

Cada paquete tiene su propio `pyproject.toml` con su configuración y entry points. Puedes instalar ambos en el mismo entorno virtual (por ejemplo, con `pip install -e ./eco_plugin` y `pip install -e ./eco_externo`). La función `cargar_algoritmos()` del paquete principal (`eco_plugin`) cargará todos los entry points registrados, incluyendo los del paquete externo.

El `main.py` en la raíz puede importar y usar esa función para ejecutar todos los algoritmos, internos y externos, sin importar su origen.


