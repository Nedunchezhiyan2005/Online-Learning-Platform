from models import User

def test_landing_page(client):
    """Test public landing page loads properly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Centralized Online Learning Platform" in response.data or b"EduCentral" in response.data

def test_student_registration_success(client, app):
    """Test valid student registration."""
    response = client.post('/auth/register', data={
        'full_name': 'New Student',
        'email': 'newstudent@example.com',
        'password': 'Password123!',
        'confirm_password': 'Password123!'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Registration successful" in response.data

    with app.app_context():
        user = User.query.filter_by(email='newstudent@example.com').first()
        assert user is not None
        assert user.role == 'student'
        assert user.check_password('Password123!')

def test_registration_duplicate_email(client, student_user):
    """Test registering with an existing email fails."""
    response = client.post('/auth/register', data={
        'full_name': 'Duplicate Attempt',
        'email': 'student@test.com',
        'password': 'Password123!',
        'confirm_password': 'Password123!'
    })
    assert response.status_code == 200
    assert b"already registered" in response.data

def test_registration_password_mismatch(client):
    """Test registering with mismatched passwords fails."""
    response = client.post('/auth/register', data={
        'full_name': 'Mismatch User',
        'email': 'mismatch@example.com',
        'password': 'Password123!',
        'confirm_password': 'DifferentPassword!'
    })
    assert response.status_code == 200
    assert b"Passwords must match" in response.data

def test_student_login_success(client, student_user):
    """Test successful student login and dashboard redirect."""
    response = client.post('/auth/login', data={
        'email': 'student@test.com',
        'password': 'StudentPass123!'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Student Dashboard" in response.data
    assert b"Test Student" in response.data

def test_admin_login_success(client, admin_user):
    """Test successful admin login and admin console redirect."""
    response = client.post('/auth/login', data={
        'email': 'admin@test.com',
        'password': 'AdminPass123!'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Admin Console" in response.data or b"Admin Dashboard" in response.data

def test_login_invalid_password(client, student_user):
    """Test login with wrong password fails."""
    response = client.post('/auth/login', data={
        'email': 'student@test.com',
        'password': 'WrongPassword!'
    })
    assert response.status_code == 200
    assert b"Invalid email or password" in response.data

def test_login_deactivated_account(client, app):
    """Test that deactivated accounts cannot log in."""
    with app.app_context():
        deactivated = User(
            full_name="Deactivated User",
            email="deactivated@test.com",
            role="student",
            is_active=False
        )
        deactivated.set_password("DeactivatedPass123!")
        from extensions import db
        db.session.add(deactivated)
        db.session.commit()

    response = client.post('/auth/login', data={
        'email': 'deactivated@test.com',
        'password': 'DeactivatedPass123!'
    })
    assert response.status_code == 200
    assert b"account has been deactivated" in response.data

def test_logout(client, student_user):
    """Test user logout clears session."""
    client.post('/auth/login', data={
        'email': 'student@test.com',
        'password': 'StudentPass123!'
    })
    response = client.get('/auth/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b"signed out successfully" in response.data
