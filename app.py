
import sqlalchemy
from flask import Flask, jsonify
import datetime as dt
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect


# Database Setup
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# View all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


# Flask Setup
app = Flask(__name__)

# Routes
@app.route("/")
def main():
    return (
        f"Welcome to the Climate App Home Page!<br>"
        f"Available Routes Below:<br>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/<start><br>"
        f"/api/v1.0/<start>/<end><br>"
    )
        
    
@app.route("/api/v1.0/precipitation")
def precip():

    # Design a query to retrieve the last 12 months of precipitation data and plot the results
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    # Get the first element of the tuple
    most_recent_date = most_recent_date[0]
    # most_recent_date

    prev_year = dt.date(2017,8,23)- dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    result_dict = dict(results)

    # return json list of dictionary
    return jsonify(result_dict)


@app.route("/api/v1.0/stations")
def stations():
    # Design a query to find the most active stations (i.e. what stations have the most rows?)
    # List the stations and the counts in descending order.

    stations = session.query(Measurement.station, func.count(Measurement.id)).\
            group_by(Measurement.station).order_by(func.count(Measurement.id).desc()).all()

    # convert results to a dict
    stations_dict = dict(stations)

    # return json list of dict
    return jsonify(stations_dict)


@app.route("/api/v1.0/tobs")
def tobs():

    max_temp_obs = session.query(Measurement.station, Measurement.tobs).\
        filter(Measurement.date >= '2016-08-23').all()

    # convert results to dict
    tobs_dict = dict(max_temp_obs)

    # return json list of dict
    return jsonify(tobs_dict)


  

if __name__ == '__main__':
    app.run(debug=True)
