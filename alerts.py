"""
alerts.py
Handles alert generation for detected threats.
"""

ALERT_MESSAGES = {
    'Orbital anomaly': 'CRITICAL: Satellite orbit deviation detected! Immediate action required.',
    'Signal interference': 'WARNING: Signal interference detected. Check communication systems.',
    'Possible debris collision': 'CRITICAL: Possible debris collision! Assess satellite integrity.',
    'Unknown anomaly': 'WARNING: Unclassified anomaly detected. Further analysis needed.',
    'None': 'All systems normal.'
}

ALERT_LEVELS = {
    'HIGH': 'CRITICAL',
    'MEDIUM': 'WARNING',
    'LOW': 'NORMAL'
}

def generate_alert(threat):
    """
    Returns alert dict with message and level.
    """
    alert_type = threat.get('type', 'None')
    risk = threat.get('risk', 'LOW')
    return {
        'message': ALERT_MESSAGES.get(alert_type, 'Unknown alert.'),
        'level': ALERT_LEVELS.get(risk, 'NORMAL'),
        'type': alert_type
    }

if __name__ == '__main__':
    t = {'type': 'Orbital anomaly', 'risk': 'HIGH'}
    print(generate_alert(t))
