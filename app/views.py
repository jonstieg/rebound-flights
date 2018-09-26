from flask import render_template, flash, redirect, request
from app import app
from .forms import Search
from .rebound import ReBound
from datetime import datetime, date, timedelta

@app.route('/', methods=['GET', 'POST'])
def search():
    try:
        form = Search()
        rebound = ReBound()
        if form.validate_on_submit():
#             dateGo = datetime.today()
#             weeksToSearch = 18
#             flash ('Results:')
#             for x in range(1,weeksToSearch+1):
#                 depAir = request.form['departingAirport'][:3]
#                 retAir = request.form['arrivingAirport'][:3]
#                 print depAir
#                 print retAir
            flights = rebound.reboundSearch(dateGo, depAir, retAir, request.form['depDay'], request.form['retDay'], request.form['depStops'], request.form['retStops'], request.form['departingTimeEarly'], request.form['depTimeEarlyAMPM'], request.form['departingTimeLate'], request.form['depTimeLateAMPM'], request.form['returningTimeEarly'], request.form['retTimeEarlyAMPM'], request.form['returningTimeLate'], request.form['retTimeLateAMPM'])
            for x in flights:
#                     year = x[0][:4]
#                     month = x[0][5:7]
#                     day = x[0][8:10]
#                     months = {"01":"January", "02": "February", "03": "March", "04": "April", "05":"May", "06":"June", "07":"July", "08":"August", "09": "September", "10":"October", "11":"November", "12":"December"}
#                     flash("%s/%s/%s: %s" % (month, day, year, x[1]))
                    # 2015-09-24T21:00-07:00
                flash(x)
#                 dateGo = dateGo + timedelta(7)
    except:
        flash("We crashed. Try search again")
    return render_template('search.html', 
                           title='Search',
                           form=form)

    # https://www.google.com/flights/#search;f=SAN;t=JFK;d=2015-09-28;r=2015-10-02;s=1
