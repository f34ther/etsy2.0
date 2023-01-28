from flask import Blueprint, render_template
# from helpers import token_required
# instead of contacts need cars/used cars
# from models import db, User, Contact, contact_schema, contacts_schema

site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    return render_template('index.html')


@site.route('/profile')
def profile():
    return render_template('profile.html')
