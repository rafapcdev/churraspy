from flask import Blueprint
from flask import request, render_template, redirect, url_for, jsonify
from py_scripts.utilidade import get_and_clean_df, get_members
from py_scripts.calculo_churras import calculo_churrasco
from py_scripts.SQL_session import UserData, db

rotas_bp = Blueprint("churras", __name__)

# Rotas
@rotas_bp.route("/", methods=["GET"])
def index():
    df_dict = get_and_clean_df(preco_Final_str=True)
    return render_template("index.html", df_dict=df_dict)

@rotas_bp.route("/resultado", methods=["GET"])
def resultado():
    user_id = "user_123"  # Substitua por um identificador único do usuário (ex: ID de login)
    user_data = UserData.query.filter_by(user_id=user_id).first()

    if user_data:
        data = calculo_churrasco(user_data.data)
   

        if data["Bovinos"] or data["Aves"] or data["Guarnições"] or data["Refrigerantes"] or data["Cervejas"]:
            return render_template("resultado.html", data=data)
    
    return redirect(url_for("churras.index"))

@rotas_bp.route("/calcular", methods=["POST"])
def calcular(): 
    user_id = "user_123"  # Substitua por um identificador único do usuário (ex: ID de login)
    user_data = UserData.query.filter_by(user_id=user_id).first()

    if not user_data:
        # Cria um novo registro se não existir
        user_data = UserData(user_id=user_id, data=0)
        db.session.add(user_data)

    user_data.data = request.get_json()
    db.session.commit()  # Salva as alterações no banco de dados

    return jsonify({"url": url_for("churras.resultado")})

@rotas_bp.route("/desenvolvedores")
def desenvolvedores():
    members = get_members()
    return render_template("desenvolvedores.html", members = members)
