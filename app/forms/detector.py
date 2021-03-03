from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired


class DetectorForm(FlaskForm):
    serial = StringField('serial', validators=[DataRequired()])
    name = PasswordField('name', validators=[DataRequired()])
    x = IntegerField('x', validators=[DataRequired()])
    y = IntegerField('y', validators=[DataRequired()])


