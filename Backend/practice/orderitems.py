from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        port=3307,           # port should be int, not string
        password='',
        database='meesho'
    )

# Create an order item
@app.route('/api/order-items', methods=['POST'])
def create_order_item():
    try:
        data = request.get_json()
        print("Received JSON:", data)  # Debug print

        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO order_items (order_id, product_id, quantity, price)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (
            data['order_id'],
            data['product_id'],
            data['quantity'],
            data['price']
        ))
        conn.commit()
        item_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return jsonify({'message': 'Order item created', 'item_id': item_id}), 201
    except Exception as e:
        print("Error in create_order_item:", e)
        return jsonify({'error': str(e)}), 500

# Get all order items
@app.route('/api/order-items', methods=['GET'])
def get_order_items():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM order_items")
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(items)

# Get a single order item by ID
@app.route('/api/order-items/<int:item_id>', methods=['GET'])
def get_order_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM order_items WHERE id = %s", (item_id,))
    item = cursor.fetchone()
    cursor.close()
    conn.close()
    if item:
        return jsonify(item)
    return jsonify({'error': 'Order item not found'}), 404

# Update an order item
@app.route('/api/order-items/<int:item_id>', methods=['PUT'])
def update_order_item(item_id):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        UPDATE order_items
        SET order_id = %s, product_id = %s, quantity = %s, price = %s
        WHERE id = %s
    """
    cursor.execute(query, (
        data['order_id'],
        data['product_id'],
        data['quantity'],
        data['price'],
        item_id
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Order item updated'})

# Delete an order item
@app.route('/api/order-items/<int:item_id>', methods=['DELETE'])
def delete_order_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM order_items WHERE id = %s", (item_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Order item deleted'})

if __name__ == '__main__':
    app.run(debug=True)
