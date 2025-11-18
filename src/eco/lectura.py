import importlib.resources

def leer_tabla():
    path = importlib.resources.files("eco") / "data/tabla.csv"
    return path.read_text()