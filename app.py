from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Importe o CORS
from datetime import datetime
from py_scripts.utilidade import get_and_clean_df
from py_scripts.calculo_churras import calculo_churrasco
from py_scripts.SQL import atualizar

# Inicialização do Flask
app = Flask(__name__)

# Configuração do CORS
CORS(app, supports_credentials=True, origins=["http://localhost:5000", "http://127.0.0.1:5000", "https://matheuspc.pythonanywhere.com/"])

# Configuração do banco de dados SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicialização do SQLAlchemy
db = SQLAlchemy(app)

# Definição do Modelo de Dados
class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), unique=True, nullable=False)  # Identificador do usuário
    data = db.Column(db.JSON)  # Dados do usuário
    created_at = db.Column(db.DateTime, default=datetime.now())  # Data de criação

    def __repr__(self):
        return f"<UserData user_id={self.user_id}, data={self.data}>"

# Rotas
@app.route("/", methods=["GET"])
def index():
    df_dict = get_and_clean_df(preco_Final_str=True)
    return render_template("index.html", df_dict=df_dict)

@app.route("/resultado", methods=["GET"])
def resultado():
    user_id = "user_123"  # Substitua por um identificador único do usuário (ex: ID de login)
    user_data = UserData.query.filter_by(user_id=user_id).first()

    if user_data:
        data = calculo_churrasco(user_data.data)
   

        if data["Bovinos"] or data["Aves"] or data["Guarnições"] or data["Refrigerantes"] or data["Cervejas"]:
            return render_template("resultado.html", data=data)
    
    return redirect(url_for("index"))

@app.route("/calcular", methods=["POST"])
def calcular(): 
    user_id = "user_123"  # Substitua por um identificador único do usuário (ex: ID de login)
    user_data = UserData.query.filter_by(user_id=user_id).first()

    if not user_data:
        # Cria um novo registro se não existir
        user_data = UserData(user_id=user_id, data=0)
        db.session.add(user_data)

    user_data.data = request.get_json()
    db.session.commit()  # Salva as alterações no banco de dados

    return jsonify({"url": url_for("resultado")})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=False)