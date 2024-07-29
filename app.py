rom flask import Flask, request, jsonify
from models import db, Vuelo
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vuelos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return "Bienvenido a la búsqueda de vuelos."

@app.route('/buscar_vuelos', methods=['GET'])
def buscar_vuelos():
    origen = request.args.get('origen')
    destino = request.args.get('destino')
    fecha_salida = request.args.get('fecha_salida')

    if not origen or not destino or not fecha_salida:
        return jsonify({"error": "Por favor, proporciona origen, destino y fecha de salida"}), 400

    try:
        fecha_salida = datetime.strptime(fecha_salida, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"error": "Formato de fecha inválido. Use AAAA-MM-DD"}), 400

    vuelos = Vuelo.query.filter_by(origen=origen, destino=destino, fecha_salida=fecha_salida).all()

    resultado = []
    for vuelo in vuelos:
        resultado.append({
            "id": vuelo.id,
            "origen": vuelo.origen,
            "destino": vuelo.destino,
            "fecha_salida": vuelo.fecha_salida.strftime('%Y-%m-%d'),
            "hora_salida": vuelo.hora_salida.strftime('%H:%M:%S'),
            "precio": vuelo.precio
        })

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
