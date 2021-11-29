# sqlalchemy-challenge

## Step 1 - Climate Analysis and Exploration

Python and SQLAlchemy are used to do basic climate analysis and data exploration for the given Hawaii climate database. The following analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

- Using the provided starter notebook and hawaii.sqlite files, climate analysis and data exploration is completed.
- SQLAlchemy create_engine is used to connect to the sqlite database.
- SQLAlchemy automap_base() is used to reflect the tables into classes and saved a reference to those classes:
  Station and Measurement.
- Python is linked to the database by creating an SQLAlchemy session.

Precipitation Analysis is done by: 
- finding the most recent date in the data set.
- Using the most recent date, retrieved the last 12 months of precipitation data by querying 12 preceding months and selecting the date and prcp values. 
- Loading the query results into a Pandas DataFrame by seting and sorting the index to the date column.
- Ploting the results using the DataFrame plot method. (fig: precipitation_by_dates.png)
- Using Pandas to print the summary statistics for the precipitation data.

Station Analysis is done by: 
- Designing a query to calculate the total number of stations in the dataset.
- Designing a query to find the most active stations (i.e. which stations have the most rows?).
- Listing the stations and observation counts in descending order.
- Finding the station id that has the highest number of observations.
- Using the most active station id, the lowest, highest, and average temperature are calculated using functions such as func.min, func.max, func.avg, and func.count in the queries.
- Designing a query to retrieve the last 12 months of temperature observation data (TOBS).
- Filtering by the station with the highest number of observations.
- Querying the last 12 months of temperature observation data for this station and Ploting the results as a histogram with bins=12. (fig: histogram of temperature.png)


## Step 2 - Climate App

After completion of initial analysis, a Flask API based on the queries developed above is designed using Flask to create routes. All available routes are listed in the home page. The query results are converted into a dictionary using date as key and precipation as value for the precipation data and returned the JSON represenation of the dictionary. Similarly, JSON list are returned for stations, temperature observations (tobs) for previous year.   

A JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range is returned in a similar way. 

For given the start date only as well as both the start and end dates, TMIN, TAVG, and TMAX for all dates greater than and equal to the start date, and in between the dates are calculated. 



## BONUS PART OF THE ANALYSIS:

## Temperature Analysis I:

Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in June and December?

Using pandas the following analysis is performed by:
- Converting the date column format from string to datetime.
- Setting the date column as the DataFrame index
- Identifying the average temperatures in June and December at all stations across all available years in the dataset. 
- using paired t-test to determine if there a significant difference in the average temperature for both the months. Found there is no significant difference as the p-value smaller than 0.05 level of significance. 

## Temperature Analysis II:

While looking to make a trip from August first to August seventh of this year, but worried that the weather will be less than ideal. Using historical data to find out what the temperature has previously looked like.

A function called calc_temps that accepts a start date and end date in the format %Y-%m-%d that returns the minimum, average, and maximum temperatures for that range of dates is used to calculate the min, avg, and max temperatures for the trip duration using the matching dates from a previous year (i.e., use “2017-08-01”).
A plot is obtained for the min, avg, and max temperature from the previous query as a bar chart that shows  
“Trip Avg Temp” as the title, the average temperature as the bar height (y value) and the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR). (fig: Average_temperature.png)

#### Daily Rainfall Average:

After gettign the idea of the temperature it comes to check what the rainfall has been!

The rainfall per weather station using the previous year’s matching dates is calculated and sorted in descending order by precipitation amount and the list of the stations, name, latitude, longitude, and elevation.

The daily normals are calculated using a given function called 'daily_normals' that calculates the daily normals for a specific date. The start and end date of the trip are set as date range by stripping off the year and saved a list of strings in the format %m-%d.

The list of daily normals is then loaded into a Pandas DataFrame and setting date as index and Panda plot is created as an area plot (stacked=False) for the daily normals. (fig: Predicted_temperature(min_avg_max).png)






