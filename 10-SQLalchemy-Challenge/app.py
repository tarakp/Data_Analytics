# Import Modules
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# from flask import Flask, jsonify
from flask import Flask, jsonify


engine=create_engine('sqlite:///C:/Users/tarak/Desktop/DataAnalytics/~Homework/Data_Analytics/10-SQLalchemy-Challenge/Resources/hawaii.sqlite')

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
sessions = Session(engine)


app = Flask(__name__)

# Use Flask to create your routes.
# Home page.
# List all routes that are available.
@app.route("/")
def welcome():
    return (
        f"Welcome to API<br>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/start<br>"
        f"/api/v1.0/start/end<br>"
          )

@app.route("/api/v1.0/precipitation")
def precipitation():
    sessions = Session(engine)
    first_date = sessions.query(Measurement.date).\
    order_by(Measurement.date.desc()).first()

    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

# # Perform a query to retrieve the data and precipitation scores
    results = sessions.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= query_date).order_by(Measurement.date.desc()).all()
    
    sessions.close()

    all_precp = []

# Convert the query results to a dictionary using date as the key and prcp as the value.
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict['date'] = date
        prcp_dict['prcp'] = prcp
        all_precp.append(prcp_dict)

# Return the JSON representation of your dictionary.    
    return jsonify(all_precp)



@app.route("/api/v1.0/stations")
def station():
    results1 = sessions.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()

    sessions.close()

    all_stations = []

    for station, name, latitude, longitude,elevation in results1:
        station_a = {}
        station_a['station'] = station
        station_a['name'] = name
        station_a['latitude'] = latitude
        station_a['longitude'] = longitude
        station_a['elevation'] = elevation

        all_stations.append(station_a)
# Return a JSON list of stations from the dataset.
    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def prcp():
    sessions = Session(engine)
    
    active = [Station.station, Station.name, func.count(Measurement.station).label('most_active')]

    prcp_count = sessions.query(*active).\
    filter(Station.station == Measurement.station).\
    group_by(Station.station).\
    order_by(func.count(Measurement.station).desc()).all()

    first_date = sessions.query(Measurement.date).\
    order_by(Measurement.date.desc()).first()

    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

# # Perform a query to retrieve the data and precipitation scores
    results2 = sessions.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date >= query_date).\
    filter(Measurement.station == prcp_count[0][0]).\
    order_by(Measurement.date.desc()).all()
    
    sessions.close()

    all_tobs = []

# Query the dates and temperature observations of the most active station for the last year of data.
    for date, tobs in results2:
        tobs_dict = {}
        tobs_dict['date'] = date
        tobs_dict['tobs'] = tobs

        all_tobs.append(tobs_dict)

# Return a JSON list of temperature observations (TOBS) for the previous year.
    return jsonify(all_tobs)


# # /api/v1.0/<start> and /api/v1.0/<start>/<end>
@app.route("/api/v1.0/<start>")
def start(start):
    sessions = Session(engine)

    # sel = [func.min(Measurement.tobs).label('min_temp'), func.avg(Measurement.tobs).label('max_temp'), func.max(Measurement.tobs).label('avg_temp')]
    results3 = sessions.query(func.min(Measurement.tobs).label('min_temp'), func.max(Measurement.tobs).label('max_temp'), func.avg(Measurement.tobs).label('avg_temp')).\
    filter(Measurement.date >= start).all()
    

    start_dt = []
    for min_temp, max_temp, avg_temp in results3:
        dt_start = {}
        dt_start['min_temp'] = min_temp
        dt_start['max_temp'] = max_temp
        dt_start['avg_temp'] = avg_temp

        start_dt.append(dt_start)       
    
    return jsonify(start_dt)


@app.route("/api/v1.0/<start>/<end>")
def SE(start, end):
    sessions = Session(engine)

    # sel = [func.min(Measurement.tobs).label('min_temp'), func.avg(Measurement.tobs).label('max_temp'), func.max(Measurement.tobs).label('avg_temp')]
    results4 = sessions.query(func.min(Measurement.tobs).label('min_temp'), func.max(Measurement.tobs).label('max_temp'), func.avg(Measurement.tobs).label('avg_temp')).\
    filter(Measurement.date >= start).\
    filter(Measurement.date <= end).all()
    

    SE_dt = []
    for min_temp, max_temp, avg_temp in results4:
        dt_SE = {}
        dt_SE['min_temp'] = min_temp
        dt_SE['max_temp'] = max_temp
        dt_SE['avg_temp'] = avg_temp

        SE_dt.append(dt_SE)       
    
    return jsonify(SE_dt)



if __name__ == '__main__':
    app.run()


# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.


# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.


# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.




if __name__ == '__main__':
    app.run(debug=True)