import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def validar_tipo_yaml(valor, tipo_str):
    """
    Valida si un valor corresponde al tipo YAML especificado.
    
    Parámetros:
        valor: cualquier dato a validar
        tipo_str: nombre del tipo en string (ej. 'int', 'str', 'list')
    
    Retorna:
        True si el valor es del tipo especificado, False en caso contrario.
    """
    tipos_yaml = {
        "str": str,
        "int": int,
        "float": float,
        "bool": bool,
        "null": type(None),
        "list": list,
        "dict": dict,
    }
    
    if tipo_str not in tipos_yaml:
        raise ValueError(f"Tipo '{tipo_str}' no soportado en YAML")
    
    return isinstance(valor, tipos_yaml[tipo_str])


