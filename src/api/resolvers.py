from typing import Any, Dict
from .models import *
from ariadne import convert_kwargs_to_snake_case

#---Queries---

@convert_kwargs_to_snake_case
def resolve_get_user(obj, info, user_id: str):
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
            'errors': [f'User {user_id} not found']
        }

    return payload

#---Mutations---

@convert_kwargs_to_snake_case
def resolve_add_user(obj, info, user: Users):
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

@convert_kwargs_to_snake_case
def resolve_update_user(obj, info, new_info: Users):
    try:
        user: Users = Users.query.get(new_info.user_id)
        user.__dict__.update(new_info.__dict__)
        
        with db.session.begin():
            db.session.add(user)
            
        payload = {
            'success': True, 
            'user': user.to_dict();
        }
        
    except:
        