import os

from tools.funcion_enlistar_nombres_carpeta import \
    aplicar_enlistar_nombres_archivos
from tools.funcion_leer_archivos import leer_archivos


def apply_dic_data(path):
    """
    Function designed to save the databases in a dictionary, the key being the
    name of the file without extension and the key being the dataframe
    Args:
        path: (str) path of folder

    Returns: (dict) dict with dataframes
    """
    lista_archivos = aplicar_enlistar_nombres_archivos(path)
    lista_archivos = [(value[:-4]).upper() for value in lista_archivos]

    df = {}

    for archivo in lista_archivos:
        path_tmp = os.path.join(path, f'{archivo.lower()}.csv')
        df[archivo] = leer_archivos(path_tmp)

    return df
