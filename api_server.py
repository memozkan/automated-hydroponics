import json
from datetime import datetime
from typing import List, Dict

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory store for sensor readings
readings: List[Dict[str, str]] = []


@app.route('/api/readings', methods=['POST'])
def add_reading():
    """Add a new sensor reading.

    Expected JSON payload::
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
    """Return all sensor readings in chronological order."""
    return jsonify(readings)


@app.route('/api/readings/latest', methods=['GET'])
def latest_reading():
    """Return the most recent sensor reading."""
    if not readings:
        return jsonify({'error': 'no readings yet'}), 404
    return jsonify(readings[-1])


if __name__ == '__main__':
    app.run(debug=True)
