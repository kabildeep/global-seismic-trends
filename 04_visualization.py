# 1. Load cleaned earthquake data

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_earthquake_data_2021_2025.csv")


# 2. Earthquakes by year

yearly_count = df.groupby("year").size()

plt.figure(figsize=(8, 5))
plt.bar(yearly_count.index, yearly_count.values)

plt.xlabel("Year")
plt.ylabel("Number of Earthquakes")
plt.title("Number of Earthquakes by Year")

plt.tight_layout()
plt.show()


# 3. Earthquakes by month

monthly_count = df.groupby("month").size()

plt.figure(figsize=(8, 5))
plt.bar(monthly_count.index, monthly_count.values)

plt.xlabel("Month")
plt.ylabel("Number of Earthquakes")
plt.title("Number of Earthquakes by Month")

plt.tight_layout()
plt.show()


# 4. Earthquake magnitude distribution

plt.figure(figsize=(8, 5))
plt.hist(df["mag"].dropna(), bins=30)

plt.xlabel("Magnitude")
plt.ylabel("Number of Earthquakes")
plt.title("Earthquake Magnitude Distribution")

plt.tight_layout()
plt.show()


# 5. Earthquake depth distribution

plt.figure(figsize=(8, 5))
plt.hist(df["depth_km"].dropna(), bins=30)

plt.xlabel("Depth (km)")
plt.ylabel("Number of Earthquakes")
plt.title("Earthquake Depth Distribution")

plt.tight_layout()
plt.show()


# 6. Top 10 countries by earthquake count

top_countries = (
    df["country"]
    .dropna()
    .replace("", pd.NA)
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10, 6))
plt.barh(top_countries.index, top_countries.values)

plt.xlabel("Number of Earthquakes")
plt.ylabel("Country")
plt.title("Top 10 Countries by Earthquake Count")

plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()


# 7. Earthquake magnitude versus depth

plot_data = df[["mag", "depth_km"]].dropna()

plt.figure(figsize=(8, 5))
plt.scatter(
    plot_data["depth_km"],
    plot_data["mag"],
    alpha=0.4,
    s=10
)

plt.xlabel("Depth (km)")
plt.ylabel("Magnitude")
plt.title("Earthquake Magnitude vs Depth")

plt.tight_layout()
plt.show()


# 8. Earthquakes by day of week

day_count = df["day_of_week"].value_counts()

day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

day_count = day_count.reindex(day_order).fillna(0)

plt.figure(figsize=(9, 5))
plt.bar(day_count.index, day_count.values)

plt.xlabel("Day of Week")
plt.ylabel("Number of Earthquakes")
plt.title("Earthquakes by Day of Week")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# 9. Earthquakes by depth category

depth_category_count = df["depth_category"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(
    depth_category_count.index,
    depth_category_count.values
)

plt.xlabel("Depth Category")
plt.ylabel("Number of Earthquakes")
plt.title("Earthquakes by Depth Category")

plt.xticks(rotation=30)

plt.tight_layout()
plt.show()


# 10. Earthquakes by magnitude category

magnitude_category_count = df["magnitude_category"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(
    magnitude_category_count.index,
    magnitude_category_count.values
)

plt.xlabel("Magnitude Category")
plt.ylabel("Number of Earthquakes")
plt.title("Earthquakes by Magnitude Category")

plt.xticks(rotation=30)

plt.tight_layout()
plt.show()


# 11. Top 10 strongest earthquakes

top_10 = df.nlargest(10, "mag")

plt.figure(figsize=(10, 6))
plt.barh(
    top_10["place"].astype(str),
    top_10["mag"]
)

plt.xlabel("Magnitude")
plt.ylabel("Location")
plt.title("Top 10 Strongest Earthquakes")

plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()