from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, HiddenField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets.html5 import NumberInput

from ..models.company import Company


class DeviceForm(FlaskForm):
    iid = HiddenField('', validators=[DataRequired()])
    direction = StringField('Direction', validators=[DataRequired()])
    order = IntegerField('Order of traffic', widget=NumberInput(), validators=[DataRequired(), NumberRange(min=0, max=99)])
    company = SelectField('company', validators=[DataRequired()], coerce=int)
    name = StringField('')

    def __init__(self, formdata=None, obj=None, prefix='', **kwargs):
        super(DeviceForm, self).__init__(formdata, **kwargs)
        _foo = [(_company.id_company, _company.name) for _company in kwargs['_companies']]
        _foo.append((-1, 'Other'))
        self.company.choices = _foo
