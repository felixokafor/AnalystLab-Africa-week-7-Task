# AnalystLab-Africa-week-7-Task

Weather ETL Pipeline Project

Project Overview

This project demonstrates the ETL (Extract, Transform, Load) process using real-time weather data collected from the OpenWeather API. The pipeline extracts weather information for multiple Nigerian cities, transforms the data into a clean and structured format using Pandas, and loads the processed data into a CSV file for analysis.

Objective

To build a simple ETL pipeline that retrieves live weather data, cleans and organizes the data, stores it for future use, and performs basic analysis.

Data Source:
OpenWeather API
https://openweathermap.org/api

Tools Used:

- Python
- Requests
- Pandas
- OpenWeather API
- VS Code

ETL Process
Extract

Weather data was collected from the OpenWeather API for the following cities:

- Lokoja
- Abuja
- Lagos
- Port Harcourt
- Ilorin
- Anambra

The following fields were extracted:

- City
- Temperature
- Humidity
- Weather Condition
- Wind Speed
- Timestamp

Transform

The extracted JSON data was transformed into a Pandas DataFrame.

Data transformation included:

- Structuring data into tabular format
- Renaming columns
- Checking data types
- Validating missing values
- Preparing data for analysis

Load

The cleaned dataset was saved as:

- process_weather_data.csv

Analysis Findings

Key insights from the collected weather data:

- Lagos recorded the highest temperature at 26.59°C.
- Ilorin recorded the highest humidity at 92%.
- The average temperature across all cities was 25.16°C.
- Cloudy weather conditions were observed across all six cities.

Skills Demonstrated

- API Integration
- Data Extraction
- Data Cleaning
- Data Transformation
- ETL Pipeline Development
- Data Analysis
- Data Storage Using CSV

Conclusion

This project demonstrates how ETL pipelines automate data collection, transformation, and storage, making raw data ready for analysis and decision making.
