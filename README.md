# sqlalchemy-challenge
Surfs Up!
*Collaborators: Sy Flores*

---
## **Table of Contents**
- [Abstract](#abstract)
- [Repository](#repository)

---

## Abstract
We are assigned with performing climate analysis on Honolulu, Hawaii, primarily through the use of SQLAlchemy ORM queries, Pandas, and Matplotlib. To start, we will be using Python and SQLAlchemy to do some basic climate analysis and data exploration of our climate database. Visualizations of precipitation and station analysis will be performed using Matplotlib.  
Following this, we will create a Flask API based on the queries that we have just developed.

## Repository
This section serves as a means to navigate the project/repository.

- **Images**
    - daily-normals.png
        - This image file contains a visualization for min, max, and avg temperatures
        - No indication points to this visual being a part of of this project
    - describe.png
        - This image file contains an example of precipitation summary statistics
    - precipitation.png
        - This image file contains a visualization of precipitation in inches plotted against individual dates
    - station-histogram.png
        - This image file contains a visualization of a temperature histogram for the most active station readings
    - surfs-up.png
        - This image file contains an image of a person surfing
    - temperatures.png
        - This image file contains a unclear temperature visualization
        - No indication points to this visual being a part of of this project
- **Resources**
    - hawaii_measurements.csv
        - This csv file contains readings from the 9 stations on precipitation and temperature
        - The fields include: station(id), date, prcp(precipitation), tobs(temperature observation data)
    - hawaii_stations.csv
        - This csv file contains information on 9 stations we will be analyzing
        - The fields include: station(id), name, latitude, longitude, and elevation
    - hawaii.sqlite
        - This sqlite file contains the data found in both the hawaii_measurements.csv and hawaii_stations.csv files
- app.py
    - This is the script that will be used to hold the Flask API based on the queries developed
- climate_starter.ipynb
    - This notebook contains analysis and exploration of climate data
- README.md
    - The primary use of this file is to explain how to navigate the project and repository

---