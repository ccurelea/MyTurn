from flask import render_template, request, Blueprint, Flask
from flaskblog.models import Post, User
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm 
from wtforms_sqlalchemy.fields import QuerySelectField
from flaskblog.users.forms import (SignupForm)
#from flaskblog.main.forms import UserForm


main = Blueprint('main', __name__)


@main.route("/home", methods=['GET', 'POST'])
@main.route("/", methods=['GET', 'POST'])
def home():
    # form = UserForm()
    
    new_names = []
    places = User.query.all()
    for place in places:
        new_names.append(place.username)
    
    print("new_names: ", new_names)
    return render_template('home.html', new_names=new_names)
    # def User_query(): return User.query




@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/plans", methods=['GET', 'POST'])
def plans():
    form = SignupForm()
    if form.validate_on_submit():
            return redirect(url_for('register.html'))
            print("Test")

    return render_template('plans.html', form=form)

