from flask import Flask, request
from flask_wtf.form import FlaskForm
from wtforms import Field, fields
from wtforms import validators as v
from typing import Optional

def number_length(min: int, max: int, message: Optional[str] = None):
    def _wrapper(form: FlaskForm, field: Field):
        if len(str(field.data)) < min or len(str(field.data)) > max:
            raise v.ValidationError(message)
    return _wrapper

number_version1 = fields.IntegerField(validators=[v.InputRequired('fdgdfgd'), number_length(1, 5)])


class NumberLength:

    def __init__(self, min: int = -1, max: int = -1, message: Optional[str] = None):
        assert (
            min != -1 or max != -1
        ), "At least one of `min` or `max` must be specified."
        assert max == -1 or min <= max, "`min` cannot be more than `max`."
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        if len(str(field.data)) < self.min or len(str(field.data)) > self.max:
            raise v.ValidationError(self.message)


number_version2 = fields.IntegerField(validators=[v.InputRequired(), NumberLength(1, 5)])
