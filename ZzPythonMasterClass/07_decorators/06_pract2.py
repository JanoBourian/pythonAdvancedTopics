"""
Example to use of decorator  
in an 'Authentication' function
"""

# Decorator function


def verify_auth(func):
    # verify_auth recibes a function welcome_message
    def wrapper(*args, **kwargs):
        # wrapper recibes an arguments of welcome_message function
        if args[0]['auth']:
            # if auth is True, return welcome_message
            return func(*args, **kwargs)
    return wrapper


user = {
    'name': 'janobourian',
    'auth': True
}


@verify_auth
def welcome_message(user):
    print(f"Hello {user['name']}")


welcome_message(user)

# if 'auth' : False, no output
# if 'auth' : True, Output -> Hello janobourian
