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
base.prepare(engine, reflect=True)

measurement = base.classes.measurement
station = base.classes.station

session = Session(engine)

# Flask

app = Flask(__name__)

# Define the Flask Routes

@app.route("/")


# @app.route("/api/v1.0/precipitation")


# @app.route("/api/v1.0/stations")


# @app.route("/api/v1.0/tobs")


# @app.route("/api/v1.0/<start>")


# @app.route("/api/v1.0/<start>/<end>")