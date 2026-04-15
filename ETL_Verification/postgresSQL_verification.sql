SELECT COUNT(*) FROM wdi_data;

SELECT *
FROM wdi_data
LIMIT 10;

-- Check duplicates 
SELECT country_code, indicator_code, year, COUNT(*)
FROM wdi_data
GROUP BY country_code, indicator_code, year
HAVING COUNT(*) > 1;