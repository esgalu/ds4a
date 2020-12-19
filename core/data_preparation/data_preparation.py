import os

import pandas as pd

from tools.generate_dic_data import apply_dic_data
from core.metadata.directory import PathDataRaw, PathOutput


def apply_data_preparation(saving=True, path_=PathOutput.output_data_core):
    """

    """

    df = apply_dic_data(PathDataRaw.data)

    list_col_earnings = [
        'estate', 'county', 'year', 'total_med', 'total_agri_fish_mine',
        'agri_fish_hunt', 'construction', 'manufacturing', 'wholesale_trade',
        'retail_trade', 'transport_warehouse_utilities', 'transport_warehouse',
        'fin_ins_realest', 'fin_ins', 'total_prof_sci_mgmt_admin',
        'prof_sci_tech', 'admin_sup', 'total_edu_health_social', 'edu_serv',
        'health_social', 'total_arts_ent_acc_food', 'acc_food_serv',
        'other_ser', 'pub_admin']

    df['EARNINGS'] = df['EARNINGS'][list_col_earnings]

    df['EARNINGS'].rename(columns={'estate': 'state'}, inplace=True)

    for col in ['state', 'county']:
        df['EARNINGS'][col] = df['EARNINGS'][col].str.upper()

    df['EARNINGS']['county'] = \
        df['EARNINGS'].county.str.split(',', expand=True)[0]
    df['EARNINGS']['county'] = df['EARNINGS'].county.str.replace('COUNTY', '')
    df['EARNINGS']['county'] = df['EARNINGS'].county.str.strip()
    df['EARNINGS']['state'] = df['EARNINGS'].state.str.strip()

    df['EARNINGS'].drop(columns=[
        'total_med', 'total_prof_sci_mgmt_admin', 'total_edu_health_social',
        'total_arts_ent_acc_food', 'total_agri_fish_mine', 'fin_ins_realest',
        'fin_ins', 'prof_sci_tech', 'admin_sup'],
        inplace=True)

    df['EARNINGS'] = df['EARNINGS'].groupby(['state', 'year'],
                                            as_index=False).sum()

    cond_year_min = df['CHEMICALS'].year >= 2010
    cond_year_max = df['CHEMICALS'].year <= 2016

    df['CHEMICALS'] = df['CHEMICALS'][cond_year_min & cond_year_max]

    df['CHEMICALS'] = df['CHEMICALS'].groupby(
        ['state', 'county', 'chemical_species', 'contaminant_level',
         'unit_measurement', 'year'])[['value']].sum().reset_index()

    for col in ['state', 'county']:
        df['CHEMICALS'][col] = df['CHEMICALS'][col].str.upper()

    df['CHEMICALS'].value = df['CHEMICALS'].apply(
        lambda x: x.value / 1000 if x.unit_measurement == 'micrograms/L' else x.value,
        axis=1)
    df['CHEMICALS'].unit_measurement = 'mg/L'

    df['CHEMICALS'] = \
        df['CHEMICALS'].groupby(['state', 'county', 'chemical_species',
                                 'unit_measurement', 'year'])[
            ['value']].sum().reset_index()

    df_modify = {}
    lista_col_chemical = ['state', 'county', 'chemical_species', 'year', 'value']

    for agente in df['CHEMICALS'].chemical_species.unique():
        df_modify[agente] = df['CHEMICALS'][
            df['CHEMICALS'].chemical_species == agente][lista_col_chemical]
        df_modify[agente].rename(columns={'value': f'{agente}_value'},
                                 inplace=True)
        df_modify[agente].drop(columns=['chemical_species'], inplace=True)
        df_modify[agente].set_index(['state', 'county', 'year'], inplace=True)

    df['CHEMICALS'] = pd.concat([df_ for df_ in df_modify.values()],
                                axis=1).reset_index()

    df['CHEMICALS'] = df['CHEMICALS'].groupby(['state', 'year'],
                                              as_index=False).sum()

    df_core = pd.merge(df['CHEMICALS'], df['EARNINGS'],
                       how='inner', on=['state', 'year'])

    if saving:
        df_core.to_csv(
            os.path.join(path_, 'data_core.csv'), index=False, sep=';'
        )
    else:
        pass

    return df_core