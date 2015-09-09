from flask import render_template, flash, redirect
from app import app
from .forms import Search
from .rebound import ReBound

@app.route('/results')

def results():
    return render_template("results.html",
                           title='Results',)

@app.route('/')
@app.route('/search')#, methods=['GET', 'POST'])
def search():
    form = Search()
    rebound = ReBound()
    if form.validate_on_submit():
        # flash('Departing Airport ="%s"' % (form.departingAirport.data))
        flights = rebound.reboundSearch(form.departingAirport.data, form.arrivingAirport.data, form.departingWeekday.data, form.returningWeekday.data)
        flash(flights)
        return redirect('/results')
    return render_template('search.html', 
                           title='Search',
                           form=form)