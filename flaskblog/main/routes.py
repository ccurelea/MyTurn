from flask import render_template, request, Blueprint, Flask
from flaskblog.models import Post, User
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm 
from wtforms_sqlalchemy.fields import QuerySelectField


main = Blueprint('main', __name__)


@main.route("/home", methods=['GET', 'POST'])
@main.route("/", methods=['GET', 'POST'])
def home():
    form = UserForm()
    return render_template('home.html', form=UserForm)

def User_query(): return User.query

class UserForm(FlaskForm): opts = QuerySelectField(query_factory=User_query, allow_blank=False,)



@main.route("/about")
def about():
    return render_template('about.html', title='About')