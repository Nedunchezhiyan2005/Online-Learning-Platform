from models import Course, Lesson, Enrollment, LessonProgress

def test_lesson_access_requires_enrollment(client, student_user, sample_course, app):
    """Test unenrolled student cannot access course lessons."""
    client.post('/auth/login', data={'email': 'student@test.com', 'password': 'StudentPass123!'})
    
    with app.app_context():
        lesson = Lesson.query.filter_by(course_id=sample_course).first()
        lesson_id = lesson.id

    response = client.get(f'/student/course/{sample_course}/lesson/{lesson_id}', follow_redirects=True)
    assert response.status_code == 200
    assert b"must enroll in this course before accessing" in response.data

def test_lesson_access_and_progress_toggle(client, student_user, sample_course, app):
    """Test enrolled student can read lesson and mark it completed."""
    client.post('/auth/login', data={'email': 'student@test.com', 'password': 'StudentPass123!'})
    client.post(f'/student/enroll/{sample_course}')

    with app.app_context():
        lessons = Lesson.query.filter_by(course_id=sample_course).order_by(Lesson.lesson_order.asc()).all()
        l1, l2 = lessons[0], lessons[1]
        l1_id, l2_id = l1.id, l2.id

    # View lesson 1
    resp = client.get(f'/student/course/{sample_course}/lesson/{l1_id}')
    assert resp.status_code == 200
    assert b"Lesson 1: Git Essentials" in resp.data

    # Mark lesson 1 completed
    resp_toggle = client.post(f'/student/course/{sample_course}/lesson/{l1_id}/toggle-progress', follow_redirects=True)
    assert resp_toggle.status_code == 200
    assert b"marked as completed" in resp_toggle.data

    with app.app_context():
        enrollment = Enrollment.query.filter_by(user_id=student_user, course_id=sample_course).first()
        done, total, pct = enrollment.calculate_progress()
        assert done == 1
        assert total == 2
        assert pct == 50
        assert enrollment.status == 'in_progress'

    # Mark lesson 2 completed (completing entire course)
    client.post(f'/student/course/{sample_course}/lesson/{l2_id}/toggle-progress')

    with app.app_context():
        enrollment = Enrollment.query.filter_by(user_id=student_user, course_id=sample_course).first()
        done, total, pct = enrollment.calculate_progress()
        assert done == 2
        assert total == 2
        assert pct == 100
        assert enrollment.status == 'completed'
