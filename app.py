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


### Rolex ###
@app.route('/Rolex')
def Rolex():
    return render_template('brands/rolex.html')

@app.route('/Rolex/1908')
def Rolex_1908():
    return render_template('brands/rolex_models/1908.html')

@app.route('/Rolex/AirKing')
def Rolex_airking():
    return render_template('brands/rolex_models/airking.html')

@app.route('/Rolex/Datejust')
def Rolex_datejust():
    return render_template('brands/rolex_models/datejust.html')

@app.route('/Rolex/daydate')
def Rolex_daydate():
    return render_template('brands/rolex_models/daydate.html')

@app.route('/Rolex/Daytona') 
def rolex_daytona():
    return render_template('brands/rolex_models/daytona.html')


@app.route('/Rolex/Explorer_I')
def Rolex_exploreri():
    return render_template('brands/rolex_models/exploreri.html')

@app.route('/Rolex/Explorer_II')
def Rolex_explorerii():
    return render_template('brands/rolex_models/explorerii.html')

@app.route('/Rolex/GMT_Master_II')
def Rolex_gmtmasterii():
    return render_template('brands/rolex_models/gmtmasterii.html')

@app.route('/Rolex/Milgauss')
def Rolex_milgauss():
    return render_template('brands/rolex_models/milgauss.html')

@app.route('/Rolex/Oyster_Perpetual')
def Rolex_oysterperpetual():
    return render_template('brands/rolex_models/oysterperpetual.html')

@app.route('/Rolex/Skydweller')
def Rolex_skydweller():
    return render_template('brands/rolex_models/skydweller.html')

@app.route('/Rolex/Submariner')
def Rolex_submariner():
    return render_template('brands/rolex_models/submariner.html')

@app.route('/Rolex/Yacht_Master')
def Rolex_yachtmaster():
    return render_template('brands/rolex_models/yachtmaster.html')

@app.route('/Rolex/All')
def Rolex_All():
    return render_template('brands/rolex_all.html')

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