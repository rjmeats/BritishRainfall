# Mapping Daily Weather Report Stations to Rainfall Rescue (British Rainfall) stations

In January 2024, Ed Hawkins and Philip Craig released digitised observations from the 1861-1875 Met Office Daily Weather Reports, transcribed by volunteers in 2019 using the Zooniverse platform.

* [Digitizing observations from the 1861–1875 Met Office Daily Weather Reports using citizen scientist volunteers](https://rmets.onlinelibrary.wiley.com/doi/full/10.1002/gdj3.236)
* [Weather Rescue Data v2.1](https://zenodo.org/records/8057546)

The rescued observations include daily rainfall figures from a few tens of stations in Great Britain and Ireland and some nearby countries. 

This note records how the DWR rainfall stations relate to the British Rainfall monthly rainfall stations in Great Britain and Ireland, mostly by a combination of:
* identifying British Rainfall stations with 'Met Council' or similar as the observer in the British Rainfall almanacs or on the ten-year rainfall sheets. These first appear in the 1877 edition of British Rainfall.
* aggregating the DWR daily rainfall into monthly figures and comparing these with the British Rainfall values from the Rainfall Rescue project
* some station history information provided with the digitised observations, and in early Met Office Annual Reports

## DWR Stations with no related British Rainfall Station

These are nearly all stations which had stopped appearing in the DWRs by 1875, i.e. before the Met Office began supplying records to British Rainfall in 1877:

Aberdeen, Berwick, Cape Clear, Galway, Greencastle (initial site), Holyhead (initial site), Jersey, London (Westminster sites), Milford Haven, Penzance, Plymouth (initial site), Portland, Portrush, Portsmouth, Queenstown, Wick (initial site)

## DWR Stations active by 1875 but only appearing later in British Rainfall

A lot of the DWR stations which have rainfall in the rescued 1861–1875 data-set only appear in British Rainfall from 1877 onwards (i.e. slightly after the data-set finishes) at the point where the Met Office began supplying its rainfall records to British Rainfall, with no back-filling. British Rainfall gives 'The Meteorological Council' as observer for these records.

|DWR Station|British Rainfall Station|
|-----------|-----------------------|
|Dover|Two 'leftover' Kent sheets: [1870s](https://github.com/ed-hawkins/rainfall-rescue-leftover/blob/main/DATA/Kent/TYRain_1870-1879_01_pt3-page-025.jpg) and [1880s](https://github.com/ed-hawkins/rainfall-rescue-leftover/blob/main/DATA/Kent/TYRain_1880-1889_02_pt1-page-021.jpg)|
|Holyhead (Sailor's Home site)|[HOLYHEAD](https://github.com/ed-hawkins/rainfall-rescue/tree/master/DATA/HOLYHEAD)|
|Hurst Castle|[HURST-CASTLE](https://github.com/ed-hawkins/rainfall-rescue/tree/master/DATA/HURST-CASTLE)|
|Leith|[LEITH](https://github.com/ed-hawkins/rainfall-rescue/tree/master/DATA/LEITH)|
|Moville (successor to Greencastle)|[MOVILLE-PROSPECT-VILLA](https://github.com/ed-hawkins/rainfall-rescue-data-eire/tree/main/DATA/MOVILLE-PROSPECT-VILLA)|
|Portishead|One 'leftover' Somerset sheet: [1870s](https://github.com/ed-hawkins/rainfall-rescue-leftover/blob/main/DATA/Somerset/TYRain_1870-1879_05_pt3-page-021.jpg)|
|Roche's Point|[ROCHES-POINT](https://github.com/ed-hawkins/rainfall-rescue/tree/master/DATA/ROCHES-POINT)|
|Scarborough|[SCARBOROUGH-MIX](https://github.com/ed-hawkins/rainfall-rescue/tree/master/DATA/SCARBOROUGH-MIX)|
|Shields|[NORTH-SHIELDS-POST-OFFICE](https://github.com/ed-hawkins/rainfall-rescue/tree/master/DATA/NORTH-SHIELDS-POST-OFFICE)|
|Stornoway|[STORNOWAY-MIX](https://github.com/ed-hawkins/rainfall-rescue/tree/master/DATA/STORNOWAY-MIX)|
|Sumburgh|[SUMBURGHEAD-DUNROSSNESS](https://github.com/ed-hawkins/rainfall-rescue/tree/master/DATA/SUMBURGHEAD-DUNROSSNESS)|
|Thurso|One 'leftover' Caithness sheet: [1870s](https://github.com/ed-hawkins/rainfall-rescue-leftover/blob/main/DATA/Caithness/TYRain_1870-1879_12_pt3-page-100.jpg)|
|Wick (Market Place site)|[WICK-COASTGUARD-STATION](WICK-COASTGUARD-STATION)|
|Yarmouth (Sailor's Home site)|[YARMOUTH-SAILORS-HOME.csv](https://github.com/ed-hawkins/rainfall-rescue/tree/master/DATA/YARMOUTH-SAILORS-HOME)|

## DWR Stations active by 1875 but only appearing later in British Rainfall

The remaining DWR rainfall stations in the 1861–1875 data-set have aggregate monthly rainfall figures that match up at least partially with a British Rainfall monthly rainfall station. 

A comparison spreadsheet for each site compares the month-by-month DWR 1861-1875 and British Rainfall (BR) figures, with exact matches shown in bright green, and near matches (< 0.1 inch difference) in pale green. 

|DWR Station|British Rainfall Station|Comparison|Notes|
|-----------|-----------------------|----------|-----|
||||
|Cambridge|[CAMBRIDGE-OBSERVATORY](https://github.com/ed-hawkins/rainfall-rescue/tree/master/DATA/CAMBRIDGE-OBSERVATORY)|[Link](Comparisons/CAMBRIDGE-DWR-1861-1875-Comparison.xlsx)|Inland institutional site added to the DWR in July 1872. Good match for most months.|
|Nottingham|[NOTTINGHAM-HIGHFIELD-HOUSE](https://github.com/ed-hawkins/rainfall-rescue/tree/master/DATA/NOTTINGHAM-HIGHFIELD-HOUSE)|[Link](Comparisons/NOTTINGHAM-DWR-1861-1875-Comparison.xlsx)|Inland institutional site added to the DWR in July 1872. BR readings for 1875 match well, are missing for 1873 and 1874, and don't match for 1872.|
|Oxford|[OXFORD-RADCLIFFE](https://github.com/ed-hawkins/rainfall-rescue/tree/master/DATA/OXFORD-RADCLIFFE)|[Link](Comparisons/OXFORD-DWR-1861-1875-Comparison.xlsx)|Inland institutional site added to the DWR in July 1872. Good match for most months to the 'Lawns' series.|
|York|[YORK-MUSEUM](https://github.com/ed-hawkins/rainfall-rescue/tree/master/DATA/YORK-MUSEUM)|[Link](Comparisons/YORK-DWR-1861-1875-Comparison.xlsx)|Inland institutional site added to the DWR in July 1872. Readings for 1873, the start of 1874 and 1875, but don't match well for most of 1874. There are no BR readings for 1872.|
||||
||||

.. to be completed ..

