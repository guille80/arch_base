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


# Ejemplo de uso:
def load_config_yaml() :

    data = load_yaml("config.yaml")
    print("Datos cargados desde YAML:", data)

    # Ejemplos de uso
    # print(validar_tipo_yaml("hola", "str"))     # True
    # print(validar_tipo_yaml(42, "int"))         # True
    # print(validar_tipo_yaml(3.14, "float"))     # True
    # print(validar_tipo_yaml(True, "bool"))      # True
    # print(validar_tipo_yaml(None, "null"))      # True
    # print(validar_tipo_yaml([1, 2, 3], "list")) # True
    # print(validar_tipo_yaml({"a": 1}, "dict"))  # True    

    if validar_tipo_yaml(data['rounds'], "int") :
        print("El valor de 'rounds' es un entero:", data['rounds'])
    else :
        print("El valor de 'rounds' no es un entero:", data['rounds'])

    if validar_tipo_yaml(data['logging']['level'], "str") :
        print("El valor de 'logging.level' es una cadena:", data['logging']['level'])
    else :  
        print("El valor de 'logging.level' NO es una cadena:", data['logging']['level'])

    if validar_tipo_yaml(data['clients'], "dict") :
        print("El valor de 'clients' es un diccionario:", data['clients'])
    else :
        print("El valor de 'clients' no es un diccionario:", data['clients'])

    if validar_tipo_yaml(data['algorithm']['params'], "dict") :
        print("El valor de 'algorithm.params' es un diccionario:", data['algorithm']['params'])
    else :
        print("El valor de 'algorithm.params' no es un diccionario:", data['algorithm']['params'])

