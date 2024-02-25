from typing import Any, Dict
from .models import *
from ariadne import convert_kwargs_to_snake_case

#---Queries---

@convert_kwargs_to_snake_case
def resolve_get_user(obj, info, user_id):
    try:
        user = Users.query.get(user_id)
        assert user 
        payload = {
            'success': True,
            'user': user.to_dict()
        }

    except AssertionError:
        payload = {
            'success': False,
            'errors': [f'User with ID `{user_id}` not found']
        }

    return payload

@convert_kwargs_to_snake_case
def resolve_get_detector(obj, info, detector_id):
    try:
        detector = Users.query.get(detector_id)
        assert detector
        payload = {
            'success': True,
            'user': detector.to_dict()
        }

    except AssertionError:
        payload = {
            'success': False,
            'errors': [f'Detector with ID `{detector_id}` not found']
        }

    return payload

@convert_kwargs_to_snake_case
def resolve_get_prediction(obj, info, prediction_id):
    try:
        prediction = Users.query.get(prediction_id)
        assert prediction
        payload = {
            'success': True,
            'user': prediction.to_dict()
        }

    except AssertionError:
        payload = {
            'success': False,
            'errors': [f'Prediction with ID `{prediction_id}` not found']
        }

    return payload

@convert_kwargs_to_snake_case
def resolve_get_sample(obj, info, sample_id):
    try:
        sample = Users.query.get(sample_id)
        assert sample
        payload = {
            'success': True,
            'user': sample.to_dict()
        }

    except AssertionError:
        payload = {
            'success': False,
            'errors': [f'Sample with ID `{sample_id}` not found']
        }

    return payload

#---User Mutations---

@convert_kwargs_to_snake_case
def resolve_add_user(obj, info, user):
    try:
        with db.session.begin():
            db.session.add(user)
        
        payload = {
            'success': True,
            'user': user.to_dict()
        }
        
    except TypeError:
        payload = {
            'success': False,
            'errors': ['Invalid Type']
        }
    
    return payload

@convert_kwargs_to_snake_case
def resolve_update_user(obj, info, new_info):
    try:
        user = Users.query.get(new_info.user_id)
        user.__dict__.update(new_info.__dict__)
        
        assert user is not None
        
        with db.session.begin():
            db.session.add(user)
            
        payload = {
            'success': True,
            'user': user.to_dict()
        }
        
    except AssertionError:
        payload = {
            'success': False,
            'errors': [f'User with ID `{new_info.user_id}` not found']
        }
        
    return payload

@convert_kwargs_to_snake_case
def resolve_delete_user(obj, info, user_id):
    try:
        user = Users.query.get(user_id)
        assert user is not None
        
        with db.session.begin():
            db.session.delete(user)
            
        payload = {
            'success': True
        }
        
    except AssertionError:
        payload = {
            'success': False,
            'errors': [f'User with ID `{user_id}` not found']
        }
        
    return payload

#---Detector Mutations---

@convert_kwargs_to_snake_case
def resolve_add_detector(obj, info, detector):
    try:
        with db.session.begin():
            db.session.add(detector)
        
        payload = {
            'success': True,
            'user': detector.to_dict()
        }
        
    except TypeError:
        payload = {
            'success': False,
            'errors': ['Invalid Type']
        }
    
    return payload

@convert_kwargs_to_snake_case
def resolve_update_detector(obj, info, new_info):
    try:
        detector = Users.query.get(new_info.detector_id)
        detector.__dict__.update(new_info.__dict__)
        
        assert detector is not None
        
        with db.session.begin():
            db.session.add(detector)
            
        payload = {
            'success': True,
            'user': detector.to_dict()
        }
        
    except AssertionError:
        payload = {
            'success': False,
            'errors': [f'Detector with ID `{new_info.detector_id}` not found']
        }
        
    return payload

@convert_kwargs_to_snake_case
def resolve_delete_detector(obj, info, detector_id):
    try:
        detector = Users.query.get(detector_id)
        assert detector is not None
        
        with db.session.begin():
            db.session.delete(detector)
            
        payload = {
            'success': True
        }
        
    except AssertionError:
        payload = {
            'success': False,
            'errors': [f'Detector with ID `{detector_id}` not found']
        }
        
    return payload

#---Sample Mutations---

@convert_kwargs_to_snake_case
def resolve_add_sample(obj, info, sample):
    try:
        with db.session.begin():
            db.session.add(sample)
        
        payload = {
            'success': True,
            'user': sample.to_dict()
        }
        
    except TypeError:
        payload = {
            'success': False,
            'errors': ['Invalid Type']
        }
    
    return payload

@convert_kwargs_to_snake_case
def resolve_update_sample(obj, info, new_info):
    try:
        sample = Users.query.get(new_info.sample_id)
        sample.__dict__.update(new_info.__dict__)
        
        assert sample is not None
        
        with db.session.begin():
            db.session.add(sample)
            
        payload = {
            'success': True,
            'user': sample.to_dict()
        }
        
    except AssertionError:
        payload = {
            'success': False,
            'errors': [f'Sample with ID `{new_info.sample_id}` not found']
        }
        
    return payload

@convert_kwargs_to_snake_case
def resolve_delete_sample(obj, info, sample_id):
    try:
        sample = Users.query.get(sample_id)
        assert sample is not None
        
        with db.session.begin():
            db.session.delete(sample)
            
        payload = {
            'success': True
        }
        
    except AssertionError:
        payload = {
            'success': False,
            'errors': [f'Sample with ID `{sample_id}` not found']
        }
        
    return payload

#---Prediction Mutations---

@convert_kwargs_to_snake_case
def resolve_add_prediction(obj, info, prediction):
    try:
        with db.session.begin():
            db.session.add(prediction)
        
        payload = {
            'success': True,
            'user': prediction.to_dict()
        }
        
    except TypeError:
        payload = {
            'success': False,
            'errors': ['Invalid Type']
        }
    
    return payload

@convert_kwargs_to_snake_case
def resolve_update_prediction(obj, info, new_info):
    try:
        prediction = Users.query.get(new_info.prediction_id)
        prediction.__dict__.update(new_info.__dict__)
        
        assert prediction is not None
        
        with db.session.begin():
            db.session.add(prediction)
            
        payload = {
            'success': True,
            'user': prediction.to_dict()
        }
        
    except AssertionError:
        payload = {
            'success': False,
            'errors': [f'Prediction with ID `{new_info.prediction_id}` not found']
        }
        
    return payload

@convert_kwargs_to_snake_case
def resolve_delete_prediction(obj, info, prediction_id):
    try:
        prediction = Users.query.get(prediction_id)
        assert prediction is not None
        
        with db.session.begin():
            db.session.delete(prediction)
            
        payload = {
            'success': True
        }
        
    except AssertionError:
        payload = {
            'success': False,
            'errors': [f'Prediction with ID `{prediction_id}` not found']
        }
        
    return payload

