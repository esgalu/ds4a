from pathlib import Path


def aplicar_enlistar_nombres_archivos(path:str):
    lista = [obj.name for obj in Path(path).iterdir() if obj.is_file()]
    return lista