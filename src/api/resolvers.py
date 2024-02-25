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

#---Mutations---

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

