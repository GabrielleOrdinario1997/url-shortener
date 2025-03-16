from flask import Flask
from flask_cors import CORS

from backend.url_conversion import shortener_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(shortener_bp)
if __name__ == '__main__':
    app.run(debug=True)