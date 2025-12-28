"""
model.py
ML anomaly detection using Isolation Forest.
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.is_trained = False

    def train(self, data):
        X = data[['altitude', 'velocity', 'signal_strength']]
        self.model.fit(X)
        self.is_trained = True

    def predict(self, row):
        X = np.array([[row['altitude'], row['velocity'], row['signal_strength']]])
        score = self.model.decision_function(X)[0]
        status = 'ANOMALY' if self.model.predict(X)[0] == -1 else 'NORMAL'
        return {'score': float(score), 'status': status}

# Utility to load and train on CSV
_detector = None

def get_detector():
    global _detector
    if _detector is None:
        df = pd.read_csv('data/satellite.csv')
        _detector = AnomalyDetector()
        _detector.train(df)
    return _detector

def detect_anomaly(row):
    detector = get_detector()
    return detector.predict(row)

if __name__ == '__main__':
    # Test on a sample row
    row = {'altitude': 400, 'velocity': 7.8, 'signal_strength': 95}
    print(detect_anomaly(row))
