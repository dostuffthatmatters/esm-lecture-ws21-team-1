import os
import pandas as pd
import numpy as np
import warnings


def create_luf_df(year: int, month: int | None, city: str):
    if month is None:
        filename = f"data/raw/NO2_{year}.xlsx"
    else:
        filename = f"data/raw/NO2_{year}_{str(month).zfill(2)}.xlsx"

    if not os.path.isfile(filename):
        return None
    else:
        print(f"reading {filename}")

    # hide warnings from excel libraries
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        df = pd.read_excel(filename, engine="openpyxl")

    # rename columns correctly
    if month is None:
        df.columns = list(df.loc[0])
    else:
        df.columns = list(df.loc[1])
    df.columns = [c.replace(f"{city} ", f"{city}/") for c in df.columns]

    # validating the excel file format
    assert df.columns[0] == "Zeitpunkt"
    if month is None:
        df = df.drop(index=[0])
    else:
        assert list(df.loc[0])[0] == "  NO2 [µg/m3] 1h-MW"
        df = df.drop(index=[0, 1])

    # drop columns not of interest
    df = df.drop(
        axis=1,
        labels=[
            c for c in df.columns if not (c.startswith(f"{city}") or c == "Zeitpunkt")
        ],
    )

    # drop all rows no from this month
    if month is None:
        df = df[df["Zeitpunkt"].str.contains(f".{year} ")]
    else:
        df = df[df["Zeitpunkt"].str.contains(f".{str(month).zfill(2)}.{year} ")]
    df = df.set_index("Zeitpunkt")

    # replace all cells with no valid entry
    df = df.applymap(lambda x: x if str(x).replace(".", "").isnumeric() else np.nan)

    return df


if __name__ == "__main__":

    dfs = []
    for year in range(2021, 2023):
        for month in range(1, 13):
            df = create_luf_df(year, month, "München")
            if df is not None:
                dfs.append(df)

    for year in range(2010, 2021):
        df = create_luf_df(year, None, "München")
        if df is not None:
            dfs.append(df)

    df = pd.concat(dfs, axis=0, join="outer").sort_index()
    print(df)
    print(df.columns)

    df.to_csv("data/LUF_merged.csv", na_rep="NaN", float_format="%.0f")
