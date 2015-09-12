from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, RadioField
from wtforms.validators import DataRequired

class Search(Form):
    departingAirport = StringField('departingAirport', validators=[DataRequired()])
    arrivingAirport = StringField('arrivingAirport', validators=[DataRequired()])
    # departingWeekday = StringField('departingWeekday', validators=[DataRequired()])
    # returningWeekday = StringField('returningWeekday', validators=[DataRequired()])
    maxStopsDeparting = StringField('maxStopsDeparting', validators=[DataRequired()])
    maxStopsReturning = StringField('maxStopsReturning', validators=[DataRequired()])