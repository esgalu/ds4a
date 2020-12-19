import pandas as pd
import os
import dataframe_image as dfi
from IPython.core.display import display

from tools.generate_dic_data import apply_dic_data

# Libreries for paths
from core.metadata.directory import PathOutput


def apply_tables_maker_eda(path, display_=False, saving=True):
    df = apply_dic_data(path)

    for key in df:
        print(f'---- DATABASE {key}----- :  READY')
        tmp_0 = df[key].describe().T
        tmp_1 = pd.DataFrame(df[key].isnull().any()).rename(
            columns={0: 'Is there null value?'})
        tmp_2 = pd.DataFrame(df[key].isnull().sum()).rename(
            columns={0: 'NULL_VALUES'})
        tmp_3 = pd.DataFrame(df[key].dtypes).rename(columns={0: 'DTYPES'})

        tmp = pd.concat([tmp_1, tmp_2, tmp_3, tmp_0], axis=1)
        tmp.fillna('NA', inplace=True)

        for col in tmp:
            tmp.rename(columns={col: col.upper()}, inplace=True)

        """Show Display"""
        if display_:
            display(tmp)
        else:
            pass

        """Saving Condition"""
        if saving:
            tmp.dfi.export(os.path.join(PathOutput.output_EDA_tables,
                                        f'table_resume_{key}.png'), max_rows=20)
        else:
            pass

    return None
