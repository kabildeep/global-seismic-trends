USE global_seismic_db;

DESCRIBE earthquakes;

-- Q1. Top 10 strongest earthquakes

SELECT
    id,
    time,
    place,
    mag,
    depth_km
FROM earthquakes
ORDER BY mag DESC
LIMIT 10;

-- Q2. Top 10 deepest earthquakes

SELECT
    id,
    time,
    place,
    mag,
    depth_km
FROM earthquakes
ORDER BY depth_km DESC
LIMIT 10;

-- Q3. Shallow earthquakes below 50 km with magnitude greater than 7.5

SELECT
    id,
    time,
    place,
    mag,
    depth_km
FROM earthquakes
WHERE depth_km < 50
  AND mag > 7.5
ORDER BY mag DESC;

-- Q5. Average magnitude for each magnitude type

SELECT
    magType,
    AVG(mag) AS average_magnitude
FROM earthquakes
GROUP BY magType
ORDER BY average_magnitude DESC;

-- Q6. Year with the most earthquakes

SELECT
    year,
    COUNT(*) AS earthquake_count
FROM earthquakes
GROUP BY year
ORDER BY earthquake_count DESC
LIMIT 1;

-- Q7. Month with the highest number of earthquakes

SELECT
    month,
    COUNT(*) AS earthquake_count
FROM earthquakes
GROUP BY month
ORDER BY earthquake_count DESC
LIMIT 1;

-- Q8. Day of week with the most earthquakes

SELECT
    day_of_week,
    COUNT(*) AS earthquake_count
FROM earthquakes
GROUP BY day_of_week
ORDER BY earthquake_count DESC
LIMIT 1;

-- Q9. Number of earthquakes by hour of the day

SELECT
    HOUR(STR_TO_DATE(time, '%Y-%m-%d %H:%i:%s.%f')) AS earthquake_hour,
    COUNT(*) AS earthquake_count
FROM earthquakes
GROUP BY earthquake_hour
ORDER BY earthquake_hour;

-- Q10. Most active reporting network

SELECT
    net,
    COUNT(*) AS earthquake_count
FROM earthquakes
GROUP BY net
ORDER BY earthquake_count DESC
LIMIT 1;

-- Q14. Count of reviewed versus automatic earthquakes

SELECT
    status,
    COUNT(*) AS earthquake_count
FROM earthquakes
GROUP BY status
ORDER BY earthquake_count DESC;

-- Q15. Number of earthquakes by earthquake type

SELECT
    type,
    COUNT(*) AS earthquake_count
FROM earthquakes
GROUP BY type
ORDER BY earthquake_count DESC;

-- Q16. Number of earthquakes by data type

SELECT
    types,
    COUNT(*) AS earthquake_count
FROM earthquakes
GROUP BY types
ORDER BY earthquake_count DESC;

-- Q18. Earthquakes with high station coverage
-- Threshold: more than 100 stations

SELECT
    id,
    time,
    place,
    mag,
    nst
FROM earthquakes
WHERE nst > 100
ORDER BY nst DESC;

-- Q19. Number of tsunamis triggered per year

SELECT
    year,
    COUNT(*) AS tsunami_count
FROM earthquakes
WHERE tsunami = 1
GROUP BY year
ORDER BY year;

-- Q21. Top 5 countries with the highest average magnitude

SELECT
    country,
    AVG(mag) AS average_magnitude
FROM earthquakes
WHERE country IS NOT NULL
  AND country <> ''
GROUP BY country
ORDER BY average_magnitude DESC
LIMIT 5;


-- Q22. Countries that experienced both shallow and deep earthquakes
-- in the same month

SELECT
    country,
    year,
    month
FROM earthquakes
WHERE country IS NOT NULL
  AND country <> ''
GROUP BY country, year, month
HAVING
    SUM(CASE WHEN depth_km < 50 THEN 1 ELSE 0 END) > 0
    AND
    SUM(CASE WHEN depth_km > 300 THEN 1 ELSE 0 END) > 0
ORDER BY country, year, month;

-- Q23. Year-over-year growth rate in total earthquakes

WITH yearly_counts AS (
    SELECT
        year,
        COUNT(*) AS earthquake_count
    FROM earthquakes
    GROUP BY year
),
growth AS (
    SELECT
        year,
        earthquake_count,
        LAG(earthquake_count) OVER (ORDER BY year) AS previous_year_count
    FROM yearly_counts
)
SELECT
    year,
    earthquake_count,
    previous_year_count,
    ROUND(
        ((earthquake_count - previous_year_count)
        / previous_year_count) * 100,
        2
    ) AS growth_rate_percent
FROM growth
ORDER BY year;

-- Q24. Top 3 most seismically active countries
-- based on earthquake frequency and average magnitude

SELECT
    country,
    COUNT(*) AS earthquake_count,
    ROUND(AVG(mag), 2) AS average_magnitude,
    ROUND(
        COUNT(*) * AVG(mag),
        2
    ) AS seismic_activity_score
FROM earthquakes
WHERE country IS NOT NULL
  AND country <> ''
GROUP BY country
ORDER BY seismic_activity_score DESC
LIMIT 3;


-- Q25. Average earthquake depth for each country
-- within 5 degrees north or south of the equator

SELECT
    country,
    ROUND(AVG(depth_km), 2) AS average_depth_km,
    COUNT(*) AS earthquake_count
FROM earthquakes
WHERE latitude BETWEEN -5 AND 5
  AND country IS NOT NULL
  AND country <> ''
GROUP BY country
ORDER BY average_depth_km DESC;


-- Q26. Countries with the highest ratio of shallow
-- to deep earthquakes

SELECT
    country,
    SUM(CASE WHEN depth_km < 50 THEN 1 ELSE 0 END) AS shallow_count,
    SUM(CASE WHEN depth_km > 300 THEN 1 ELSE 0 END) AS deep_count,
    ROUND(
        SUM(CASE WHEN depth_km < 50 THEN 1 ELSE 0 END)
        /
        NULLIF(
            SUM(CASE WHEN depth_km > 300 THEN 1 ELSE 0 END),
            0
        ),
        2
    ) AS shallow_deep_ratio
FROM earthquakes
WHERE country IS NOT NULL
  AND country <> ''
GROUP BY country
HAVING deep_count > 0
ORDER BY shallow_deep_ratio DESC;


-- Q27. Average magnitude difference between tsunami
-- and non-tsunami earthquakes

SELECT
    AVG(CASE WHEN tsunami = 1 THEN mag END) AS tsunami_avg_magnitude,
    AVG(CASE WHEN tsunami = 0 THEN mag END) AS non_tsunami_avg_magnitude,
    ROUND(
        AVG(CASE WHEN tsunami = 1 THEN mag END)
        -
        AVG(CASE WHEN tsunami = 0 THEN mag END),
        2
    ) AS magnitude_difference
FROM earthquakes;

-- Q28. Events with lowest data reliability
-- using GAP and RMS

SELECT
    id,
    time,
    place,
    mag,
    gap,
    rms,
    ROUND(
        (COALESCE(gap, 0) + COALESCE(rms, 0)) / 2,
        2
    ) AS reliability_error_score
FROM earthquakes
WHERE gap IS NOT NULL
  AND rms IS NOT NULL
ORDER BY reliability_error_score DESC
LIMIT 10;

-- Q30. Regions with the highest frequency of deep-focus earthquakes
-- Depth greater than 300 km

SELECT
    country,
    COUNT(*) AS deep_earthquake_count
FROM earthquakes
WHERE depth_km > 300
  AND country IS NOT NULL
  AND country <> ''
GROUP BY country
ORDER BY deep_earthquake_count DESC
LIMIT 10;

