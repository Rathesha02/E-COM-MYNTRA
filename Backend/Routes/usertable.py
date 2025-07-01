from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
import mysql.connector

usertable = Blueprint('usertable', __name__)

# ✅ Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="myntra",
        port=3307
    )

# ✅ CREATE (Register User)
@usertable.route('/users', methods=['POST', 'OPTIONS'])
@cross_origin(origins="http://localhost:5173", supports_credentials=True)
def register_user():
    if request.method == 'OPTIONS':
        return '', 200

    data = request.get_json()
    username = data['username']
    emailid = data['emailid']
    password = data['password']

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, emailid, password) VALUES (%s, %s, %s)",
                       (username, emailid, password))
        conn.commit()
        return jsonify({'message': 'User registered successfully!'})
    except mysql.connector.Error as err:
        return jsonify({'message': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# ✅ READ (Get All Users)
@usertable.route('/users', methods=['GET'])
@cross_origin(origins="http://localhost:5173", supports_credentials=True)
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

# ✅ UPDATE (Update User by ID)
@usertable.route('/users/<int:user_id>', methods=['PUT', 'OPTIONS'])
@cross_origin(origins="http://localhost:5173", supports_credentials=True)
def update_user(user_id):
    if request.method == 'OPTIONS':
        return '', 200

    data = request.get_json()
    username = data.get('username')
    emailid = data.get('emailid')
    password = data.get('password')

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET username=%s, emailid=%s, password=%s WHERE id=%s",
                       (username, emailid, password, user_id))
        conn.commit()
        return jsonify({'message': 'User updated successfully!'})
    except mysql.connector.Error as err:
        return jsonify({'message': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# ✅ DELETE (Delete User by ID)
@usertable.route('/users/<int:user_id>', methods=['DELETE', 'OPTIONS'])
@cross_origin(origins="http://localhost:5173", supports_credentials=True)
def delete_user(user_id):
    if request.method == 'OPTIONS':
        return '', 200

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        return jsonify({'message': 'User deleted successfully!'})
    except mysql.connector.Error as err:
        return jsonify({'message': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# ✅ LOGIN (Verify Email + Password)
@usertable.route('/users/login', methods=['POST', 'OPTIONS'])
@cross_origin(origins="http://localhost:5173", supports_credentials=True)
def login_user():
    if request.method == 'OPTIONS':
        return '', 200

    data = request.get_json()
    emailid = data['emailid']
    password = data['password']

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE emailid = %s AND password = %s", (emailid, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        return jsonify({'message': 'Login successful!', 'user': user})
    else:
        return jsonify({'message': 'Invalid email or password'}), 401
