from flask import render_template, flash, redirect, request
from app import app
from .forms import Search
from .rebound import ReBound

@app.route('/', methods=['GET', 'POST'])
def search():
    form = Search()
    rebound = ReBound()
    if form.validate_on_submit():
        # flights = rebound.reboundSearch(form.departingAirport.data, form.arrivingAirport.data, request.form['depDay'], request.form['retDay'], request.form['depStops'], request.form['retStops'])
        # flash(flights)
        flash('hello')
    return render_template('search.html', 
                           title='Search',
                           form=form)

    # https://www.google.com/flights/#search;f=SAN;t=JFK;d=2015-09-28;r=2015-10-02;s=1