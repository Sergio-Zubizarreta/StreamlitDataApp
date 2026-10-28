# Water Quality Dashboard

An interactive Streamlit web app for exploring water quality data collected in Biscayne Bay, Miami, FL. Built for **CIS 3590 – Internship-Ready Software Development** (Prof. Gregory Reis) at FIU.

**Live app:** [YOUR-APP-NAME.streamlit.app](https://YOUR-APP-NAME.streamlit.app) <!-- replace after deploying -->

## Purpose

The app lets users explore a real environmental dataset without writing any code. Users can view the raw data and summary statistics, pick which measurements to chart, and see where each reading was taken on a map. The goal is to make it easy to spot patterns, such as how temperature relates to salinity or how depth changes across the survey area.

## Dataset

**File:** `biscayneBay\_waterquality.csv` (included in this repository)

* Collected on **February 4, 2022**, between roughly 4:18 PM and 4:34 PM, in northern Biscayne Bay.
* **941 rows** (one reading per second) and **69 columns**.
* Data was recorded by an autonomous underwater vehicle carrying a water quality sensor. Each row includes:

  * **Location:** Latitude, Longitude
  * **Water quality:** Temperature (°C), Salinity (ppt), pH, Dissolved Oxygen (ODO mg/L and % saturation), Turbidity (NTU), Chlorophyll (µg/L), Blue-green algae (cells/mL)
  * **Depth:** Total water column (m)
  * **Vehicle telemetry:** speed, heading, battery, fin positions, and so on

## Features

|Tab|What it shows|
|-|-|
|**Data**|The full dataset, descriptive statistics, and a column picker to show only the columns you want|
|**Charts**|A line chart of any parameter over time, a Temperature vs. Salinity scatter plot, and a 3D view of the bay floor|
|**Maps**|The vehicle's path on an interactive map, colored by water temperature|

All charts are interactive Plotly charts: hover to see exact values, drag to zoom, and double-click to reset the view.

## How to Use the App

1. Open the live app link above. The Biscayne Bay dataset loads automatically.
2. *(Optional)* Upload your own CSV from the **sidebar**. It needs the same column names as the default dataset for the charts to work.
3. In the **Data** tab, use the **"Select columns to display"** box to choose which columns appear in the table.
4. In the **Charts** tab, use the **"Select a parameter"** dropdown to change what the line chart plots.
5. In the **Maps** tab, hover over points to see the location and temperature of each reading.

## Running Locally

Requires Python 3.13 or newer.

```bash
git clone https://github.com/Sergio-Zubizarreta/StreamlitDataApp.git
cd StreamlitDataApp
pip install -r requirements.txt
streamlit run main.py
```

If `streamlit` isn't recognized as a command, use `python -m streamlit run main.py` instead.

## Project Structure

```
├── main.py                         # Streamlit app
├── biscayneBay\_waterquality.csv    # Default dataset
├── requirements.txt                # Python dependencies
├── pyproject.toml / uv.lock        # uv project files
└── README.md
```

## Tech Stack

* [Streamlit](https://streamlit.io/): web app framework
* [Pandas](https://pandas.pydata.org/): data loading and manipulation
* [Plotly Express](https://plotly.com/python/plotly-express/): interactive charts

