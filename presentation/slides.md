---
theme: ./theme
layout: cover
drawings:
    persist: false
title: esm-lecture-presentation-team-1
---

# Team 1 (Landshuter Allee) - ESM Lecture

**Team Members:** Yichu Chen, Mei Gao, Moritz Makowski

---
layout: cover
---

# <uim-scenery class="mr-1"/> Visit the site

---

Station located at **Landshuter Allee**:

<div class="w-full flex justify-center">
    <img src="/images/section-1/station-map.png" class="w-lg rounded"/>
</div>

---

<div class="w-full h-full flex justify-center items-center">
    <img src="/images/section-1/station-image-device.png" class="w-xl rounded"/>
</div>

<!--

The road is 8 lanes wide at that location.

-->

---

**Are all the requirements of the 39. BImSchV fulfilled?**

-   Maximum distance to the street: 10 m
-   Minimum distance to the crossroad: 25 m
-   Height of the measurement inlet: 1.5 to 4 m


---

<div class="w-full flex gap-x-2 items-center justify-center" style="height:30rem;">
    <div class="font-semibold whitespace-nowrap">59cm &lt; 10m</div>
    <img src="/images/section-1/station-measurement-distance.jpg" class="rounded h-full"/>
    <img src="/images/section-1/station-measurement-height.jpg" class="rounded h-full"/>
    <div class="font-semibold whitespace-nowrap">402cm (1.5m &lt; inlets &lt; 4m)</div>
</div>

---

<div class="font-semibold w-full text-center mb-4">Next crossroad &gt; 25m</div>

<div class="w-full flex gap-x-2 items-center justify-center" style="height:20rem;">
    <img src="/images/section-1/station-image-north.png" class="rounded h-full"/>
    <img src="/images/section-1/station-image-south.jpg" class="rounded h-full"/>
</div>

---

**Are there any obstacles that could falsify the results?**

---

**Air filters** might falsify the measurements:

<div class="w-full flex gap-x-2 items-center justify-center" style="height:20rem;">
    <img src="/images/section-1/station-image-north.png" class="rounded h-full"/>
    <img src="/images/section-1/station-image-south.jpg" class="rounded h-full"/>
</div>

---

**Air filters** might falsify the measurements:

<div class="w-full flex gap-x-2 items-center justify-center" style="height:20rem;">
    <img src="/images/section-1/station-image-luftfilter.jpg" class="h-full rounded"/>
</div>

---

**Air filters** might falsify the measurements:

<div class="w-full flex gap-x-2 items-center justify-center" style="height:25rem;">
    <img src="/images/section-1/station-image-luftfilter-cropped.jpg" class="h-full rounded"/>
</div>

---

**Do you think that this particular station is representative of the city/for the background?**

---
layout: cover
---

# <uim-microscope class="mr-1"/> Analyze the data

---

## $\text{NO}_2$ measured on march 20th/21st

All 5 Stations reached the highest $\text{NO}_2$ concentration from morning to midday on 21 March.

<br/>

<v-click>

Station with the highest $\text{NO}_2$ concentration: <br/>
<span class="text-red-500 font-semibold">🚗 Landshuter Allee</span>

Station with the lowest $\text{NO}_2$ concentration: <br/>
<span class="text-green-500 font-semibold">🌱 Johanneskirchen</span>

</v-click>

<div class="absolute w-full h-full top-0 left-0 flex items-center justify-center" style="z-index:-10;">
    <img src="/images/section-2/all-stations.png" class="w-full"/>
</div>

<v-click>

<div class="absolute w-full h-full top-0 left-0 flex items-center justify-center" style="z-index:-10;">
    <img src="/images/section-2/all-stations-gap.png" class="w-full"/>
</div>

</v-click>

---

<div class="absolute text-xl text-center" style="top: 27%; right: 1.5rem;">

Station with the highest $\text{NO}_2$ concentration:
<br/><span class="text-red-500 font-semibold">🚗 Landshuter Allee</span>
</div>

<div class="absolute w-full h-full top-0 left-0 flex items-center justify-center" style="z-index:-10;">
    <img src="/images/section-2/map-representative-2.png" class="w-full"/>
</div>

---

<div class="absolute text-xl text-center" style="top: 27%; right: 1.5rem;">

Station with the lowest $\text{NO}_2$ concentration:
<br/><span class="text-green-500 font-semibold">🌱 Johanneskirchen</span>
</div>

<div class="absolute w-full h-full top-0 left-0 flex items-center justify-center" style="z-index:-10;">
    <img src="/images/section-2/map-representative-5.png" class="w-full"/>
</div>

---

<div class="absolute text-xl text-center max-w-sm" style="bottom: 25%; right: 7.5%">

The **traffic data is an average** rather than the actual measurements for the day.

</div>

<div class="absolute w-full h-full top-0 left-0 flex items-center justify-center" style="z-index:-10;">
    <img src="/images/section-2/traffic-data.png" style="width:90%"/>
</div>

---
layout: two-cols
class: text-center
---

**Correlation between $NO_2$ concentration and traffic:**

<img src="/images/section-2/weekday.png" style="height:18rem"/>

One **weekend** day: <br/>
Correlation coefficient $= 0.386$

::right::

<img src="/images/section-2/weekend.png" style="height:18rem; margin-top: 3.5rem;"/>

One **working** day: <br/>
Correlation coefficient $= 0.558$

---

**Interpolating the measured concentrations**

<div class="absolute w-full h-full top-0 left-0 flex items-center justify-center" style="z-index:-10;">
    <img src="/images/section-2/map-process.png" style="width:80%"/>
</div>

<div class="absolute mx-auto bottom-0 grid grid-cols-3 leading-snug text-center" style="z-index:-10; height: 5rem; width: 80%; left: 10%">
<div>5 stations in Munich</div>
<div>Munich map 20km x 20km<br/>Resolution 1km x 1km</div>
<div>Concentration map calculated<br/>with interpolation algorithm</div>
</div>

---

**Interpolating the measured concentrations**

<div class="absolute w-full h-full top-0 left-0 flex items-center justify-center" style="z-index:-10;">
    <img src="/images/section-2/map-matrix.png" style="width:45%" class="mt-12"/>
</div>

---
layout: cover
---

# <uim-graph-bar class="mr-1"/> More data

---

## LFU - Air Quality Data Archive


<v-clicks>

- $\text{NO}_2$, $\text{PM}_{10}$, $\text{PM}_{2.5}$, $\text{O}_{3}$, $\text{CO}$, ...
- 52 Stations in Bavaria
- Hourly data = 8760 data points per station per year
- Since 1980 (not all stations over the whole timespan)

</v-clicks>

<br/>

<v-click>

**Data Source:** https://www.lfu.bayern.de/luft/immissionsmessungen/messwertarchiv

</v-click>

---

<div class="w-full h-full flex justify-center items-center">
    <img src="/images/section-3/luf-website.png" class="w-xl rounded"/>
</div>

<!--
"Daten" -> "Luft" -> "Messwertarchiv"

I will talk about the data license at the end.

-->

---

## LFU - Data Preparation

<v-clicks>

- Replace cells like `?`, `#` or nothing in it with `NaN`
- Remove locations, not of interest
- Merge all data into one CSV file

</v-clicks>

<br/>

<v-click>

In the following, I will only look at **data between 2010 and now** and the station **at Landshuter Allee** from $\textbf{NO}_\textbf{2}$ **concentrations**.

</v-click>


<!--

Optional:
Last signal from Prinzregentenstraße: 20120208
Last signal from Moosach: 20130709

-->

---

<div class="top-0 left-0 absolute flex justify-center items-center w-full h-full">
    <img src="/graphs/alltime_weekly_cycle.png" class="rounded" style="width: 96%"/>
</div>

<div class="right-0 absolute w-1/2 bg-white h-1/2" style="top:27%"></div>

---

<div class="top-0 left-0 absolute flex justify-center items-center w-full h-full">
    <img src="/graphs/alltime_weekly_cycle.png" class="rounded" style="width: 96%"/>
</div>

---

**Findings:**

<v-clicks>

- Daily and weekly cycle
- Shape of the cycle did not change since 2010
- Average concentration has been reduced by 40-50% since 2010

</v-clicks>

<br/>

<v-click>

**Next Question:** Is there a trend by month - certain months with low/high concentrations.

</v-click>

<!--

Since the concentration goes down over the years we should only look at years separately.

We picked 2016, 2017, 2018, and 2019 (the 4 years before the current pandemic).

-->

---

<div class="w-full h-full flex justify-center items-center">
    <img src="/videos/section-3/weekly_cycle_colored_by_month.gif" class="w-2xl rounded"/>
</div>

<div class="absolute font-semibold z-10" style="top: 2rem; left:2rem;"><span class="text-blue-600">Dec/Jan</span> - <span class="text-red-600">Jun/Jul</span></div>

<div class="absolute w-full h-full bg-white top-0 left-0 bg-opacity-90 font-semibold text-black z-0">
    <div class="absolute" style="top: 27.5%; right:57.5%;">2016</div>
    <div class="absolute" style="top: 27.5%; left:57.5%;">2017</div>
    <div class="absolute" style="bottom: 27.5%; right:57.5%;">2018</div>
    <div class="absolute" style="bottom: 27.5%; left:57.5%;">2019</div>
</div>

<!--
The concentration seems to go down in the winter months and tends to rise during summer.
-->

---

<div class="w-full h-full flex justify-center items-center">
    <img src="/videos/section-3/weekly_cycle_colored_by_month.gif" class="w-2xl rounded"/>
</div>

<div class="absolute font-semibold z-10" style="top: 2rem; left:2rem;"><span class="text-blue-600">Dec/Jan</span> - <span class="text-red-600">Jun/Jul</span></div>

---

<div class="w-full h-full flex justify-center items-center">
    <img src="/graphs/mean_monthwise_weekly_cycle_colored_by_month.png" class="w-2xl rounded"/>
</div>

<div class="absolute font-semibold z-10" style="top: 2rem; left:2rem;"><span class="text-blue-600">Dec/Jan</span> - <span class="text-red-600">Jun/Jul</span></div>


<!--

In a still image, this can be seen more clearly. But I made the GIF and wanted to show it too ;)

I down know why the concentration goes down during winter. I did assume with many people on vacation in summer the concentrations should be lower.

Something not uncommon in data science: You assume something and find out that the opposite is true.

-->

---

**Findings:**

<v-clicks>

-   Concentration in summer months tends to be higher than in winter months in the observed period

</v-clicks>

<br/>

<v-click>

**Next Question:** Is there a correlation between weather and concentration.


</v-click>

<!--

LAST QUESTION we want to visit here.

Assumption: People use cars more often when it is cold or when it is raining, i.e. higher concentrations.

-->

---

## DWD - German Climatedata Archive

<v-clicks>

-   Mean temperature, mean pressure, sunshine hours, ...
-   83 stations in Germany
-   Daily data
-   **Munich Airport** data since 1992

</v-clicks>

<br/>

<v-click>

**Data Source:** https://www.dwd.de/DE/leistungen/klimadatendeutschland/klarchivtagmonat ("DWD - Klimadaten Deutschland - Monats- und Tageswerte (Archiv)")

</v-click>

<!--

The DWD website's organization is rather messy so I won't show a picture of how you get there. Here is the Link and the name of that archive.

-->

---

<div class="w-full h-full flex justify-center items-center">
    <img src="/graphs/concentration_over_weather_conditions.png" class="w-2xl rounded"/>
</div>

<div class="absolute font-semibold z-10" style="top: 2rem; left:2rem;"><span class="text-blue-600">2010</span> - <span class="text-red-600">2022</span></div>

<div class="absolute w-full h-full bg-white top-0 left-0 bg-opacity-80 font-semibold text-black z-0">
    <div class="absolute" style="top: 27.5%; right:57.5%;">Temperature</div>
    <div class="absolute" style="top: 27.5%; left:57.5%;">Precipitation</div>
    <div class="absolute" style="bottom: 27.5%; right:57.5%;">Sunshine Hours</div>
    <div class="absolute" style="bottom: 27.5%; left:57.5%;">Wind Speed</div>
</div>

<!--

The good thing: We see a correlation between wind speed and concentration. Higher wind speed -> lower concentration. Molecules get transported away faster.

The interesting thing here is that there is no correlation between temperature/precipitation and concentration.

There is also no more information when looking at individual years.

-->

---

<div class="w-full h-full flex justify-center items-center">
    <img src="/graphs/concentration_over_weather_conditions.png" class="w-2xl rounded"/>
</div>

<div class="absolute font-semibold z-10" style="top: 2rem; left:2rem;"><span class="text-blue-600">2010</span> - <span class="text-red-600">2022</span></div>

---

<div class="absolute font-semibold z-10" style="top: 2rem; left:2rem;"><span class="text-blue-600">2010</span> - <span class="text-red-600">2022</span></div>

<div class="w-full h-full flex justify-center items-center">
    <img src="/graphs/rolling_concentration_over_weather_conditions.png" class="w-2xl rounded"/>
</div>

<!--

I chose to use a rolling mean instead of the best fit line since the best fit line can be dominated by a bulk of points at e.g. 0mm precipitation, 0m/s wind speed, or 0h sunshine.

The only slight trend there is a rising concentration with temperature. Only very minor trends, not very conclusive.

-->

---

One argument for using a car: <v-click><span class="text-green-800 font-semibold">"Not many people want to use a bike or public transport when it's cold or raining outside"</span></v-click>

<v-click>

<span class="text-green-800 font-semibold">Do these findings disprove this argumentation?</span> Is the reason for using a car really the weather or is it mainly habit and each individual's situation?

</v-click>

---

## Licensing and Code Repository

**LUF data** is under `CC 4.0 BY` license.

**DWD data** has no license except for the statement "data is freely available without any restrictions".

<br/>

<v-click>

**Continue this analysis:** Code, cleaned data, plots, and presentation on https://github.com/dostuffthatmatters/esm-lecture-ws21-team-1

</v-click>

<!--

Therefore we can freely share cleaned-up data and all the plots.

If you want to use the same data, here is the link to our open source code which does this preparation and analysis.

Will be open source after 3 pm ;)

-->
