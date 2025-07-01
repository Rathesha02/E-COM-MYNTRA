from flask import Flask, request, jsonify, send_from_directory
import mysql.connector
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# MySQL config (update according to your XAMPP settings)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cardapp'

# Folder to store uploaded images (use XAMPP's htdocs/uploads)
UPLOAD_FOLDER = 'C:/xampp/htdocs/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



# Upload image and save metadata
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['image']
    name = request.form.get('name')

    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    filename = file.filename
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(save_path)

    # Save to DB
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO images (name, image_path) VALUES (%s, %s)", (name, filename))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Image uploaded successfully'}), 200

# Get all uploaded images
@app.route('/images', methods=['GET'])
def get_images():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, image_path FROM images")
    data = cur.fetchall()
    cur.close()

    result = [{'id': row[0], 'name': row[1], 'image_url': f"http://localhost/uploads/{row[2]}"} for row in data]
    return jsonify(result)


@app.route('/db-check')
def db_check():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()
        return jsonify({"status": "success", "message": f"MySQL version: {version[0]}"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '_main_':
    app.run(port=5000, debug=True)