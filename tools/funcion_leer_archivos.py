import pandas as pd


def leer_archivos(path):
    df = pd.read_csv(path, encoding='unicode-escape')
    return df