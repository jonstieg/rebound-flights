from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, RadioField
from wtforms.validators import DataRequired

class Search(Form):
    departingAirport = StringField('departingAirport', validators=[DataRequired()])
    arrivingAirport = StringField('arrivingAirport', validators=[DataRequired()])
    departingTimeEarly = StringField('departingTimeEarly', validators=[DataRequired()])
    departingTimeLate = StringField('departingTimeEarly', validators=[DataRequired()])
    returningTimeEarly = StringField('departingTimeEarly', validators=[DataRequired()])
    returningTimeLate = StringField('departingTimeEarly', validators=[DataRequired()])