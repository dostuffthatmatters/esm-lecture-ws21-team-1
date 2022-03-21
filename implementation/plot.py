import warnings
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from datetime import datetime, timedelta

CIRCLE_SIZE = 4
CIRCLE_ALPHA = 0.5
pd.options.mode.chained_assignment = None
plt.style.use("seaborn")
warnings.simplefilter(action="ignore", category=FutureWarning)


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
        if color_by == "year":
            for year in range(2010, 2023):
                local_df = df[df["year"] == str(year)]
                plt.plot(list(local_df[x]), list(local_df[y]), color=year_to_rgb(year))
        else:
            for month in range(1, 13):
                local_df = df[df["month"] == str(month).zfill(2)]
                plt.plot(
                    list(local_df[x]), list(local_df[y]), color=month_to_rgb(month)
                )
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(
        [
            Line2D([0], [0], color=[0, 0, 1], lw=4),
            Line2D([0], [0], color=[1, 0, 0], lw=4),
        ],
        [blue_label, red_label],
        loc="upper right",
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


def plot_weekly_cycle_colored_by_month(df, month):
    plt.rcParams["figure.figsize"] = (12, 9)
    plt.suptitle(
        f"Air Quality at München/Landshuter Allee - Month {month}", fontsize=15
    )
    defaults = {
        "x": "weekday",
        "y": "München/Landshuter Allee",
        "y_label": "NO2 [µg/m3] 1h-MW",
        "x_label": "Day of Week (0=Monday Morning, 7=Sunday Evening)",
        "color_by": "month",
        "close": False,
        "save": False,
    }

    for i in range(4):
        plt.subplot(2, 2, i + 1)
        local_df = filter_df_years(df, include=[str(2016 + i)])
        plot_scatterly(
            local_df,
            **defaults,
        ),
        plot_scatterly(
            local_df.groupby(["year", "month", "weekday"]).mean().reset_index(),
            **defaults,
            title=str(2016 + i),
            kind="line",
        )

    plt.savefig(f"renders/images/weekly_cycle_colored_by_month_{month}.png")
    plt.close()


def plot_mean_monthwise_weekly_cycle_colored_by_month(df):
    plt.rcParams["figure.figsize"] = (12, 9)
    plt.suptitle(f"Air Quality at München/Landshuter Allee", fontsize=15)
    defaults = {
        "x": "weekday",
        "y": "München/Landshuter Allee",
        "y_label": "NO2 [µg/m3] 1h-MW",
        "x_label": "Day of Week (0=Monday Morning, 7=Sunday Evening)",
        "color_by": "month",
        "close": False,
        "save": False,
        "kind": "line",
    }

    for i in range(4):
        plt.subplot(2, 2, i + 1)
        local_df = filter_df_years(df, include=[str(2016 + i)])
        plot_scatterly(
            local_df.groupby(["year", "month", "weekday"]).mean().reset_index(),
            **defaults,
            title=str(2016 + i),
        )

    plt.savefig(f"renders/images/mean_monthwise_weekly_cycle_colored_by_month.png")
    plt.close()


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


def plot_rolling_concentration_over_weather(df):
    plt.rcParams["figure.figsize"] = (12, 9)
    plt.suptitle("Air Quality at München/Landshuter Allee", fontsize=15)
    defaults = {
        "y": "München/Landshuter Allee",
        "y_label": "NO2 [µg/m3] 1h-MW",
        "color_by": "year",
        "close": False,
        "save": False,
    }

    def plot_rolling(x, x_label):
        for year in range(2010, 2022):
            local_df = df[df["year"] == str(year)].sort_values(by=[x])
            local_df["München/Landshuter Allee"] = local_df.rolling(500, on=x).mean()[
                "München/Landshuter Allee"
            ]
            plot_scatterly(
                local_df,
                x=x,
                x_label=x_label,
                **defaults,
                kind="line",
            )

    # upper left
    plt.subplot(2, 2, 1)
    plot_rolling("temperature", "daily average temperature [°C]")

    # upper right
    plt.subplot(2, 2, 2)
    plot_rolling("precipitation", "daily precipitation [mm]")

    # lower left
    plt.subplot(2, 2, 3)
    plot_rolling("sunshine", "daily sunshine hours")

    # lower right
    plt.subplot(2, 2, 4)
    plot_rolling("wind", "daily average wind speed [m/s]")

    plt.savefig(f"renders/images/rolling_concentration_over_weather_conditions.png")
    plt.close()


if __name__ == "__main__":
    luf_df = pd.read_csv("data/LUF_merged.csv").set_index(["date", "hour"])
    dwd_df = pd.read_csv("data/DWD_merged.csv").set_index(["date"])
    df = luf_df.join(dwd_df)

    df["weekday"] = df.index.map(get_weekday_from_index)
    df["month"] = df.index.map(lambda x: str(x[0])[4:6])
    df["year"] = df.index.map(lambda x: str(x[0])[0:4])

    plot_alltime_weekly_cycle(df)

    for i in range(1, 13):
        month = str(i).zfill(2)
        plot_weekly_cycle_colored_by_month(filter_df_months(df, include=[month]), month)

    plot_mean_monthwise_weekly_cycle_colored_by_month(df)

    plot_concentration_over_weather(df)

    for year in range(2010, 2021):
        local_df = filter_df_years(df, include=[str(year)])
        plot_concentration_over_weather(local_df, year=year)

    plot_rolling_concentration_over_weather(df)
