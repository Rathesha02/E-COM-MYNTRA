from flask import Flask, send_from_directory
from flask_cors import CORS

from Routes.usertable import usertable
from Routes.producttable import producttable
from Routes.ordertable import ordertable
from Routes.carttable import carttable

app = Flask(__name__)

# ✅ CORS: allow requests from React frontend to /api/*
CORS(app, supports_credentials=True, origins=["http://localhost:5173"])
# ✅ Register Blueprints at `/api` prefix
app.register_blueprint(usertable, url_prefix='/api')
app.register_blueprint(producttable, url_prefix='/api')
app.register_blueprint(ordertable, url_prefix='/api')
app.register_blueprint(carttable, url_prefix='/api')

# ✅ Serve images from Static folder
@app.route('/Static/Images/<path:filename>')
def serve_image(filename):
    return send_from_directory('Static/Images', filename)

# ✅ Root test route
@app.route('/')
def home():
    return {'message': 'Welcome to E-Commerce'}, 200

if __name__ == '__main__':
    app.run(debug=True)
