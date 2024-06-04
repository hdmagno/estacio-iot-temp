from flask import Blueprint, render_template, request, jsonify
from . import socketio
import logging

main = Blueprint('main', __name__)

logging.basicConfig(filename='temperature.log', level=logging.INFO, format='%(asctime)s - %(message)s')

received_temperature = None

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/temperature', methods=['POST'])
def receive_temperature():
    global received_temperature
    data = request.json
    received_temperature = data.get('temperature')
    logging.info(f"Temperatura recebida: {received_temperature}°C")
    socketio.emit('new_temperature', {'temperature': received_temperature})
    return jsonify({"message": "Temperatura recebida com sucesso"}), 200

@main.route('/temperature', methods=['GET'])
def provide_temperature():
    if received_temperature is not None:
        return jsonify({"temperature": received_temperature}), 200
    else:
        return jsonify({"error": "Temperatura não disponível"}), 404
