from flask import Flask, request
from db import GroceryDB
from tinydb import TinyDB

app = Flask(__name__)
db = GroceryDB()


@app.route('/', methods=['GET'])
def home():
    return """
    <h1>Grocery list by</h1>
    <ul>
        <li><a href="http://127.0.0.1:5000/grocery">All products</a></li>
        <li><a href="http://127.0.0.1:5000/grocery/name/Sugar">Grocery by name<a/>
        <li><a href="http://127.0.0.1:5000/grocery/price/2.5">Grocery by price<a/>
        <li><a href="http://127.0.0.1:5000/add">Add product with POST method</a>

        <ul><h4>Types</h4>
            <li><a href="http://127.0.0.1:5000/grocery/type/fruit">Fruits</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/dairy">Dairy Products</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/vegetable">Vegetables</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/bakery">Bakery</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/grain">Grain</a></li>
        </ul>

    </ul>"""



# view all grocery
@app.route('/grocery')
def all_grocery():
    """Get all grocery"""
    product = db.all()
    table = """
    <h1>Grocery list by</h1>
    <ul>
        <li><a href="http://127.0.0.1:5000/grocery">All products</a></li>
        <li><a href="http://127.0.0.1:5000/grocery/name/Sugar">Grocery by name<a/>
        <li><a href="http://127.0.0.1:5000/grocery/price/2.5">Grocery by price<a/>
        <li><a href="http://127.0.0.1:5000/add">Add product with POST method</a>

        <ul><h4>Types</h4>
            <li><a href="http://127.0.0.1:5000/grocery/type/fruit">Fruits</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/dairy">Dairy Products</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/vegetable">Vegetables</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/bakery">Bakery</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/grain">Grain</a></li>
        </ul>

    </ul>
    <table border="1">
    <tr>
        <th>name</th>
        <th>quatity</th>
        <th>price</th>
        <th>type</th>
    </tr>"""
    for item in product:
        table += f"""
        <tr>
            <td>{item['name']}</td>
            <td>{item['quantity']}</td>
            <td>${item['price']}</td>
            <td>{item['type']}</td>
        </tr>"""
    table += "</table>"
    return table


# view add grocery
@app.route('/grocery/add/', methods=['POST'])
def add_grocery():
    """Add a grocery"""
    data = request.get_json()
    db.add(data)
    
    return data


# view all grocery by type
@app.route('/grocery/type/<tur>')
def all_grocery_by_type(tur):
    """Get all grocery by type"""
    product = db.get_by_type(tur)
    table = """
    <h1>Grocery list by</h1>
    <ul>
        <li><a href="http://127.0.0.1:5000/grocery">All products</a></li>
        <li><a href="http://127.0.0.1:5000/grocery/name/Sugar">Grocery by name<a/>
        <li><a href="http://127.0.0.1:5000/grocery/price/2.5">Grocery by price<a/>
        <li><a href="http://127.0.0.1:5000/add">Add product with POST method</a>

        <ul><h4>Types</h4>
            <li><a href="http://127.0.0.1:5000/grocery/type/fruit">Fruits</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/dairy">Dairy Products</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/vegetable">Vegetables</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/bakery">Bakery</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/grain">Grain</a></li>
        </ul>

    </ul>
    <table border="1">
    <tr>
        <th>name</th>
        <th>quatity</th>
        <th>price</th>
        <th>type</th>
    </tr>"""
    for item in product:
        table += f"""
        <tr>
            <td>{item['name']}</td>
            <td>{item['quantity']}</td>
            <td>${item['price']}</td>
            <td>{item['type']}</td>
        </tr>"""
    table += "</table>"
    return table


# view all grocery by name
@app.route('/grocery/name/<name>')
def all_grocery_by_name(name):
    """Get all grocery by name"""
    product = db.get_by_name(name)
    table = """
    <h1>Grocery list by</h1>
    <ul>
        <li><a href="http://127.0.0.1:5000/grocery">All products</a></li>
        <li><a href="http://127.0.0.1:5000/grocery/name/Sugar">Grocery by name<a/>
        <li><a href="http://127.0.0.1:5000/grocery/price/2.5">Grocery by price<a/>
        <li><a href="http://127.0.0.1:5000/add">Add product with POST method</a>

        <ul><h4>Types</h4>
            <li><a href="http://127.0.0.1:5000/grocery/type/fruit">Fruits</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/dairy">Dairy Products</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/vegetable">Vegetables</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/bakery">Bakery</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/grain">Grain</a></li>
        </ul>

    </ul>
    <table border="1">
    <tr>
        <th>name</th>
        <th>quatity</th>
        <th>price</th>
        <th>type</th>
    </tr>"""
    for item in product:
        table += f"""
        <tr>
            <td>{item['name']}</td>
            <td>{item['quantity']}</td>
            <td>${item['price']}</td>
            <td>{item['type']}</td>
        </tr>"""
    table += "</table>"
    return table


# view all grocery by price
@app.route('/grocery/price/<float:price>')
def all_grocery_by_price(price):
    """Get all grocery by price"""
    product = db.get_by_price(price)
    table = """
    <h1>Grocery list by</h1>
    <ul>
        <li><a href="http://127.0.0.1:5000/grocery">All products</a></li>
        <li><a href="http://127.0.0.1:5000/grocery/name/Sugar">Grocery by name<a/>
        <li><a href="http://127.0.0.1:5000/grocery/price/2.5">Grocery by price<a/>
        <li><a href="http://127.0.0.1:5000/add">Add product with POST method</a>

        <ul><h4>Types</h4>
            <li><a href="http://127.0.0.1:5000/grocery/type/fruit">Fruits</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/dairy">Dairy Products</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/vegetable">Vegetables</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/bakery">Bakery</a></li>
            <li><a href="http://127.0.0.1:5000/grocery/type/grain">Grain</a></li>
        </ul>

    </ul>
    <table border="1">
    <tr>
        <th>name</th>
        <th>quatity</th>
        <th>price</th>
        <th>type</th>
    </tr>"""
    for item in product:
        table += f"""
        <tr>
            <td>{item['name']}</td>
            <td>{item['quantity']}</td>
            <td>${item['price']}</td>
            <td>{item['type']}</td>
        </tr>"""
    table += "</table>"
    return table



if __name__ == '__main__':
    app.run(debug=True, port=5000)