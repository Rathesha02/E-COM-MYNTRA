from flask import Blueprint, request, jsonify
import mysql.connector
from flask_cors import CORS

# Blueprint and CORS setup
carttable = Blueprint('carttable', __name__)
CORS(carttable)

# ✅ Database connection
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        port=3307,
        database='myntra'
    )

# 🔹 POST: Add or update item in cart
@carttable.route("/cart", methods=["POST"])
def add_to_cart():
    data = request.get_json()
    required_fields = [
        "user_id", "product_id", "product_name", 
        "product_image", "product_price", "stock", "quantity"
    ]
    missing = [f for f in required_fields if f not in data]
    
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if item already in cart
    cursor.execute("""
        SELECT quantity FROM carttable1 
        WHERE product_id = %s AND user_id = %s
    """, (data["product_id"], data["user_id"]))
    existing = cursor.fetchone()

    if existing:
        # Update existing quantity
        cursor.execute("""
            UPDATE carttable1 
            SET quantity = quantity + %s 
            WHERE product_id = %s AND user_id = %s
        """, (data["quantity"], data["product_id"], data["user_id"]))
    else:
        # Insert new product into cart
        cursor.execute("""
            INSERT INTO carttable1 
            (product_id, user_id, product_name, product_image, product_price, stock, quantity) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            data["product_id"], data["user_id"], data["product_name"],
            data["product_image"], data["product_price"], data["stock"], data["quantity"]
        ))

    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Product added to cart"}), 201

# 🔹 GET: Retrieve cart items for a user
@carttable.route("/cart/<int:user_id>", methods=["GET"])
def get_cart(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM carttable1 WHERE user_id = %s", (user_id,))
    cart_items = cursor.fetchall()

    cursor.close()
    conn.close()
    return jsonify(cart_items), 200

# 🔹 PUT: Update quantity of a product in cart
@carttable.route("/cart", methods=["PUT"])
def update_cart():
    data = request.get_json()
    if not all(k in data for k in ("user_id", "product_id", "quantity")):
        return jsonify({"error": "Missing required fields"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE carttable1
        SET quantity = %s 
        WHERE product_id = %s AND user_id = %s
    """, (data["quantity"], data["product_id"], data["user_id"]))
    conn.commit()

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return jsonify({"error": "Item not found in cart"}), 404

    cursor.close()
    conn.close()
    return jsonify({
        "message": "Cart quantity updated successfully",
        "updated_item": {
            "product_id": data["product_id"],
            "user_id": data["user_id"],
            "quantity": data["quantity"]
        }
    }), 200

# 🔹 DELETE: Remove a product from cart
@carttable.route("/cart", methods=["DELETE"])
def delete_from_cart():
    data = request.get_json()
    if not all(k in data for k in ("user_id", "product_id")):
        return jsonify({"error": "Missing required fields"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM carttable1 
        WHERE product_id = %s AND user_id = %s
    """, (data["product_id"], data["user_id"]))
    conn.commit()

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return jsonify({"error": "Item not found in cart"}), 404

    cursor.close()
    conn.close()
    return jsonify({"message": "Item removed from cart"}), 200
