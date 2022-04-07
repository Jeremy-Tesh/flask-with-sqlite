
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from market import routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

db = SQLAlchemy(app)
