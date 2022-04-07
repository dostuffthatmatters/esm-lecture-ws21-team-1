# Analyzing Air Quality Data in Munich

## Air Quality Data

The `.xlsx` files for NO2 in `implementation/data/raw` were downloaded from the [Bavarian Ministry for Environment](https://www.lfu.bayern.de/luft/immissionsmessungen/messwertarchiv/index.html). The data is licensed under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

The file `implementation/data/LUF_merged.csv` contains all data from Munich between 2010 and now in one CSV file.

<br/>
<br/>

## Weather Data

The file `implementation/data/raw/dwd_klima_flughafen.txt` was downloaded from the [German Weather Service (DWD)](https://www.dwd.de/DE/leistungen/klimadatendeutschland/klarchivtagmonat.html). The data is available without any restrictions (DWD: "no restrictions except when stated", https://www.dwd.de/DE/leistungen/klimadatendeutschland/ueberblick.html?nn=16102&lsbId=526270).

In `implementation/data/DWD_merged.csv` this data has been cleaned up and reduced to the variables of concern.
