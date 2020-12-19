from pathlib import Path


def aplicar_enlistar_nombres_archivos(path:str):
    """
    Function responsible for generating a list of files found in a folder.
    Args:
        path: (str) path of folder
    Returns: list
    """
    lista = [obj.name for obj in Path(path).iterdir() if obj.is_file()]
    return lista