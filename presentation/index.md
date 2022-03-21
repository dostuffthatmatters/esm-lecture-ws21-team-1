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

_PICTURE OF GOOGLE MAPS_

---

_PICTURES OF STATION_

---

_ANSWERED QUESTIONS_

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
2. Remove locations not of interest
3. Merge all data into one CSV file

<!--

Optional:
Last signal from Prinzregentenstraße: 20120208
Last signal from Moosach: 20130709

-->

---

In the following I will only look at **data between 2010 and now** and the station **at Landshuter Allee** from $\textbf{NO}_\textbf{2}$ **concentrations**.

---

![h:500 bg](../implementation/renders/images/alltime_weekly_cycle.png)

---

**Findings:**

-   Daily and weekly cycle
-   Shape of cycle did not change since 2010
-   Average concentration has been reduced by 40-50% since 2010

<br/>

**Next Question:** Is there a trend by month - certain months with low/high concentrations.

<!--

Since the concentration goes down over the years we should only look at years separately.

We picked 2016, 2017, 2018 and 2019 (the 4 years before the current pandemic).

-->

---

![h:700 bg](../implementation/renders/videos/weekly_cycle_colored_by_month.gif)

<!--
The concentration seems to go down in the winter months and tends to rise during summer.
-->

---

![h:700 bg](../implementation/renders/images/mean_monthwise_weekly_cycle_colored_by_month.png)

<!--

In a still image this can be seen more clearly. But I made the GIF and wanted to show it too ;)

I down know why the concentration goes down during winter. I actually did assume with many people on vacation in summer the concentrations should be lower.

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

The DWD website's organization is rather messy so I won't show picture of how you get there. Here is the Link and the name of that archive.

-->

---

![h:700 bg](../implementation/renders/videos/concentration_over_weather_conditions.gif)

<!--

This GIF is again looping over all the years.

The good thing: We see a correlation between wind speed and concentration. Higher wind speed -> lower concentration. Molecules get transported away faster.

The interesting thing here is that there is no correlation between temperature/precipitation and concentration.

-->

---

_BEST FIT LINES_

---

Argument for using a car: "Less people want to use a bike or public transport when it is cold or wet raining"

**Do these findings disprove this argumentation?** Is the reason for using a car really the weather or is it mainly habit and each individuals situation?

---

**LUF data** is under `CC 4.0 BY` license.

**DWD data** has no license except for the statement "data is freely available without any restrictions".

<!--
Therefore we can freely share cleaned up data and all the plots.
-->

---

**Code, cleaned data, plots and presentation:**

https://github.com/dostuffthatmatters/esm-lecture-group-task

<!--

If you want to use the same data, here is the link to our open source code which does this preparation and analysis.

Will be open source after 3pm ;)

-->
