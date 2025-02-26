from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Home Page Route
@app.route('/')
def home():
    return render_template('home.html')


# Favourites Page Route
@app.route('/favourites')
def favourites():
    return "<h1> Favourites Page Coming Soon! </h1>"


# Search Page Route
@app.route('/search')
def search():
    return "<h1> Search Page Coming Soon! </h1>"


### Dynamic Brand and Model Routing ###

def get_all_brands():
    """Fetch all unique brands from the database."""
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT brand FROM watches ORDER BY brand")
    brands = [row[0] for row in cursor.fetchall()]
    conn.close()
    return brands

def get_models_by_brand(brand):
    """Fetch all unique models for a given brand."""
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT model FROM watches WHERE brand = ? ORDER BY model", (brand,))
    models = [row[0] for row in cursor.fetchall()]
    conn.close()
    return models

def get_watches_by_brand_and_model(brand, model):
    """Fetch all watches that match a given brand and model."""
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM watches WHERE brand = ? AND model = ?", (brand, model))
    watches = cursor.fetchall()
    conn.close()
    return watches


@app.route('/brands')
def brand_list():
    """Show all brands dynamically."""
    brands = get_all_brands()
    return render_template("brands.html", brands = brands)


@app.route('/<brand>')
def model_list(brand):
    """Show all models for a selected brand dynamically."""
    models = get_models_by_brand(brand)
    return render_template("models.html", brand = brand, models = models)


@app.route('/<brand>/<model>')
def watch_list(brand, model):
    """Display all watches matching a given brand and model."""
    watches = get_watches_by_brand_and_model(brand, model)

    if not watches:
        return "<h1>No watches found for this brand/model.</h1>", 404

    return render_template("model_page.html", brand=brand, model = model, watches = watches)


if __name__ == '__main__':
    app.run(debug=True)