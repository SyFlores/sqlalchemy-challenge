# Dependencies

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

import pandas as pd
import numpy as np
import datetime as dt

# Database and Table Reflections

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
base = automap_base()
base.prepare(engine, reflect = True)

measurement = base.classes.measurement
station = base.classes.station

session = Session(engine)

# Flask

app = Flask(__name__)

# Define the Flask Routes

@app.route("/")
def landing(): 
    return (
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/<start> <br/>"
        f"/api/v1.0/<start>/<end> <br/>"
)


# @app.route("/api/v1.0/precipitation")
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data for the last year"""

    year_back_date = dt.date(2017, 8, 23) - dt.timedelta(days = 365)

    precipitation_data = session.query(measurement.date, measurement.prcp)\
    .filter(measurement.date >= year_back_date).all()

    # Dict with date as the key and prcp as the value
    precipitation = []
    for date_value, prcp_value in precipitation_data:
        date_dictionary = {}
        date_dictionary[date_value] = prcp_value
        precipitation.append(date_dictionary)

    return jsonify(precipitation)


@app.route("/api/v1.0/stations")
def stations():
    all_results = session.query(station.name).all()
    station_names = list(np.ravel(all_results))

    return jsonify(station_names)


@app.route("/api/v1.0/tobs")
def tobs():
    year_back_date = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
    active_data = session.query(measurement.tobs)\
        .filter(measurement.station == "USC00519281")\
        .filter(measurement.date >= year_back_date).all()

    tobs_active = list(np.ravel(active_data))

    return jsonify(tobs_active)


@app.route("/api/v1.0/<start>")
def start_stats(start):
    after_data = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs))\
        .filter(measurement.date >= start).all()
    
    summary_table = []
    for tobs_min, tobs_max, tobs_avg in after_data:
        placeholder = {}

        placeholder["Min Temp"] = tobs_min
        placeholder["Max Temp"] = tobs_max
        placeholder["Avg Temp"] = tobs_avg

        summary_table.append(placeholder) # Adds {} into []
    
    return jsonify(summary_table)


@app.route("/api/v1.0/<start>/<end>")
def between_stats(start, end):
    after_data = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs))\
        .filter(measurement.date >= start)\
        .filter(measurement.date <= end).all() # This hsould be the only major difference between this and the last
    
    summary_table = []
    for tobs_min, tobs_max, tobs_avg in after_data:
        placeholder = {}

        placeholder["Min Temp"] = tobs_min
        placeholder["Max Temp"] = tobs_max
        placeholder["Avg Temp"] = tobs_avg

        summary_table.append(placeholder) # Adds {} into []
    
    return jsonify(summary_table)


if __name__ == "__main__":
    app.run(debug = True)
