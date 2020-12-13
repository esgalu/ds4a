import pandas as pd


def leer_archivos(path):
    try:
        df = pd.read_csv(path, encoding='unicode-escape')
    except:
        df = pd.read_csv(path, encoding='unicode-escape', sep=';')
    return df