"""Basit bir sensör okuma API sunucusu."""

import json
from datetime import datetime
from typing import List, Dict

from flask import Flask, request, jsonify

app = Flask(__name__)

# Sensör okumalarını bellekte tutan yapı
readings: List[Dict[str, str]] = []


@app.route('/api/readings', methods=['POST'])
def add_reading():
    """Yeni bir sensör okuması ekle.

    Beklenen JSON yükü::
        {
            "light": <int>,
            "ph": <float>,
            "ec": <float>
        }
    """
    data = request.get_json(force=True)
    reading = {
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'light': data.get('light'),
        'ph': data.get('ph'),
        'ec': data.get('ec'),
    }
    readings.append(reading)
    return jsonify(reading), 201


@app.route('/api/readings', methods=['GET'])
def list_readings():
    """Tüm sensör okumalarını kronolojik olarak döndür."""
    return jsonify(readings)


@app.route('/api/readings', methods=['DELETE'])
def clear_readings():
    """Tüm sensör okumalarını temizle."""
    readings.clear()
    return '', 204


@app.route('/api/readings/latest', methods=['GET'])
def latest_reading():
    """En son sensör okumasını döndür."""
    if not readings:
        return jsonify({'error': 'henüz veri yok'}), 404
    return jsonify(readings[-1])


if __name__ == '__main__':
    app.run(debug=True)
