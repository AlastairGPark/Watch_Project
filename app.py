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


# Favourite Page Route
@app.route('/favourites')
def favourites():
    return "<h1> Favourites Page Coming Soon! </h1>"


# Search Page Route
@app.route('/search')
def search():
    return "<h1> Search Page Coming Soon! </h1>"


@app.route('/<brand>/<model>')
def show_model(brand, model):  # The function name must match what is used in `url_for()`
    print(f"Brand: {brand}, Model: {model}")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # Ensure case-insensitive matching
    cursor.execute("SELECT * FROM watches WHERE brand = ? AND model = ?", (brand, model))
    
    watches = cursor.fetchall()
    conn.close()

    if not watches:
        return "<h1>No watches found for this brand/model.</h1>", 404
    
    return render_template('model_page.html', brand = brand, model = model, watches = watches)



### Rolex ###
@app.route('/Rolex')
def Rolex():
    return render_template('brands/rolex.html')

### End of Rolex ###



### Audemars Piguet ###

@app.route('/AudemarsPiguet')
def AudemarsPiguet():
    return render_template('brands/ap.html')

### End of Audemars Piguet ###



### Vacheron Constantin ###

@app.route('/VacheronConstantin')
def VacheronConstantin():
    return render_template('brands/vc.html')

### End of Vacheron Constantin ###



### Tudor ###

@app.route('/Tudor')
def Tudor():
    return render_template('brands/tudor.html')

### End of Tudor ###



### Ulysse Nardin ###

@app.route('/UlysseNardin')
def UlysseNardin():
    return render_template('brands/un.html')

### End of Ulysse Nardin ###




@app.route('/brand/<brand_name>')
def brand_page(brand_name):
    return render_template('brand.html', brand_name=brand_name)


if __name__ == '__main__':
    app.run(debug = True)