from typing import Dict
from . import db

class Users(db.Model):
    __tablename__ = 'Users'
    
    user_id: str = db.Column('UserID', db.String, nullable=False, primary_key=True)
    email: str = db.Column('Email', db.String)
    
    def to_dict(self) -> Dict:
        return {
            'user_id': self.user_id,
            'email': self.email
        }

class Detectors(db.Model):
    __tablename__ = 'Detectors'
    
    detector_id: int = db.Column('DetectorID', db.Integer, nullable=False, primary_key=True)
    detector_name: str = db.Column('DetectorName', db.String, nullable=False)
    
    user_id: str = db.Column(db.ForeignKey('Users.UserID'))
    
    def to_dict(self) -> Dict:
        return {
            'user_id': self.user_id,
            'detector_id': self.detector_id,
            'detector_name': self.detector_name
        }
    
class Predictions(db.Model):
    __tablename__ = 'Predictions'
    
    prediction_id: int = db.Column('PredictionID', db.Integer, nullable=False, primary_key=True)
    is_valid: bool = db.Column('IsValid', db.Boolean, nullable=False)
    
    user_id: str = db.Column(db.ForeignKey('Users.UserID'))
    
    def to_dict(self) -> Dict:
        return {
            'user_id': self.user_id,
            'prediction_id': self.prediction_id,
            'is_valid': self.is_valid
        }
    
class Samples(db.Model):
    __tablename__ = 'Samples'
    
    sample_id: int = db.Column('SampleID', db.Integer, nullable=False, primary_key=True)
    longitude: float = db.Column('Longitude', db.Float, nullable=False)
    latitude: float = db.Column('Latitude', db.Float, nullable=False)
    temperature: float = db.Column('Temperature', db.Float, nullable=False)
    barametric_pressure: float = db.Column('BarametricPressure', db.Float, nullable=False)
    altitude: float = db.Column('Alitude', db.Float, nullable=False)

    user_id: str = db.Column(db.ForeignKey('Users.UserID'))
    
    def to_dict(self) -> Dict:
        return {
            'user_id': self.user_id,
            'sample_id': self.sample_id,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'temperature': self.temperature,
            'barametric_pressure': self.barametric_pressure,
            'altitude': self.altitude
        }
