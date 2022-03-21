from cProfile import label
import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from datetime import datetime, timedelta

CIRCLE_SIZE = 4
CIRCLE_ALPHA = 0.4
pd.options.mode.chained_assignment = None
plt.style.use("seaborn")


def plot_scatterly(
    df: pd.DataFrame,
    x: str = "",
    y: str = "",
    x_label: str = "",
    y_label: str = "",
    title: str = "",
    show: bool = False,
    save: bool = True,
    close: bool = True,
    color_by: str = "",
    kind: str = "scatter",
):
    if color_by == "month":
        df["color"] = df["month"].map(month_to_rgb)
        red_label, blue_label = "Jun/Jul", "Dec/Jan"
    else:
        df["color"] = df["year"].map(year_to_rgb)
        red_label, blue_label = "2022", "2010"

    if kind == "scatter":
        plt.scatter(
            x=list(df[x]),
            y=list(df[y]),
            c=list(df["color"]),
            alpha=CIRCLE_ALPHA,
            s=CIRCLE_SIZE,
        )
    else:
        for year in range(2010, 2023):
            local_df = df[df["year"] == str(year)]
            plt.plot(list(local_df[x]), list(local_df[y]), color=year_to_rgb(year))
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(
        [
            Line2D([0], [0], color=[0, 0, 1], lw=4),
            Line2D([0], [0], color=[1, 0, 0], lw=4),
        ],
        [blue_label, red_label],
    )
    plt.ylim(0, 250)
    if save:
        plt.savefig(f"renders/images/{title.lower().replace(' ', '_')}.png")
    if show:
        plt.show()
    if close:
        plt.close()


def get_weekday_from_index(index):
    di, hi = index
    add_timedelta = False
    if hi == 24:
        hi = 0
        add_timedelta = True
    d = datetime.strptime(str(di), "%Y%m%d")
    if add_timedelta:
        d += timedelta(days=1)
    return d.weekday() + (hi / 24)


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
    plot_scatterly(
        df,
        x="weekday",
        y="München/Landshuter Allee",
        x_label="Day of Week",
        y_label="NO2 [µg/m3] 1h-MW",
        title=title,
        color_by="year",
    )


def plot_weekdays_color_monthly(df, title: str = ""):
    plot_scatterly(
        df,
        x="weekday",
        y="München/Landshuter Allee",
        x_label="Day of Week",
        y_label="NO2 [µg/m3] 1h-MW",
        title=title,
        color_by="month",
    )


def plot_concentration_over_weather(df, year=None):
    plt.rcParams["figure.figsize"] = (12, 9)
    plt.suptitle("Air Quality at München/Landshuter Allee", fontsize=15)
    defaults = {
        "y": "München/Landshuter Allee",
        "y_label": "NO2 [µg/m3] 1h-MW",
        "color_by": "year",
        "close": False,
        "save": False,
    }

    # upper left
    plt.subplot(2, 2, 1)
    plot_scatterly(
        df, x="temperature", x_label="daily average temperature [°C]", **defaults
    )

    # upper right
    plt.subplot(2, 2, 2)
    plot_scatterly(
        df, x="precipitation", x_label="daily precipitation [mm]", **defaults
    )

    # lower left
    plt.subplot(2, 2, 3)
    plot_scatterly(df, x="sunshine", x_label="daily sunshine hours", **defaults)

    # lower right
    plt.subplot(2, 2, 4)
    plot_scatterly(df, x="wind", x_label="daily average wind speed [m/s]", **defaults)

    plt.savefig(
        f"renders/images/concentration_over_weather_conditions{('_' + str(year)) if year is not None else ''}.png"
    )
    plt.close()


def plot_alltime_weekly_cycle(df):
    plt.rcParams["figure.figsize"] = (15, 5)
    plt.suptitle("Air Quality at München/Landshuter Allee - Weekly Cycle", fontsize=15)
    defaults = {
        "x": "weekday",
        "y": "München/Landshuter Allee",
        "y_label": "NO2 [µg/m3] 1h-MW",
        "x_label": "Day of Week (0=Monday Morning, 7=Sunday Evening)",
        "color_by": "year",
        "close": False,
        "save": False,
    }

    # only include years where we have all year data
    df = filter_df_years(df, exclude=["2022"])

    df_averaged_by_weekday = df.groupby(["year", "weekday"]).mean().reset_index()

    # left
    plt.subplot(1, 2, 1)
    plot_scatterly(df, **defaults, title="raw data points")

    # right
    plt.subplot(1, 2, 2)
    plot_scatterly(
        df_averaged_by_weekday,
        **defaults,
        title="mean at each time of day",
        kind="line",
    )

    plt.savefig(f"renders/images/alltime_weekly_cycle.png")
    plt.close()


if __name__ == "__main__":
    luf_df = pd.read_csv("data/LUF_merged.csv").set_index(["date", "hour"])
    dwd_df = pd.read_csv("data/DWD_merged.csv").set_index(["date"])
    df = luf_df.join(dwd_df)

    df["weekday"] = df.index.map(get_weekday_from_index)
    df["month"] = df.index.map(lambda x: str(x[0])[4:6])
    df["year"] = df.index.map(lambda x: str(x[0])[0:4])

    plot_alltime_weekly_cycle(df)

    # for year in range(2016, 2020):
    #     for month in range(1, 13):
    #         local_df = filter_df_years(df, include=[str(year)])
    #         local_df = filter_df_months(df, include=[str(month).zfill(2)])
    #         plot_weekdays_color_monthly(
    #             local_df, title=f"Weekly Cycle {str(month).zfill(2)}.{year}"
    #         )

    plot_concentration_over_weather(df)
    for year in range(2010, 2021):
        local_df = filter_df_years(df, include=[str(year)])
        plot_concentration_over_weather(local_df, year=year)
