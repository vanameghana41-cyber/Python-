from functools import wraps

is_logged_in = False

def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please log in.")
    return wrapper

@require_login
def secret_data():
    print("Sensitive information here!")

secret_data()

is_logged_in = True
secret_data()
'''Access denied. Please log in.
Sensitive information here!'''
