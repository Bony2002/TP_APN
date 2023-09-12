import pandas as pd

data = {
    "sdc": [],
    "prob_entrar": [1],
    "horas": [1],
    "total_tiempos": [1],
    "datos_choques": [1],
    "total_tiempos_sdc": [1],
    "total_choques_sdc": [1]
}
data["sdc"].append(True)

df = pd.DataFrame(data)

print(df)