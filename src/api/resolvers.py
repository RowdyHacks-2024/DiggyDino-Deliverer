from .models import *
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def resolve_get_user(obj, info, user_name):
    try:
        user = Users.query.get(user_name)
        payload = {
            'success': True,
            'user': user      
        }
    
    except AttributeError:
        payload = {
            'success': False,
            'errors': [f'User {user_name} not found']
        }

    return payload

@convert_kwargs_to_snake_case
def resolve_add_user(obj, info):
    