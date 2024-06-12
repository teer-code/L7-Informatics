from flask import Flask, render_template, request, redirect, url_for
from models import SeasonalFlavor, Ingredient, CustomerSuggestion

app = Flask(__name__)

@app.route('/')
def index():
    flavors = SeasonalFlavor.get_all()
    return render_template('index.html', flavors=flavors)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    flavors = [flavor for flavor in SeasonalFlavor.get_all() if query.lower() in flavor[1].lower()]
    return render_template('search.html', flavors=flavors)

@app.route('/add_allergen', methods=['GET', 'POST'])
def add_allergen():
    if request.method == 'POST':
        name = request.form['name']
        suggestion = request.form['suggestion']
        allergens = request.form['allergens']
        CustomerSuggestion.add_suggestion(name, suggestion, allergens)
        return redirect(url_for('index'))
    return render_template('add_allergen.html')

@app.route('/cart', methods=['GET'])
def cart():
    # Logic for cart goes here
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)
