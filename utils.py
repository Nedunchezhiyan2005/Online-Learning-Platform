from functools import wraps
from flask import session, redirect, url_for, flash, abort, g
from extensions import db
from models import User

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please sign in to access this page.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                flash('Please sign in to access this page.', 'warning')
                return redirect(url_for('auth.login'))
            user = db.session.get(User, session['user_id'])
            if not user or not user.is_active or user.role != role:
                flash('Access denied. You do not have permission to view this resource.', 'danger')
                if user and user.role == 'student':
                    return redirect(url_for('student.dashboard'))
                elif user and user.role == 'admin':
                    return redirect(url_for('admin.dashboard'))
                return redirect(url_for('auth.login'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def admin_required(f):
    return role_required('admin')(f)

def student_required(f):
    return role_required('student')(f)
