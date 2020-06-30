from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from ..models import Shelf, Language

class BooksForm(FlaskForm):
    """
    Class form to books
    """

    code = StringField('Code', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    publisher = StringField('Publisher', validators=[DataRequired()])
    shelf = QuerySelectField(query_factory=lambda: Shelf.query.all(), get_label="sh_desc")
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    language = QuerySelectField(query_factory=lambda: Language.query.all(), get_label="name")
    submit = SubmitField('Submit')