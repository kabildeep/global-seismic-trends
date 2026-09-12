import pandas as pd
import re

input_file = "data/global_earthquake_data_2021_2025.csv"
output_file = "data/cleaned_earthquake_data_2021_2025.csv"

df = pd.read_csv(input_file)

print("Original shape:", df.shape)

print()
print("Original columns:")
print(df.columns.tolist())


# Convert datetime columns

df["time"] = pd.to_datetime(df["time"], errors="coerce")
df["updated"] = pd.to_datetime(df["updated"], errors="coerce")


# Convert numeric columns

numeric_columns = [
    "latitude",
    "longitude",
    "depth_km",
    "mag",
    "tsunami",
    "sig",
    "nst",
    "dmin",
    "rms",
    "gap",
    "magError",
    "depthError",
    "magNst",
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")


# Clean string columns

string_columns = [
    "id",
    "magType",
    "place",
    "status",
    "net",
    "locationSource",
    "magSource",
    "types",
    "ids",
    "sources",
    "type",
]

for column in string_columns:
    df[column] = df[column].astype("string").str.strip()


# Remove duplicate earthquake IDs

df = df.drop_duplicates(subset=["id"])


# Extract country from place using Regex

def extract_country(place):

    if pd.isna(place):
        return pd.NA

    match = re.search(r",\s*([^,]+)$", str(place))

    if match:
        return match.group(1).strip()

    return pd.NA


df["country"] = df["place"].apply(extract_country)


# Create time-based derived columns

df["year"] = df["time"].dt.year
df["month"] = df["time"].dt.month
df["day"] = df["time"].dt.day
df["day_of_week"] = df["time"].dt.day_name()


# Create depth category

df["depth_category"] = df["depth_km"].apply(
    lambda x: "Shallow" if x < 70 else "Deep"
    if pd.notna(x) else pd.NA
)


# Create magnitude category

def magnitude_category(magnitude):

    if pd.isna(magnitude):
        return pd.NA

    if magnitude < 5:
        return "Moderate"

    elif magnitude < 7:
        return "Strong"

    else:
        return "Major"


df["magnitude_category"] = df["mag"].apply(magnitude_category)


# Sort data by earthquake time

df = df.sort_values("time").reset_index(drop=True)


# Display final information

print()
print("----------------------------------------")
print("DATA CLEANING COMPLETED")
print("----------------------------------------")

print("Final shape:", df.shape)

print()
print("Final columns:")
print(df.columns.tolist())

print()
print("Missing values:")
print(df.isnull().sum())

print()
print("Depth categories:")
print(df["depth_category"].value_counts(dropna=False))

print()
print("Magnitude categories:")
print(df["magnitude_category"].value_counts(dropna=False))

print()
print("Sample data:")
print(df.head())


# Save cleaned dataset

df.to_csv(output_file, index=False)

print()
print(f"Cleaned dataset saved successfully: {output_file}")