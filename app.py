from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


# Home Page Route
@app.route('/')
def home():
    return render_template('home.html')


# Favourite Page Route
@app.route('/favourites')
def favourites():
    return "<h1> Favourites Page Coming Soon! </h1>"


# Search Page Route
@app.route('/search')
def search():
    return "<h1> Search Page Coming Soon! </h1>"


@app.route('/Rolex')
def Rolex():
    return render_template('brands/rolex.html')


if __name__ == '__main__':
    app.run(debug = True)