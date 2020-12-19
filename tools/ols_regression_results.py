import matplotlib.pyplot as plt
import scipy
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np


def apply_regression(earning:str, chemical:str, df:pd.DataFrame):
    """
    funcion diseñada para realizar el analisis estadistico con el fin de generar
     una regresion lineal y una transformacion log, ademas genera las graficas
     principales de ambos casos y el valor de boxcox.
    Args:
        earning: (str) earning sector
        chemical: (str) chemical agent
        df: (pd.DataFrame) df_core

    Returns:
        result_lin_1: model summary linear
        fig_1: graph of model summary linear
        mod_log_2: model summary log
        fig_2: graph of model summary log
        value_boxcox: value boxcox for the case
        r_sqrt_lin: r sqrt lin
        r_sqrt_log: r sqrt log

    """
    model_lin = sm.OLS.from_formula(f"{earning} ~ {chemical}", data=df)
    result_lin = model_lin.fit()
    result_lin_1 = result_lin.summary()
    r_sqrt_lin = result_lin_1.as_text()[231:236]

    fig_1 = sm.graphics.plot_fit(result_lin, f"{chemical}")

    mod_log = smf.ols(formula=f'np.log({earning}) ~ ({chemical})',
                   data=df).fit()
    mod_log_2 = mod_log.summary()
    r_sqrt_log = mod_log_2.as_text()[240:245]

    fig_2 = sm.graphics.plot_fit(mod_log, f"{chemical}")

    earning, fitted_lambda = scipy.stats.boxcox(df[earning])

    value_boxcox = round(fitted_lambda, 2)

    return result_lin_1, fig_1, mod_log_2, fig_2, value_boxcox, r_sqrt_lin,\
                r_sqrt_log
