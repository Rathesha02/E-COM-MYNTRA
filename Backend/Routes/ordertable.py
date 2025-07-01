from flask import Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
import mysql.connector
import traceback

ordertable = Blueprint('ordertable', __name__)
CORS(ordertable, supports_credentials=True, origins=["http://localhost:5173"])

# ✅ Database connection
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        port=3307,
        user='root',
        password='',
        database='myntra'
    )

# 🔹 1. CREATE – Place new order
@ordertable.route('/orders', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True, origins=["http://localhost:5173"])
def create_order():
    if request.method == 'OPTIONS':
        return jsonify({"message": "CORS preflight successful"}), 200

    try:
        data = request.get_json()

        user_id = data.get('user_id')
        product_id = data.get('product_id')
        product_name = data.get('product_name')
        product_price = data.get('product_price')
        product_image = data.get('product_image')
        quantity = data.get('quantity', 1)
        total_price = data.get('total_price')
        delivery_address = data.get('delivery_address')
        payment = data.get('payment')
        status = data.get('status', 'pending')

        if not user_id or not product_id or not product_name or not delivery_address or not payment:
            return jsonify({'error': 'Missing required fields'}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO ordertable 
            (user_id, product_id, product_name, product_price, product_image, quantity, total_price, delivery_address, payment, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (user_id, product_id, product_name, product_price, product_image, quantity, total_price, delivery_address, payment, status))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'message': '✅ Order placed successfully'}), 200

    except Exception:
        print("❌ CREATE Order Error:\n", traceback.format_exc())
        return jsonify({'error': 'Internal Server Error'}), 500


# 🔹 2. READ – Get all orders for a user
@ordertable.route('/orders', methods=['GET'])
@cross_origin(supports_credentials=True, origins=["http://localhost:5173"])
def get_orders():
    try:
        user_id = request.args.get('user_id')

        if not user_id:
            return jsonify({'error': 'Missing user_id'}), 400

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM ordertable WHERE user_id = %s", (user_id,))
        orders = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify(orders), 200

    except Exception:
        print("❌ GET Orders Error:\n", traceback.format_exc())
        return jsonify({'error': 'Internal Server Error'}), 500


# 🔹 3. UPDATE – Update order status
@ordertable.route('/orders/<int:id>', methods=['PUT', 'OPTIONS'])
@cross_origin(supports_credentials=True, origins=["http://localhost:5173"])
def update_order(id):
    if request.method == 'OPTIONS':
        return jsonify({"message": "CORS preflight successful"}), 200

    try:
        data = request.get_json()
        status = data.get('status')

        if not status:
            return jsonify({'error': 'Missing status'}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("UPDATE ordertable SET status = %s WHERE order_id = %s", (status, id))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': f'✅ Order #{id} updated to "{status}"'}), 200

    except Exception:
        print("❌ UPDATE Order Error:\n", traceback.format_exc())
        return jsonify({'error': 'Internal Server Error'}), 500


# 🔹 4. DELETE – Delete specific order
@ordertable.route('/orders/<int:id>', methods=['DELETE', 'OPTIONS'])
@cross_origin(supports_credentials=True, origins=["http://localhost:5173"])
def delete_order(id):
    if request.method == 'OPTIONS':
        return jsonify({"message": "CORS preflight successful"}), 200

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM ordertable WHERE order_id = %s", (id,))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': f'🗑️ Order #{id} deleted'}), 200

    except Exception:
        print("❌ DELETE Order Error:\n", traceback.format_exc())
        return jsonify({'error': 'Internal Server Error'}), 500
