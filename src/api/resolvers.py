from typing import Any, Dict
from .models import *
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def resolve_get_user(obj, info, user_id):

    try:
        user = Users.query.get(user_id)
        payload = {
            'success': True,
            'user': user
        }

    except AttributeError:
        payload = {
            'success': False,
            'errors': [f'User {user_id} not found']
        }

    return payload

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
