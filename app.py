from flask import Flask
from controllers.user_controller import user_bp
from controllers.product_controller import product_bp
from config.database_config import STORAGE

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(product_bp)


@app.route("/")
def home():
    return f"""
    <h1>Welcome to ShopEase</h1>
    <p><small>Storage: {STORAGE}</small></p>
    <p><a href='/users'>View Users</a></p>
    <p><a href='/products'>View Products</a></p>
    """


if __name__ == "__main__":
    app.run(debug=True)
