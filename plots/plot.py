import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data.csv")

df_sin_sdc = df[df['sdc'] == False]

df_filtro_2 = df_sin_sdc[df_sin_sdc['horas'] == 2]

mean_2hr_02den = np.array(eval(df_filtro_2["total_tiempos"][0])).mean() # Mean value en 2 horas con density 0.2

mean_2hr_04den = np.array(eval(df_filtro_2["total_tiempos"][3])).mean() # Mean value en 2 horas con density 0.4

mean_2hr_06den = np.array(eval(df_filtro_2["total_tiempos"][6])).mean() # Mean value en 2 horas con density 0.6

df_filtro_5 = df_sin_sdc[df_sin_sdc['horas'] == 5]

mean_5hr_02den = np.array(eval(df_filtro_5["total_tiempos"][9])).mean() # Mean value en 5 horas con density 0.2

mean_5hr_04den = np.array(eval(df_filtro_5["total_tiempos"][12])).mean() # Mean value en 5 horas con density 0.4

mean_5hr_06den = np.array(eval(df_filtro_5["total_tiempos"][15])).mean() # Mean value en 5 horas con density 0.6

df_filtro_7 = df_sin_sdc[df_sin_sdc['horas'] == 7]

mean_7hr_02den = np.array(eval(df_filtro_7["total_tiempos"][18])).mean() # Mean value en 7 horas con density 0.2

mean_7hr_04den = np.array(eval(df_filtro_7["total_tiempos"][21])).mean() # Mean value en 7 horas con density 0.4

mean_7hr_06den = np.array(eval(df_filtro_7["total_tiempos"][24])).mean() # Mean value en 7 horas con density 0.6

