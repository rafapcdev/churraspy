from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Inicialização do SQLAlchemy
db = SQLAlchemy()

# Definição do Modelo de Dados
class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), unique=True, nullable=False)  # Identificador do usuário
    data = db.Column(db.JSON)  # Dados do usuário
    created_at = db.Column(db.DateTime, default=datetime.now())  # Data de criação

    def __repr__(self):
        return f"<UserData user_id={self.user_id}, data={self.data}>"
