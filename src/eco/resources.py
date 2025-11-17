import importlib.resources
from importlib.resources import files
with importlib.resources.as_file(files("eco") / "data/tabla.csv") as f:
    datos = f.read_text()

# import importlib.resources
#     with importlib.resources.files("eco") / "data/tabla.csv" as f:
#     datos = f.read_text()