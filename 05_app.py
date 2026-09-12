# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Global Seismic Trends",
    page_icon="🌍",
    layout="wide"
)

# Project title
st.title("🌍 Global Seismic Trends")
st.subheader("Data-Driven Earthquake Insights")

# Project description
st.write(
    "Analysis of global earthquake data from 2021 to 2025 "
    "using Python, Pandas, SQL and Streamlit."
)

# Load cleaned earthquake data
df = pd.read_csv(
    "data/cleaned_earthquake_data_2021_2025.csv"
)

# Earthquake overview
st.header("📊 Earthquake Overview")

total_earthquakes = len(df)
strongest_magnitude = df["mag"].max()
deepest_earthquake = df["depth_km"].max()
tsunami_count = df["tsunami"].sum()

# Create four metric columns
col1, col2, col3, col4 = st.columns(4)

# Total earthquakes
with col1:
    st.metric(
        "Total Earthquakes",
        f"{total_earthquakes:,}"
    )

# Strongest magnitude
with col2:
    st.metric(
        "Strongest Magnitude",
        strongest_magnitude
    )

# Deepest earthquake
with col3:
    st.metric(
        "Deepest Earthquake (km)",
        f"{deepest_earthquake:.2f}"
    )

# Tsunami events
with col4:
    st.metric(
        "Tsunami Events",
        int(tsunami_count)
    )

# Earthquakes by year
st.header("📈 Earthquakes by Year")

yearly_count = df.groupby("year").size()

fig1, ax1 = plt.subplots(figsize=(8, 5))

ax1.bar(
    yearly_count.index,
    yearly_count.values
)

ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Earthquakes")
ax1.set_title("Number of Earthquakes by Year")

st.pyplot(fig1)

# Earthquakes by month
st.header("📅 Earthquakes by Month")

monthly_count = df.groupby("month").size()

fig2, ax2 = plt.subplots(figsize=(8, 5))

ax2.bar(
    monthly_count.index,
    monthly_count.values
)

ax2.set_xlabel("Month")
ax2.set_ylabel("Number of Earthquakes")
ax2.set_title("Number of Earthquakes by Month")

st.pyplot(fig2)

# Magnitude distribution
st.header("📊 Magnitude Distribution")

fig3, ax3 = plt.subplots(figsize=(8, 5))

ax3.hist(
    df["mag"].dropna(),
    bins=30
)

ax3.set_xlabel("Magnitude")
ax3.set_ylabel("Number of Earthquakes")
ax3.set_title("Earthquake Magnitude Distribution")

st.pyplot(fig3)

# Depth distribution
st.header("🌋 Depth Distribution")

fig4, ax4 = plt.subplots(figsize=(8, 5))

ax4.hist(
    df["depth_km"].dropna(),
    bins=30
)

ax4.set_xlabel("Depth (km)")
ax4.set_ylabel("Number of Earthquakes")
ax4.set_title("Earthquake Depth Distribution")

st.pyplot(fig4)

# Top 10 countries by earthquake count
st.header("🌎 Top 10 Countries by Earthquake Count")

top_countries = (
    df["country"]
    .dropna()
    .replace("", pd.NA)
    .value_counts()
    .head(10)
)

fig5, ax5 = plt.subplots(figsize=(10, 6))

ax5.barh(
    top_countries.index,
    top_countries.values
)

ax5.set_xlabel("Number of Earthquakes")
ax5.set_ylabel("Country")
ax5.set_title("Top 10 Countries by Earthquake Count")

ax5.invert_yaxis()

st.pyplot(fig5)

# Magnitude versus depth
st.header("🔎 Magnitude vs Depth")

plot_data = df[
    ["mag", "depth_km"]
].dropna()

fig6, ax6 = plt.subplots(figsize=(8, 5))

ax6.scatter(
    plot_data["depth_km"],
    plot_data["mag"],
    alpha=0.4,
    s=10
)

ax6.set_xlabel("Depth (km)")
ax6.set_ylabel("Magnitude")
ax6.set_title("Earthquake Magnitude vs Depth")

st.pyplot(fig6)

# Global earthquake locations
st.header("🗺️ Global Earthquake Locations")

map_data = df[
    ["latitude", "longitude"]
].dropna()

st.map(
    map_data.rename(
        columns={
            "latitude": "lat",
            "longitude": "lon"
        }
    )
)

# Top 10 strongest earthquakes
st.header("💥 Top 10 Strongest Earthquakes")

top_10 = df.nlargest(
    10,
    "mag"
)[
    [
        "id",
        "time",
        "place",
        "mag",
        "depth_km"
    ]
]

st.dataframe(
    top_10,
    use_container_width=True
)

# Footer
st.write("---")

st.write(
    "Data Source: USGS Earthquake Hazards Program"
)

st.write(
    "Project: Global Seismic Trends: Data-Driven Earthquake Insights"
)