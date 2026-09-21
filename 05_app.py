# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Global Seismic Trends", page_icon="🌍", layout="wide")

# Project title
st.title("Global Seismic Trends")
st.subheader("Data-Driven Earthquake Insights")

# Project description
st.write(
    "Analysis of global earthquake data from 2021 to 2025 "
    "using Python, Pandas, SQL and Streamlit."
)

# Load cleaned earthquake data
df = pd.read_csv("data/cleaned_earthquake_data_2021_2025.csv")


# EARTHQUAKE OVERVIEW


st.header("Earthquake Overview")

total_earthquakes = len(df)
strongest_magnitude = df["mag"].max()
deepest_earthquake = df["depth_km"].max()
tsunami_count = df["tsunami"].sum()

# Create four metric columns
col1, col2, col3, col4 = st.columns(4)

# Total earthquakes
with col1:
    st.metric("Total Earthquakes", f"{total_earthquakes:,}")

# Strongest magnitude
with col2:
    st.metric("Strongest Magnitude", strongest_magnitude)

# Deepest earthquake
with col3:
    st.metric("Deepest Earthquake (km)", f"{deepest_earthquake:.2f}")

# Tsunami events
with col4:
    st.metric("Tsunami Events", int(tsunami_count))


# EARTHQUAKES BY YEAR

st.header("Earthquakes by Year")

yearly_count = df.groupby("year").size()

fig1, ax1 = plt.subplots(figsize=(8, 5))

ax1.bar(yearly_count.index, yearly_count.values)

ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Earthquakes")
ax1.set_title("Number of Earthquakes by Year")

st.pyplot(fig1)

# Insight
highest_year = yearly_count.idxmax()
highest_year_count = yearly_count.max()

lowest_year = yearly_count.idxmin()
lowest_year_count = yearly_count.min()

st.info(
    f"Insight: {highest_year} recorded the highest number of earthquakes "
    f"with {highest_year_count:,} events. "
    f"{lowest_year} recorded the lowest number with "
    f"{lowest_year_count:,} events."
)

# EARTHQUAKES BY MONTH

st.header("Earthquakes by Month")

monthly_count = df.groupby("month").size()

fig2, ax2 = plt.subplots(figsize=(8, 5))

ax2.bar(monthly_count.index, monthly_count.values)

ax2.set_xlabel("Month")
ax2.set_ylabel("Number of Earthquakes")
ax2.set_title("Number of Earthquakes by Month")

st.pyplot(fig2)

# Insight
highest_month = monthly_count.idxmax()
highest_month_count = monthly_count.max()

lowest_month = monthly_count.idxmin()
lowest_month_count = monthly_count.min()

st.info(
    f"Insight: Month {highest_month} recorded the highest number "
    f"of earthquakes with {highest_month_count:,} events. "
    f"Month {lowest_month} recorded the lowest number with "
    f"{lowest_month_count:,} events."
)


# MAGNITUDE DISTRIBUTION

st.header("Magnitude Distribution")

fig3, ax3 = plt.subplots(figsize=(8, 5))

ax3.hist(df["mag"].dropna(), bins=30)

ax3.set_xlabel("Magnitude")
ax3.set_ylabel("Number of Earthquakes")
ax3.set_title("Earthquake Magnitude Distribution")

st.pyplot(fig3)

# Insight
average_magnitude = df["mag"].mean()
median_magnitude = df["mag"].median()
minimum_magnitude = df["mag"].min()
maximum_magnitude = df["mag"].max()

st.info(
    f"Insight: The average earthquake magnitude is "
    f"{average_magnitude:.2f}, while the median magnitude is "
    f"{median_magnitude:.2f}. "
    f"The magnitude ranges from {minimum_magnitude:.2f} "
    f"to {maximum_magnitude:.2f}. "
    f"Most recorded earthquakes are concentrated at lower magnitudes."
)

# DEPTH DISTRIBUTION

st.header("Depth Distribution")

fig4, ax4 = plt.subplots(figsize=(8, 5))

ax4.hist(df["depth_km"].dropna(), bins=30)

ax4.set_xlabel("Depth (km)")
ax4.set_ylabel("Number of Earthquakes")
ax4.set_title("Earthquake Depth Distribution")

st.pyplot(fig4)

# Insight
average_depth = df["depth_km"].mean()
median_depth = df["depth_km"].median()

shallow_count = (df["depth_km"] < 70).sum()

deep_count = (df["depth_km"] >= 70).sum()

st.info(
    f"Insight: The average earthquake depth is "
    f"{average_depth:.2f} km and the median depth is "
    f"{median_depth:.2f} km. "
    f"There are {shallow_count:,} shallow earthquakes "
    f"and {deep_count:,} earthquakes at depths of 70 km or more."
)

# TOP 10 COUNTRIES BY EARTHQUAKE COUNT

st.header("Top 10 Countries by Earthquake Count")

top_countries = df["country"].dropna().replace("", pd.NA).value_counts().head(10)

fig5, ax5 = plt.subplots(figsize=(10, 6))

ax5.barh(top_countries.index, top_countries.values)

ax5.set_xlabel("Number of Earthquakes")
ax5.set_ylabel("Country")
ax5.set_title("Top 10 Countries by Earthquake Count")

ax5.invert_yaxis()

st.pyplot(fig5)

# Insight
top_country = top_countries.index[0]
top_country_count = top_countries.iloc[0]

st.info(
    f"Insight: {top_country} has the highest number of recorded "
    f"earthquakes among the countries identified in the dataset, "
    f"with {top_country_count:,} events."
)

# MAGNITUDE VS DEPTH

st.header("Magnitude vs Depth")

plot_data = df[["mag", "depth_km"]].dropna()

fig6, ax6 = plt.subplots(figsize=(8, 5))

ax6.scatter(plot_data["depth_km"], plot_data["mag"], alpha=0.4, s=10)

ax6.set_xlabel("Depth (km)")
ax6.set_ylabel("Magnitude")
ax6.set_title("Earthquake Magnitude vs Depth")

st.pyplot(fig6)

# Insight
correlation = plot_data["depth_km"].corr(plot_data["mag"])

st.info(
    f"Insight: The correlation between earthquake depth "
    f"and magnitude is {correlation:.2f}. "
    f"The scatter plot shows the relationship between "
    f"earthquake depth and magnitude."
)

# GLOBAL EARTHQUAKE LOCATIONS

st.header("Global Earthquake Locations")

map_data = df[["latitude", "longitude"]].dropna()

st.map(map_data.rename(columns={"latitude": "lat", "longitude": "lon"}))

# Insight
st.info(
    f"Insight: The map displays {len(map_data):,} earthquake "
    f"locations with valid latitude and longitude values, "
    f"showing the geographical distribution of earthquake activity."
)
# TOP 10 STRONGEST EARTHQUAKES

st.header("Top 10 Strongest Earthquakes")

top_10 = df.nlargest(10, "mag")[["id", "time", "place", "mag", "depth_km"]]

st.dataframe(top_10, use_container_width=True)

# Insight
strongest_event = top_10.iloc[0]

st.info(
    f"Insight: The strongest earthquake in the dataset "
    f"had a magnitude of {strongest_event['mag']:.2f}. "
    f"It was recorded at {strongest_event['place']}."
)

# FOOTER

st.write("---")

st.write("Data Source: USGS Earthquake Hazards Program")

st.write("Project: Global Seismic Trends: " "Data-Driven Earthquake Insights")
