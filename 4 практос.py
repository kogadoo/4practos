# Управление товарами
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def update(self, product):
        for idx, product in enumerate(self.products):
            if product.name == product.name:
                self.products[idx] = product

    def get_all(self):
        return self.products

# Управление заказами
class Order:
    def __init__(self, user, products):
        self.user = user
        self.products = products

class OrderRepository:
    def __init__(self):
        self.orders = []

    def add(self, order):
        self.orders.append(order)

    def get_all(self):
        return self.orders

# Управление пользователями
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserRepository:
    def __init__(self):
        self.users = []

    def add(self, user):
        self.users.append(user)

    def get_all(self):
        return self.users

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None
    
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f"User: {self.username}"

    def is_authenticated(self):
        return self.username == "admin" and self.password == "admin"

class Client(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def place_order(self, products):
        order = Order(self, products)
        OrderRepository().add(order)

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def add_product(self, name, price):
        product = Product(name, price)
        ProductRepository().add(product)

def validate_username(username):
    if not username:
        return "Username is required"
    return None

def validate_password(password):
    if not password:
        return "Password is required"
    return None

import sqlite3

def save_to_db(user):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user.username, user.password))
    conn.commit()
    conn.close()

def show_error(message):
    print(f"Error: {message}")


import sqlite3

conn = sqlite3.connect("users.db")
conn.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
conn.execute('''CREATE IF NOT EXISTS products
                (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
conn.execute('''CREATE IF NOT EXISTS orders
                (id INTEGER PRIMARY KEY, user_id INTEGER, product_ids TEXT)''')
conn.commit()
conn.close()


def get_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

