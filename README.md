from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vuelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origen = db.Column(db.String(100), nullable=False)
    destino = db.Column(db.String(100), nullable=False)
    fecha_salida = db.Column(db.Date, nullable=False)
    hora_salida = db.Column(db.Time, nullable=False)
    precio = db.Column(db.Float, nullable=False)
