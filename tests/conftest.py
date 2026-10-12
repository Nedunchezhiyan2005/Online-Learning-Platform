import pytest
from app import create_app
from extensions import db
from models import User, Course, Lesson, Enrollment, LessonProgress

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def student_user(app):
    with app.app_context():
        user = User(
            full_name="Test Student",
            email="student@test.com",
            role="student",
            is_active=True
        )
        user.set_password("StudentPass123!")
        db.session.add(user)
        db.session.commit()
        return user.id

@pytest.fixture
def admin_user(app):
    with app.app_context():
        user = User(
            full_name="Test Administrator",
            email="admin@test.com",
            role="admin",
            is_active=True
        )
        user.set_password("AdminPass123!")
        db.session.add(user)
        db.session.commit()
        return user.id

@pytest.fixture
def sample_course(app):
    with app.app_context():
        course = Course(
            title="Introduction to DevOps",
            description="Comprehensive introduction to DevOps and CI/CD pipelines.",
            instructor="Prof. Smith",
            category="Cloud & DevOps",
            duration="4 Weeks",
            learning_objectives="- Master Git\n- Learn Docker\n- Automate with Jenkins",
            is_published=True
        )
        db.session.add(course)
        db.session.commit()

        lesson1 = Lesson(
            course_id=course.id,
            title="Lesson 1: Git Essentials",
            content="Detailed material about Git and version control systems.",
            lesson_order=1,
            resource_url="https://git-scm.com"
        )
        lesson2 = Lesson(
            course_id=course.id,
            title="Lesson 2: Docker Containers",
            content="Detailed material about containerization.",
            lesson_order=2,
            resource_url="https://docker.com"
        )
        db.session.add_all([lesson1, lesson2])
        db.session.commit()
        return course.id
