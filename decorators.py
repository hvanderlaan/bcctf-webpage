from functools import wraps
from flask import session, redirect, url_for
from models import User
from typing import Any, Callable

def login_required(f: callable):
    '''
    login_required decorator
    
    :param f: Function
    :type f: callable
    '''
    @wraps(f)
    def wrapper(*args, **kwargs) -> Any:
        '''
        wrapper function for login_required decorator
        
        :param args: Any argument(s)
        :param kwargs: Any keyword argumnet(s)
        :return: wrapped function
        :rtype: Any
        '''
        if "user_id" not in session:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return wrapper

def admin_required(f: callable):
    '''
    admin_required decorator
    
    :param f: Function
    :type f: callable
    '''
    @wraps(f)
    def wrapper(*args, **kwargs) -> Any:
        '''
        wrapper function for admin_required decorator
        
        :param args: Any argument(s)
        :param kwargs: Any keyword argumnet(s)
        :return: wrapped function
        :rtype: Any
        '''
        user: User = User.query.get(session.get("user_id"))
        if not user or not user.is_admin:
            return redirect(url_for("main.index"))
        return f(*args, **kwargs)
    return wrapper
