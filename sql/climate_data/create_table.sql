CREATE TABLE "Climate" (
	date DATETIME, 
	day BIGINT, 
	temp_avg_c FLOAT, 
	temp_max_c FLOAT, 
	temp_min_c FLOAT, 
	atmospheric_pressure_at_sea_lvl_hpa FLOAT, 
	rel_humidity_avg_percent FLOAT, 
	total_rainfall_or_snow_melt FLOAT, 
	visibility_avg_km FLOAT, 
	wind_speed_avg_km_p_hr FLOAT, 
	sustained_wind_speed_max_km_p_hr FLOAT, 
	wind_speed_max_km_p_hr FLOAT, 
	did_it_rain BIGINT, 
	did_it_snow BIGINT, 
	did_it_storm BIGINT, 
	was_there_fog BIGINT
)