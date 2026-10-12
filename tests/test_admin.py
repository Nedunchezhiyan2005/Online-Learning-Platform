from extensions import db
from models import Course, Lesson, User

def test_admin_route_protection_for_students(client, student_user):
    """Test students cannot access admin console routes."""
    client.post('/auth/login', data={'email': 'student@test.com', 'password': 'StudentPass123!'})
    
    response = client.get('/admin/dashboard', follow_redirects=True)
    assert response.status_code == 200
    assert b"Access denied" in response.data

def test_admin_dashboard_metrics(client, admin_user, sample_course):
    """Test admin dashboard loads metrics."""
    client.post('/auth/login', data={'email': 'admin@test.com', 'password': 'AdminPass123!'})
    
    response = client.get('/admin/dashboard')
    assert response.status_code == 200
    assert b"Administrative Overview" in response.data
    assert b"Total Courses" in response.data

def test_admin_course_create_edit_delete(client, admin_user, app):
    """Test full admin CRUD lifecycle on courses."""
    client.post('/auth/login', data={'email': 'admin@test.com', 'password': 'AdminPass123!'})

    # Create
    resp_create = client.post('/admin/courses/new', data={
        'title': 'Automated CI/CD with Jenkins',
        'category': 'Cloud & DevOps',
        'instructor': 'Sarah Connor',
        'duration': '5 Weeks',
        'description': 'End to end testing and Jenkins pipeline automation.',
        'learning_objectives': '- Write Jenkinsfile\n- Run Docker agents',
        'is_published': True
    }, follow_redirects=True)
    assert resp_create.status_code == 200

    with app.app_context():
        course = Course.query.filter_by(title='Automated CI/CD with Jenkins').first()
        assert course is not None
        course_id = course.id

    # Edit
    resp_edit = client.post(f'/admin/courses/{course_id}/edit', data={
        'title': 'Automated CI/CD with Jenkins (Updated)',
        'category': 'Cloud & DevOps',
        'instructor': 'Sarah Connor',
        'duration': '6 Weeks',
        'description': 'Updated description.',
        'learning_objectives': '- Write Jenkinsfile',
        'is_published': True
    }, follow_redirects=True)
    assert resp_edit.status_code == 200
    assert b"updated successfully" in resp_edit.data

    # Delete
    resp_delete = client.post(f'/admin/courses/{course_id}/delete', follow_redirects=True)
    assert resp_delete.status_code == 200
    assert b"deleted" in resp_delete.data

    with app.app_context():
        course_deleted = db.session.get(Course, course_id)
        assert course_deleted is None

def test_admin_student_status_toggle(client, admin_user, student_user, app):
    """Test admin can deactivate and reactivate student accounts."""
    client.post('/auth/login', data={'email': 'admin@test.com', 'password': 'AdminPass123!'})

    # Deactivate
    resp_toggle = client.post(f'/admin/students/{student_user}/toggle-status', follow_redirects=True)
    assert resp_toggle.status_code == 200
    assert b"deactivated" in resp_toggle.data

    with app.app_context():
        student = db.session.get(User, student_user)
        assert student.is_active is False

    # Reactivate
    resp_reactivate = client.post(f'/admin/students/{student_user}/toggle-status', follow_redirects=True)
    assert resp_reactivate.status_code == 200
    assert b"activated" in resp_reactivate.data

    with app.app_context():
        student = db.session.get(User, student_user)
        assert student.is_active is True

def test_admin_enrollment_reports(client, admin_user, sample_course):
    """Test admin enrollment reporting page."""
    client.post('/auth/login', data={'email': 'admin@test.com', 'password': 'AdminPass123!'})

    response = client.get('/admin/enrollments')
    assert response.status_code == 200
    assert b"Platform Enrollment Reports" in response.data
