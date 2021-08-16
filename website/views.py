# stores the URL end points for the front-end websites
# store standard routes - where the user can go to

from flask import Blueprint, render_template

# defining Blueprint
views = Blueprint('views', __name__)

# home page
@views.route("/")
@views.route("/home")
def home():
  return render_template('index.html')

# about page
@views.route("/about")
def about():
  return render_template('about.html', title = 'About')