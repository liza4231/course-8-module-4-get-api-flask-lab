from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)


# TODO: Implement homepage route that returns a welcome message

@app.route("/", methods=["GET"])
def home():
    # TODO: Return a welcome message
    return jsonify({
        "message": "Welcome to the Product Catalog API!"
    }), 200


# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products", methods=["GET"])
def get_products():
    # TODO: Return all products or filter by ?category=
    category = request.args.get("category")

    # If category is provided filter products
    if category:
        filtered_products = [
            product for product in products
            if product["category"].lower() == category.lower()
        ]
        return jsonify(filtered_products), 200

    # If no category is provided return all products
    return jsonify(products), 200


# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    # TODO: Return product by ID or 404
    # Product found by ID
    product = next((product for product in products if product["id"] == id), None)

    # Product not found, return 404
    if product is None:
        return jsonify({
            "error": "Product not found"
        }), 404

    return jsonify(product), 200

if __name__ == "__main__":
    app.run(debug=True)
