import pandas as pd


def leer_archivos(path:str):
    """
    function in charge of reading files in a certain path with .csv format,
     try to do it with a conventional separator or separated by semicolons.
    Args:
        path: (str) path of file
    Returns:
        pd.Dataframe: dataframe
    """
    try:
        df = pd.read_csv(path, encoding='unicode-escape')
    except:
        df = pd.read_csv(path, encoding='unicode-escape', sep=';')
    return df