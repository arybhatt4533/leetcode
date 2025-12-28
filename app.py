"""
app.py
Flask app for STDAMS API and dashboard.
"""
from flask import Flask, jsonify, render_template
import pandas as pd
import os
from model import detect_anomaly
from threat_engine import classify_threat
from alerts import generate_alert

app = Flask(__name__)

DATA_FILE = 'data/satellite.csv'

# Helper to get latest telemetry

def get_latest_telemetry():
    if not os.path.exists(DATA_FILE):
        return None
    df = pd.read_csv(DATA_FILE)
    if df.empty:
        return None
    row = df.iloc[-1]
    return {
        'timestamp': row['timestamp'],
        'altitude': float(row['altitude']),
        'velocity': float(row['velocity']),
        'signal_strength': float(row['signal_strength'])
    }

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/telemetry')
def api_telemetry():
    telemetry = get_latest_telemetry()
    return jsonify(telemetry)

@app.route('/api/anomaly')
def api_anomaly():
    telemetry = get_latest_telemetry()
    if not telemetry:
        return jsonify({'status': 'NO DATA'})
    anomaly = detect_anomaly(telemetry)
    return jsonify(anomaly)

@app.route('/api/alerts')
def api_alerts():
    telemetry = get_latest_telemetry()
    if not telemetry:
        return jsonify({'level': 'NORMAL', 'message': 'No telemetry data.', 'type': 'None'})
    anomaly = detect_anomaly(telemetry)
    threat = classify_threat(telemetry, anomaly['status'])
    alert = generate_alert(threat)
    return jsonify(alert)

if __name__ == '__main__':
    app.run(debug=True)
