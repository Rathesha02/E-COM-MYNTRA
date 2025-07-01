from flask import Blueprint, request, jsonify
import mysql.connector
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from flask_cors import cross_origin

producttable = Blueprint('producttable', __name__)
CORS(producttable)

# ⚡️ Database Connection
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        port=3307,
        user='root',
        password='',
        database='myntra'
    )

# ⚡️ Directory for uploaded images
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ⚡️ Create a Product
@producttable.route('/products', methods=['POST'])
def create_product():
    if 'name' not in request.form or 'price' not in request.form:
        return jsonify({'error': 'name and price are required'}), 400

    name = request.form['name']
    price = float(request.form['price'])
    stock = int(request.form.get('stock', 0))
    description = request.form.get('description', '')
    category = request.form.get('category', '')
    image_file = request.files.get('image')
    image_filename = None

    if image_file:
        image_filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(UPLOAD_FOLDER, image_filename))

    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO producttable (name, price, stock, image, description, category)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (name, price, stock, image_filename, description, category))
    conn.commit()
    product_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return jsonify({'message': 'Product created', 'product_id': product_id}), 201

# ⚡️ Get All Products
@producttable.route('/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id AS productid, name, price, stock, image, description, category FROM producttable")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(products)  # Always return a list

# ⚡️ Get a Single Product
@producttable.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT id AS productid, name, price, stock, image, description, category 
        FROM producttable WHERE id = %s
    """, (product_id,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()

    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404

# ⚡️ Update a Product
@producttable.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Check if product exists
    cursor.execute("SELECT * FROM producttable WHERE id = %s", (product_id,))
    existing_product = cursor.fetchone()
    if not existing_product:
        cursor.close()
        conn.close()
        return jsonify({'error': 'Product not found'}), 404

    # Get updated fields
    name = request.form.get('name', existing_product['name'])
    price = float(request.form.get('price', existing_product['price']))
    stock = int(request.form.get('stock', existing_product['stock']))
    description = request.form.get('description', existing_product['description'])
    category = request.form.get('category', existing_product['category'])
    image_file = request.files.get('image')
    image_filename = existing_product['image']

    # If new image uploaded, update it
    if image_file:
        image_filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(UPLOAD_FOLDER, image_filename))

    # Update query
    query = """
        UPDATE producttable
        SET name=%s, price=%s, stock=%s, image=%s, description=%s, category=%s
        WHERE id=%s
    """
    cursor = conn.cursor()
    cursor.execute(query, (
        name, price, stock, image_filename, description, category, product_id
    ))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Product updated'})

# ⚡️ Delete a Product
@producttable.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM producttable WHERE id = %s", (product_id,))
    conn.commit()
    affected = cursor.rowcount
    cursor.close()
    conn.close()

    if affected == 0:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({'message': 'Product deleted'})
