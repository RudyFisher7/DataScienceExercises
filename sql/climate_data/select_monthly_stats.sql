SELECT STRFTIME('%Y-%m', date) AS month, COUNT(*) AS sample_count, AVG(temp_avg_c), MAX(temp_max_c), MIN(temp_min_c) FROM Climate
GROUP BY month
;