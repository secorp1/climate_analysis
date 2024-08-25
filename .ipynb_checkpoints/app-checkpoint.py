import datetime as database 
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import session
from sqlalchemy import create_engine, func

from Flask import Flask, jsonify


engine = create_engine("sqlite:////Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine)

Measurement = Base.classes.Measurement
Station = Base.classes.Station

session = Session(engine)

app = Flask(___name___)


@app.route("/")
def welcome():
    return(
        f"Welcome to Hawaii Climate Analysis API<br/>",
        f"Available Routes:<br/>",
        f"/api/v1.0/precipitation<br/>",
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br/>",
        f"<p>'start' and 'end' date should be in the format MMDDYYYY.</p>"
    )    
    @app.route("/api/v1.0/precipitation")
    def precipitation():
        prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)

        precipitation = session.query(Measurement.date, Measurement.prcp).\
            filter(Measurement.date >= prev_year).all()

        session.close()
        precip = { date: prcp for date, prcp in precipitation}

        return jsonify(precip)


    if ___name___ = "___main___":
        app.run(debug=True)
        



