from models import Enrollment

def test_enrollment_requires_login(client, sample_course):
    """Test unauthenticated user cannot enroll and is redirected to login."""
    response = client.post(f'/student/enroll/{sample_course}')
    assert response.status_code == 302
    assert '/auth/login' in response.headers['Location']

def test_student_enrollment_success(client, student_user, sample_course, app):
    """Test authenticated student can enroll in a course."""
    # Login as student
    client.post('/auth/login', data={'email': 'student@test.com', 'password': 'StudentPass123!'})
    
    response = client.post(f'/student/enroll/{sample_course}', follow_redirects=True)
    assert response.status_code == 200
    assert b"Successfully enrolled" in response.data

    with app.app_context():
        enrollment = Enrollment.query.filter_by(user_id=student_user, course_id=sample_course).first()
        assert enrollment is not None
        assert enrollment.status == 'in_progress'

def test_duplicate_enrollment_prevention(client, student_user, sample_course):
    """Test student cannot enroll twice in the same course."""
    client.post('/auth/login', data={'email': 'student@test.com', 'password': 'StudentPass123!'})
    
    # First enrollment
    client.post(f'/student/enroll/{sample_course}')
    # Second attempt
    response = client.post(f'/student/enroll/{sample_course}', follow_redirects=True)
    assert response.status_code == 200
    assert b"already enrolled" in response.data

def test_my_learning_page(client, student_user, sample_course):
    """Test My Learning page displays enrolled courses."""
    client.post('/auth/login', data={'email': 'student@test.com', 'password': 'StudentPass123!'})
    client.post(f'/student/enroll/{sample_course}')

    response = client.get('/student/my-learning')
    assert response.status_code == 200
    assert b"Introduction to DevOps" in response.data
    assert b"Continue Learning" in response.data

def test_certificate_generation_and_download(client, student_user, sample_course, app):
    """Test certificate is generated and downloadable upon 100% course completion."""
    from models import Lesson, LessonProgress
    from extensions import db
    from datetime import datetime, timezone

    client.post('/auth/login', data={'email': 'student@test.com', 'password': 'StudentPass123!'})
    client.post(f'/student/enroll/{sample_course}')

    with app.app_context():
        enrollment = Enrollment.query.filter_by(user_id=student_user, course_id=sample_course).first()
        enrollment_id = enrollment.id
        lessons = Lesson.query.filter_by(course_id=sample_course).all()
        # Mark all lessons completed
        for l in lessons:
            db.session.add(LessonProgress(
                enrollment_id=enrollment_id,
                lesson_id=l.id,
                is_completed=True,
                completed_at=datetime.now(timezone.utc)
            ))
        enrollment.update_completion_status()
        db.session.commit()

    # View certificate web page
    resp_cert = client.get(f'/student/certificate/{enrollment_id}')
    assert resp_cert.status_code == 200
    assert b"Certificate of Completion" in resp_cert.data
    assert b"Test Student" in resp_cert.data
    assert b"Introduction to DevOps" in resp_cert.data
    assert b"Download Certificate HTML" in resp_cert.data

    # Download certificate attachment file
    resp_download = client.get(f'/student/certificate/{enrollment_id}/download')
    assert resp_download.status_code == 200
    assert resp_download.mimetype == "text/html"
    assert "attachment;filename=" in resp_download.headers.get("Content-Disposition", "")
    assert b"Certificate of Completion" in resp_download.data

def test_certificate_denied_when_incomplete(client, student_user, sample_course, app):
    """Test certificate cannot be generated or downloaded when course is incomplete."""
    client.post('/auth/login', data={'email': 'student@test.com', 'password': 'StudentPass123!'})
    client.post(f'/student/enroll/{sample_course}')

    with app.app_context():
        enrollment = Enrollment.query.filter_by(user_id=student_user, course_id=sample_course).first()
        enrollment_id = enrollment.id

    resp = client.get(f'/student/certificate/{enrollment_id}', follow_redirects=True)
    assert resp.status_code == 200
    assert b"must complete all lessons in this course to earn your certificate" in resp.data
