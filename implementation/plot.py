from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

CIRCLE_SIZE = 4
CIRCLE_ALPHA = 0.4
pd.options.mode.chained_assignment = None


def plot_scatterly(
    df: pd.DataFrame,
    x: str = "",
    y: str = "",
    x_label: str = "",
    y_label: str = "",
    title: str = "",
    save: bool = True,
    show: bool = False,
):
    p = df.plot.scatter(
        x=x,
        y=y,
        alpha=CIRCLE_ALPHA,
        c="color",
        s=CIRCLE_SIZE,
    )
    p.set_title(title)
    p.set_xlabel(x_label)
    p.set_ylabel(y_label)
    plt.ylim(0, 250)
    if save:
        plt.savefig(f"renders/{title.lower().replace(' ', '_')}.png")
    if show:
        plt.show()
    plt.close()


def get_weekday_from_str(s):
    add_timedelta = False
    if s[11:13] == "24":
        s = s[:11] + "00" + s[13:]
        add_timedelta = True
    d = datetime.strptime(s, "%d.%m.%Y %H:%M")
    if add_timedelta:
        d += timedelta(days=1)
    return d.weekday() + (d.hour / 24)


def filter_df_years(
    df: pd.DataFrame, include: list[str] = None, exclude: list[str] = None
):
    assert None in [include, exclude], 'Only one of "include"/"exclude" can be set'
    if include is not None:
        filter_condition = [False] * len(list(df["year"]))
        for year in include:
            filter_condition |= df["year"] == year
    if exclude is not None:
        filter_condition = [True] * len(list(df["year"]))
        for year in exclude:
            filter_condition &= df["year"] != year
    return df[filter_condition]


def filter_df_months(
    df: pd.DataFrame, include: list[str] = None, exclude: list[str] = None
):
    assert None in [include, exclude], 'Only one of "include"/"exclude" can be set'
    if include is not None:
        filter_condition = [False] * len(list(df["month"]))
        for month in include:
            filter_condition |= df["month"] == month
    if exclude is not None:
        filter_condition = [True] * len(list(df["month"]))
        for month in exclude:
            filter_condition &= df["month"] != month
    return df[filter_condition]


# blue = 2010, red = 2022
def year_to_rgb(y):
    x = (int(y) - 2010) / 12
    return [x, 0, 1 - x]


# blue = january/december, red = june/july
def month_to_rgb(m):
    x = (abs(int(m) - 6.5) - 0.5) / 5
    return [1 - x, 0, x]


def plot_weekdays_color_yearly(df, title: str = ""):
    df["color"] = df["year"].map(year_to_rgb)
    plot_scatterly(
        df,
        x="weekday",
        y="München/Landshuter Allee",
        x_label="Day of Week",
        y_label="NO2 [µg/m3] 1h-MW",
        title=title,
    )


def plot_weekdays_color_monthly(df, title: str = ""):
    df["color"] = df["month"].map(month_to_rgb)
    plot_scatterly(
        df,
        x="weekday",
        y="München/Landshuter Allee",
        x_label="Day of Week",
        y_label="NO2 [µg/m3] 1h-MW",
        title=title,
    )


if __name__ == "__main__":
    df = pd.read_csv("data/NO2_merged.csv").set_index("Zeitpunkt")

    df["weekday"] = df.index.map(get_weekday_from_str)
    df["day"] = df.index.map(lambda x: x[0:2])
    df["month"] = df.index.map(lambda x: x[3:5])
    df["year"] = df.index.map(lambda x: x[6:10])
    df["hour"] = df.index.map(lambda x: x[11:13])

    print(df)

    for year in range(2010, 2022):
        local_df = filter_df_years(df, include=[str(year)])
        plot_weekdays_color_yearly(local_df, title=f"Weekly Cycle {year}")

    for year in range(2016, 2020):
        for month in range(1, 12):
            local_df = filter_df_years(df, include=[str(year)])
            local_df = filter_df_months(df, include=[str(month).zfill(2)])
            plot_weekdays_color_monthly(
                local_df, title=f"Weekly Cycle {str(month).zfill(2)}.{year}"
            )
