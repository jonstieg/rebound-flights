from flask import render_template, flash, redirect, request
from app import app
from .forms import Search
from .rebound import ReBound

@app.route('/results')

def results():
    return render_template("results.html",
                           title='Results',)

@app.route('/', methods=['GET', 'POST'])
@app.route('/search', methods=['GET', 'POST'])
def search():
    form = Search()
    rebound = ReBound()
    if form.validate_on_submit():
        flights = rebound.reboundSearch(form.departingAirport.data, form.arrivingAirport.data, request.form['depDay'], request.form['retDay'], form.maxStopsDeparting.data, form.maxStopsReturning.data)
        flash(flights)
        return redirect('/results')
    return render_template('search.html', 
                           title='Search',
                           form=form)