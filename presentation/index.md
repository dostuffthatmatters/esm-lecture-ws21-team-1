---
marp: true
paginate: false
math: katex
---

<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

# Team 1 (Landshuter Allee) - ESM Lecture

**Team Members:** Yichu Chen, Mei Gao, Moritz Makowski

---

<!--
paginate: true
-->

# 1. Visit the site

---

Station located at **Landshuter Allee**:

![h:550 center](images/station-map.png)

---

![h:600 center](images/station-image-1.jpg)

---

![h:600 center](images/station-image-3.jpg)

<!--
The road is 8 lanes wide at that location.

CO2 Boxes next to the station.
TODO: What are they?

-->

---

## Are all the requirements of the 39. BImSchV fulfilled?

-   Maximum distance to the street: 10 m
-   Minimum distance to the crossroad: 25 m
-   Height of the measurement inlet: 1.5 to 4 m

---

## Do you think that this particular station is representative of the city/for the background?

---

# 2. Analyze the data

---

...

---

# 3. Additional work: **MORE DATA**

---

## LFU - Air Quality Data Archive

-   $\text{NO}_2$, $\text{PM}_{10}$, $\text{PM}_{2.5}$, $\text{O}_{3}$, $\text{CO}$, ...
-   52 Stations in Bavaria
-   Hourly data = `8760` data points per station per year
-   Since 1980 (not all stations over the whole timespan)

<br/>

**Data Source:** https://www.lfu.bayern.de/luft/immissionsmessungen/messwertarchiv

---

![center h:650](images/lfu-website.png)

<!--
"Daten" -> "Luft" -> "Messwertarchiv"

I will talk about the data license at the end.

-->

---

### LFU - Data Preparation

1. Replace cells like `?`, `#` or nothing in it with `NaN`
2. Remove locations, not of interest
3. Merge all data into one CSV file

<!--

Optional:
Last signal from Prinzregentenstraße: 20120208
Last signal from Moosach: 20130709

-->

---

In the following, I will only look at **data between 2010 and now** and the station **at Landshuter Allee** from $\textbf{NO}_\textbf{2}$ **concentrations**.

---

![h:500 bg](../implementation/renders/images/alltime_weekly_cycle.png)

---

**Findings:**

-   Daily and weekly cycle
-   Shape of the cycle did not change since 2010
-   Average concentration has been reduced by 40-50% since 2010

<br/>

**Next Question:** Is there a trend by month - certain months with low/high concentrations.

<!--

Since the concentration goes down over the years we should only look at years separately.

We picked 2016, 2017, 2018, and 2019 (the 4 years before the current pandemic).

-->

---

![h:700 bg](../implementation/renders/videos/weekly_cycle_colored_by_month.gif)

<!--
The concentration seems to go down in the winter months and tends to rise during summer.
-->

---

![h:700 bg](../implementation/renders/images/mean_monthwise_weekly_cycle_colored_by_month.png)

<!--

In a still image, this can be seen more clearly. But I made the GIF and wanted to show it too ;)

I down know why the concentration goes down during winter. I did assume with many people on vacation in summer the concentrations should be lower.

Something not uncommon in data science: You assume something and find out that the opposite is true.

-->

---

**Findings:**

-   Concentration in summer months tends to be higher than in winter months in the observed period

<br/>

**Next Question:** Is there a correlation between weather and concentration.

<!--

LAST QUESTION we want to visit here.

Assumption: People use cars more often when it is cold or when it is raining, i.e. higher concentrations.

-->

---

## DWD - German Climatedata Archive

-   Mean temperature, mean pressure, sunshine hours, ...
-   83 stations in Germany
-   Daily data
-   **Munich Airport** data since 1992

<br/>

**Data Source:** https://www.dwd.de/DE/leistungen/klimadatendeutschland/klarchivtagmonat ("DWD - Klimadaten Deutschland - Monats- und Tageswerte (Archiv)")

<!--

The DWD website's organization is rather messy so I won't show a picture of how you get there. Here is the Link and the name of that archive.

-->

---

![h:700 bg](../implementation/renders/images/concentration_over_weather_conditions.png)

<!--

The good thing: We see a correlation between wind speed and concentration. Higher wind speed -> lower concentration. Molecules get transported away faster.

The interesting thing here is that there is no correlation between temperature/precipitation and concentration.

There is also no more information when looking at individual years.

-->

---

![h:700 bg](../implementation/renders/images/rolling_concentration_over_weather_conditions.png)

<!--

I chose to use a rolling mean instead of the best fit line since the best fit line can be dominated by a bulk of points at e.g. 0mm precipitation, 0m/s wind speed, or 0h sunshine.

The only slight trend there is a rising concentration with temperature. Only very minor trends, not very conclusive.

-->

---

One argument for using a car: "Fewer people want to use a bike or public transport when it is cold or wet raining"

**Do these findings disprove this argumentation?** Is the reason for using a car really the weather or is it mainly habit and each individual's situation?

---

**LUF data** is under `CC 4.0 BY` license.

**DWD data** has no license except for the statement "data is freely available without any restrictions".

<!--
Therefore we can freely share cleaned-up data and all the plots.
-->

---

**Code, cleaned data, plots, and presentation:**

https://github.com/dostuffthatmatters/esm-lecture-group-task

<!--

If you want to use the same data, here is the link to our open source code which does this preparation and analysis.

Will be open source after 3 pm ;)

-->
