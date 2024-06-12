import sqlite3

def connect_db():
    return sqlite3.connect('parlor.db')

class SeasonalFlavor:
    @staticmethod
    def get_all():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM seasonal_flavors')
        flavors = cursor.fetchall()
        conn.close()
        return flavors

    @staticmethod
    def add_flavor(name, description):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO seasonal_flavors (name, description) VALUES (?, ?)', (name, description))
        conn.commit()
        conn.close()

class Ingredient:
    @staticmethod
    def get_all():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM ingredients')
        ingredients = cursor.fetchall()
        conn.close()
        return ingredients

    @staticmethod
    def add_ingredient(name, quantity):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO ingredients (name, quantity) VALUES (?, ?)', (name, quantity))
        conn.commit()
        conn.close()

class CustomerSuggestion:
    @staticmethod
    def add_suggestion(name, suggestion, allergens):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO customer_suggestions (name, suggestion, allergens) VALUES (?, ?, ?)', (name, suggestion, allergens))
        conn.commit()
        conn.close()
