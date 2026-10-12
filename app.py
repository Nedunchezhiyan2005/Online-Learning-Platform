import os
from flask import Flask, render_template
from dotenv import load_dotenv
from config import config_by_name
from extensions import db, csrf
from models import User, Course, Lesson, Enrollment, LessonProgress

# Load environment variables from .env file if present
load_dotenv()

def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'development')

    app = Flask(__name__)
    app.config.from_object(config_by_name.get(config_name, config_by_name['default']))

    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    # Initialize extensions
    db.init_app(app)
    csrf.init_app(app)

    # Register blueprints
    from routes.auth import auth_bp
    from routes.courses import courses_bp
    from routes.student import student_bp
    from routes.admin import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(admin_bp)

    # Public landing page
    @app.route('/')
    def index():
        featured_courses = Course.query.filter_by(is_published=True).order_by(Course.created_at.desc()).limit(3).all()
        total_courses = Course.query.filter_by(is_published=True).count()
        total_students = User.query.filter_by(role='student').count()
        return render_template(
            'index.html',
            featured_courses=featured_courses,
            total_courses=total_courses,
            total_students=total_students
        )

    # Error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    # Context processors for global template helpers
    @app.context_processor
    def inject_now():
        from datetime import datetime, timezone
        return {'current_year': datetime.now(timezone.utc).year}

    # Register CLI commands
    register_commands(app)

    return app


def register_commands(app):
    @app.cli.command('init-db')
    def init_db():
        """Create all database tables."""
        with app.app_context():
            db.create_all()
            print("Database initialized successfully.")

    @app.cli.command('create-admin')
    def create_admin():
        """Create an administrator account from environment variables or interactive prompt."""
        import click
        with app.app_context():
            db.create_all()
            admin_email = os.environ.get('ADMIN_EMAIL') or click.prompt('Admin Email', default='admin@learningplatform.edu')
            existing = User.query.filter_by(email=admin_email).first()
            if existing:
                if existing.role == 'admin':
                    print(f"Administrator with email '{admin_email}' already exists.")
                    return
                else:
                    existing.role = 'admin'
                    db.session.commit()
                    print(f"User '{admin_email}' promoted to administrator.")
                    return

            admin_name = os.environ.get('ADMIN_NAME') or click.prompt('Admin Full Name', default='System Administrator')
            admin_pass = os.environ.get('ADMIN_PASSWORD') or click.prompt('Admin Password', hide_input=True, confirmation_prompt=True)

            admin = User(
                full_name=admin_name,
                email=admin_email.lower().strip(),
                role='admin',
                is_active=True
            )
            admin.set_password(admin_pass)
            db.session.add(admin)
            db.session.commit()
            print(f"Administrator '{admin_email}' created successfully.")


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    # Default bind to 127.0.0.1 as specified in requirements
    host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_RUN_PORT', 5000))
    debug = False
    app.run(host=host, port=port, debug=debug)
