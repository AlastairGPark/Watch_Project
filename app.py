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

@app.route('/AudemarsPiguet')
def AudemarsPiguet():
    return render_template('brands/ap.html')

@app.route('/VacheronConstantin')
def VacheronConstantin():
    return render_template('brands/vc.html')

@app.route('/Tudor')
def Tudor():
    return render_template('brands/tudor.html')

@app.route('/UlysseNardin')
def UlysseNardin():
    return render_template('brands/un.html')

@app.route('/brand/<brand_name>')
def brand_page(brand_name):
    return render_template('brand.html', brand_name=brand_name)


if __name__ == '__main__':
    app.run(debug = True)