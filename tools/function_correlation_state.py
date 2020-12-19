from IPython.core.display import display


def value_corr_state_display(state_name, df, show_corr=False):
    """
    function designed to show the correlation of different earnings vs
    the Trihalomethane_value for a specific state
    Args:
        state_name: (str) state name
        df: (pd.DataFrame) df_core
        show_corr: (bool) show the corr. matrix

    Returns: value of corr.
    """

    lista_col = ['state', 'Trihalomethane_value', 'manufacturing',
                 'edu_serv', 'acc_food_serv']
    df = df[df.state == state_name][lista_col]
    df = df.corr()
    value = df.Trihalomethane_value[1:].sum() / 3

    if show_corr:
        display(df)
    else:
        pass
    return value
