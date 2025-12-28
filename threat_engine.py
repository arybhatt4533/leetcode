"""
threat_engine.py
Classifies threat type and assigns risk score.
"""

def classify_threat(telemetry, anomaly_status):
    """
    Classify threat type and assign risk score.
    Returns: dict with type, risk, and description.
    """
    if anomaly_status != 'ANOMALY':
        return {'type': 'None', 'risk': 'LOW', 'description': 'No threat detected.'}

    # Simple rules for threat classification
    if telemetry['altitude'] < 355 or telemetry['altitude'] > 445:
        return {'type': 'Orbital anomaly', 'risk': 'HIGH', 'description': 'Satellite orbit deviation detected.'}
    elif telemetry['signal_strength'] < 70:
        return {'type': 'Signal interference', 'risk': 'MEDIUM', 'description': 'Possible signal jamming or interference.'}
    elif abs(telemetry['velocity'] - 7.8) > 0.4:
        return {'type': 'Possible debris collision', 'risk': 'HIGH', 'description': 'Velocity anomaly suggests possible collision.'}
    else:
        return {'type': 'Unknown anomaly', 'risk': 'MEDIUM', 'description': 'Unclassified anomaly detected.'}

if __name__ == '__main__':
    # Example usage
    t = {'altitude': 350, 'velocity': 7.8, 'signal_strength': 95}
    print(classify_threat(t, 'ANOMALY'))
