from ast import Tuple
from . import db
from typing import Any, Dict, List
from inspect import getmembers, isroutine

class Users(db.Model):
    __tablename__ = 'Users'
    
    user_id: int = db.Column('UserId', db.Integer, primary_key=True)
    user_name: int = db.Column('UserName', db.String)
    email: str = db.Column('Email', db.String)
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'email': self.email
        }

class Detectors(db.Model):
    __tablename__ = 'Detectors'
    
    detector_id: int = db.Column('DetectorID', db.Integer, primary_key=True)
    detector_name: str = db.Column('DetectorName', db.String)
    
    user_id: int = db.Column(db.ForeignKey('Users.UserID'))
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'detector_id': self.detector_id,
            'detector_name': self.detector_name
        }
    
class Predictions(db.Model):
    __tablename__ = 'Predictions'
    
    prediction_id: int = db.Column('PredictionID', db.Integer, primary_key=True)
    is_valid: bool = db.Column('IsValid', db.Boolean)
    
    user_id: int = db.Column(db.ForeignKey('Users.UserID'))
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'prediction_id': self.prediction_id,
            'is_valid': self.is_valid
        }
    
class Samples(db.Model):
    __tablename__ = 'Samples'
    
    sample_id: int = db.Column('SampleID', db.Integer, primary_key=True)
    longitude: float = db.Column('Longitude', db.Float)
    latitude: float = db.Column('Latitude', db.Float)
    barametric_pressure: float = db.Column('BarametricPressure', db.Float)
    altitude: float = db.Column('Alitude', db.Float)

    user_id: int = db.Column(db.ForeignKey('Users.UserID'))
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'sample_id': self.sample_id,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'barametric_pressure': self.barametric_pressure,
            'altitude': self.altitude
        }
