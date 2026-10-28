import streamlit as st
import pandas as pd # data manipulation
import plotly.express as px # data visualization
from pathlib import Path

# Dictionaries, Pandas Dataframes, Streamlit - Tuesday - Sep 8th 2026
# go.fiu.edu/ttafall2026
# to run: streamlit run name_of_file.py
# if it doesn't work, try: python -m streamlit run name_of_file.py

st.title("Water Quality Dashboard")
st.header("CIS 3590 - Internship-Ready Software Development")
st.subheader("Prof. Gregory Reis")

# DESCRIPTION
st.write("Explore water quality readings collected by an autonomous underwater vehicle in Biscayne Bay on February 4, 2022.")

st.divider()

st.sidebar.header("File Upload")
st.sidebar.info("Upload a CSV file with water quality data.")

uploaded_file = st.sidebar.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

# Locate the folder where main.py is stored.
BASE_DIR = Path(__file__).resolve().parent

# Default dataset expected in the same folder as main.py.
DEFAULT_CSV_PATH = BASE_DIR / "biscayneBay_waterquality.csv"

# Load the uploaded CSV if available; otherwise use the local default dataset.
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("Uploaded CSV loaded successfully.")

elif DEFAULT_CSV_PATH.exists():
    df = pd.read_csv(DEFAULT_CSV_PATH)
    st.sidebar.success("Default Biscayne Bay dataset loaded successfully.")

else:
    st.error("No CSV data is available.")
    st.info(
        "Upload a CSV file in the sidebar, or place "
        "'biscayneBay_waterquality.csv' in the same folder as main.py."
    )
    st.code(f"Expected default file location:\n{DEFAULT_CSV_PATH}")
    st.stop()

# Clean up column names in case the CSV has accidental spaces.
df.columns = df.columns.str.strip()

# Drop columns that are completely empty (e.g., "ROSEM Command Type").
df = df.dropna(axis=1, how="all")

tables, plots, maps = st.tabs([
    "Data",
    "Charts",
    "Maps"
])

with tables:
    st.subheader("Water Quality Data")
    # DESCRIPTION
    st.write("Every reading recorded during the survey, with one row per second.")
    st.dataframe(df, use_container_width=True)

    st.subheader("Descriptive Statistics")
    # DESCRIPTION
    st.write("Summary values such as the mean, minimum, and maximum for each column.")
    st.dataframe(df.describe(), use_container_width=True)

    st.subheader("Custom View")
    # DESCRIPTION
    st.write("Choose only the columns you care about to build a smaller, focused table.")
    selected_columns = st.multiselect(
        "Select columns to display",
        options=df.columns.tolist(),
        default=df.columns.tolist()
    )

    if selected_columns:
        st.subheader("Selected Columns")
        st.dataframe(df[selected_columns], use_container_width=True)
    else:
        st.warning("Select at least one column to display.")

with plots:
    st.subheader("Line Chart")
    # DESCRIPTION
    st.write("Pick a measurement to see how it changed over the course of the survey.")
    parameter = st.selectbox("Select a parameter",options=df.columns.tolist())

    fig1 = px.line(df,
                   x="Time",
                   y=parameter,
                   title=f"{parameter} over Time")
    st.plotly_chart(fig1)

    st.subheader("Temperature vs Salinity")
    # DESCRIPTION
    st.write("Each point is one reading, showing how water temperature relates to salinity.")
    fig2 = px.scatter(df,
                      x = "Temperature (c)",
                      y = "Salinity (ppt)",
                      title = "Temperature vs Salinity")
    st.plotly_chart(fig2)

    st.subheader("Bay Floor in 3D")
    # DESCRIPTION
    st.write("Water depth plotted by location to give a rough shape of the bay floor; drag to rotate the view.")
    fig3 =px.scatter_3d(df,
                        x = "Longitude",
                        y = "Latitude",
                        z = "Total Water Column (m)",
                        title = "3D Visualization of the Bay Floor")
    fig3.update_scenes(zaxis_autorange="reversed")
    fig3.update_traces(marker_size=3)
    st.plotly_chart(fig3)
with maps:
    st.subheader("Maps")
    # DESCRIPTION
    st.write("The vehicle's path through the bay, with each point colored by water temperature.")
    first_map = px.scatter_map(df,
                               lat = "Latitude",
                               lon = "Longitude",
                               title = "Vehicle Track on a Map",
                               center = {"lat": 25.9121, "lon": -80.1371},
                               zoom = 16,
                               color = "Temperature (c)",
                               color_continuous_scale = "Viridis")

    st.plotly_chart(first_map)