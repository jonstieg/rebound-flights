from flask import render_template, flash, redirect, request
from app import app
from .forms import Search
from .rebound import ReBound

@app.route('/', methods=['GET', 'POST'])
def search():
    form = Search()
    rebound = ReBound()
    if form.validate_on_submit():
        flights = rebound.reboundSearch(form.departingAirport.data, form.arrivingAirport.data, request.form['depDay'], request.form['retDay'], request.form['depStops'], request.form['retStops'])
        flash(flights)
    return render_template('search.html', 
                           title='Search',
                           form=form)