from flask import render_template, request, Blueprint, Flask
from flaskblog.models import Post, User
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm 
from wtforms_sqlalchemy.fields import QuerySelectField
from flaskblog.main.forms import UserForm


main = Blueprint('main', __name__)


@main.route("/home", methods=['GET', 'POST'])
@main.route("/", methods=['GET', 'POST'])
def home():
    form = UserForm()
    return render_template('home.html', form=UserForm)
    def User_query(): return User.query




@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/plans")
def plans():
    return render_template('plans.html', title='Plans')