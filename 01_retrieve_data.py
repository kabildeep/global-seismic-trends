import requests
import pandas as pd
import time

url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

start_year = 2021
end_year = 2025
min_magnitude = 3

all_records = []

for year in range(start_year, end_year + 1):

    for month in range(1, 13):

        start_date = f"{year}-{month:02d}-01"

        if month == 12:
            end_date = f"{year + 1}-01-01"
        else:
            end_date = f"{year}-{month + 1:02d}-01"

        print(f"Retrieving: {start_date} to {end_date}")

        params = {
            "format": "geojson",
            "starttime": start_date,
            "endtime": end_date,
            "minmagnitude": min_magnitude,
        }

        try:

            response = requests.get(url, params=params, timeout=60)

            response.raise_for_status()

            try:
                data = response.json()

            except ValueError as e:
                print(f"JSON error for {start_date}: {e}")
                continue

            if "features" not in data:
                print(f"No features found for {start_date}")
                continue

            features = data["features"]

            print(f"Records found: {len(features)}")

            for f in features:

                properties = f.get("properties", {})

                geometry = f.get("geometry", {})

                coordinates = geometry.get("coordinates", [])

                if not isinstance(coordinates, list):
                    coordinates = []

                latitude = coordinates[1] if len(coordinates) >= 2 else None

                longitude = coordinates[0] if len(coordinates) >= 1 else None

                depth_km = coordinates[2] if len(coordinates) >= 3 else None

                record = {
                    "id": f.get("id"),
                    "time": pd.to_datetime(
                        properties.get("time"), unit="ms", errors="coerce"
                    ),
                    "updated": pd.to_datetime(
                        properties.get("updated"), unit="ms", errors="coerce"
                    ),
                    "latitude": latitude,
                    "longitude": longitude,
                    "depth_km": depth_km,
                    "mag": properties.get("mag"),
                    "magType": properties.get("magType"),
                    "place": properties.get("place"),
                    "status": properties.get("status"),
                    "tsunami": properties.get("tsunami"),
                    "sig": properties.get("sig"),
                    "net": properties.get("net"),
                    "nst": properties.get("nst"),
                    "dmin": properties.get("dmin"),
                    "rms": properties.get("rms"),
                    "gap": properties.get("gap"),
                    "magError": properties.get("magError"),
                    "depthError": properties.get("depthError"),
                    "magNst": properties.get("magNst"),
                    "locationSource": properties.get("locationSource"),
                    "magSource": properties.get("magSource"),
                    "types": properties.get("types"),
                    "ids": properties.get("ids"),
                    "sources": properties.get("sources"),
                    "type": properties.get("type"),
                }

                all_records.append(record)

        except requests.exceptions.Timeout:

            print(f"Timeout error for {start_date}")
            continue

        except requests.exceptions.ConnectionError:

            print(f"Connection error for {start_date}")
            continue

        except requests.exceptions.HTTPError as e:

            print(f"HTTP error for {start_date}: {e}")
            continue

        except requests.exceptions.RequestException as e:

            print(f"Request error for {start_date}: {e}")
            continue

        except Exception as e:

            print(f"Unexpected error for {start_date}: {e}")
            continue

        time.sleep(1)


df = pd.DataFrame(all_records)


print()
print("----------------------------------------")
print("DATA RETRIEVAL COMPLETED")
print("----------------------------------------")

print("Total records retrieved:", len(df))


if df.empty:

    print("ERROR: No earthquake data was retrieved.")

    raise SystemExit


df = df.drop_duplicates(subset=["id"])


df = df.sort_values("time").reset_index(drop=True)


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

    df[column] = df[column].astype("string")


output_file = "global_earthquake_data_2021_2025.csv"


df.to_csv(output_file, index=False)


print("Final records:", len(df))

print("Final columns:", len(df.columns))

print()
print("Columns:")
print(df.columns.tolist())

print()
print("Dataset shape:")
print(df.shape)

print()
print("First 5 records:")
print(df.head())

print()
print("Data types:")
print(df.dtypes)

print()
print("Missing values:")
print(df.isnull().sum())

print()
print(f"File saved successfully: {output_file}")
