from flask import Flask
from routes.churras import rotas_bp
from flask_cors import CORS

# Inicialização do Flask
app = Flask(__name__)
app.register_blueprint(rotas_bp)

# Configuração do CORS
CORS(app, supports_credentials=True, origins=["http://localhost:5000", "http://127.0.0.1:5000", "https://matheuspc.pythonanywhere.com/"])

# Configuração do banco de dados SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

from py_scripts.SQL_session import db

db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all() 
    app.run(debug=False)