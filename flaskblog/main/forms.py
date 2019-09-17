from flask_wtf import FlaskForm 
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_sqlalchemy import SQLAlchemy 
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class UserForm(FlaskForm):
    def User_query(): return User.query
    opts = QuerySelectField(query_factory=User_query, allow_blank=True, get_label='username')
