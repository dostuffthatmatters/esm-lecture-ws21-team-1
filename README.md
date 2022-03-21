# Analyzing Air Quality Data in Munich

The `.xlsx` files for $NO_2$ in `implementation/data/raw` were downloaded from the [Bavarian Ministry for Environment](https://www.lfu.bayern.de/luft/immissionsmessungen/messwertarchiv/index.html).

The data is licensed under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

The file `implementation/data/LUF_merged.csv` contains all data from Munich between 2010 and now in one CSV file.

<br/>
<br/>

The file `implementation/data/raw/dwd_klima_flughafen.txt` was downloaded from the [German Weather Service (DWD)](https://www.dwd.de/DE/leistungen/klimadatendeutschland/klarchivtagmonat.html).

The data is available without any restrictions.

In `implementation/data/DWD_merged.csv` this data has been cleaned up and reduced to the variables of concern.

<br/>
<br/>

## Data Unit Conversion

Units of $NO_2$ converted from $\mu g/m^3$ to $ppb$.

$$
M_{NO_2} = 46 \; \frac{g}{\text{mol}}
\\[4pt]
1 \; \frac{\mu g}{m^3} \;\; \hat{=} \;\; 21.7 \cdot 10^{-9} \; \frac{\text{mol}}{m^3}
$$

Mixed in dry air:

$$
n_{\text{air}} = 41.6 \; \frac{\text{mol}}{m^3}
\\[4pt]
X_{NO_2} {\Big|}_{1 \frac{\mu g}{m^3}} = 0.5216 \; \text{ppb}
$$
