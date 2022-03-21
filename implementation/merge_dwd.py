import numpy as np
import pandas as pd

df = pd.read_csv("data/raw/dwd_klima_flughafen.txt", sep=";")

df = df[["MESS_DATUM", "  FM", " RSK", " SDK", " TMK"]]
df = df.rename(
    columns={
        "MESS_DATUM": "date",
        "  FM": "wind",
        " RSK": "precipitation",
        " SDK": "sunshine",
        " TMK": "temperature",
    }
).set_index("date")
df = df.replace(-999.0, np.nan)

print(df)
df.to_csv("data/DWD_merged.csv", na_rep="NaN", float_format="%.1f")
