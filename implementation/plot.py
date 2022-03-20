from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

CIRCLE_SIZE = 4
CIRCLE_ALPHA = 0.4


def get_weekday_from_str(s):
    add_timedelta = False
    if s[11:13] == "24":
        s = s[:11] + "00" + s[13:]
        add_timedelta = True
    d = datetime.strptime(s, "%d.%m.%Y %H:%M")
    if add_timedelta:
        d += timedelta(days=1)
    return d.weekday() + (d.hour / 24)


def filter_df_by_years(df: pd.DataFrame, years: list[str]):
    filter_condition = df["year"] | True
    for year in years:
        filter_condition &= df["year"] == year
    return df[filter_condition]


def filter_df_by_months(df: pd.DataFrame, months: list[str]):
    filter_condition = df["month"] | True
    for month in months:
        filter_condition &= df["month"] == month
    return df[filter_condition]


# blue = 2010, red = 2022
def year_to_rgb(y):
    x = (int(y) - 2010) / 12
    return [x, 0, x - 1]


# blue = january/december, red = june/july
def month_to_rgb(m):
    x = abs(int(m) - 6.5) - 0.5
    return [1 - x, 0, x]


def plot_weekdays_color_yearly(df):
    df["color"] = df["year"].map(year_to_rgb)
    p = df.plot.scatter(
        x="weekday",
        y="München/Landshuter Allee",
        alpha=CIRCLE_ALPHA,
        c="color",
        s=CIRCLE_SIZE,
    )
    p.set_ylabel("NO2 [µg/m3] 1h-MW")
    plt.show()


def plot_weekdays_color_monthly(df):
    df["color"] = df["month"].map(month_to_rgb)
    p = df.plot.scatter(
        x="weekday",
        y="München/Landshuter Allee",
        alpha=CIRCLE_ALPHA,
        c="color",
        s=CIRCLE_SIZE,
    )
    p.set_ylabel("NO2 [µg/m3] 1h-MW")
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv("data/NO2_merged.csv").set_index("Zeitpunkt")

    df["weekday"] = df.index.map(get_weekday_from_str)
    df["day"] = df.index.map(lambda x: x[0:2])
    df["month"] = df.index.map(lambda x: x[3:5])
    df["year"] = df.index.map(lambda x: x[6:10])
    df["hour"] = df.index.map(lambda x: x[11:13])

    print(df)

    df = filter_df_by_years(df, ["2016", "2017"])

    plot_weekdays_color_yearly(df)
