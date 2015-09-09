from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class Search(Form):
    departingAirport = StringField('departingAirport', validators=[DataRequired()])
    arrivingAirport = StringField('arrivingAirport', validators=[DataRequired()])
    departingWeekday = StringField('departingWeekday', validators=[DataRequired()])
    returningWeekday = StringField('returningWeekday', validators=[DataRequired()])