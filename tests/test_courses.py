from models import Course

def test_course_listing(client, sample_course):
    """Test public course catalog lists published courses."""
    response = client.get('/courses/')
    assert response.status_code == 200
    assert b"Introduction to DevOps" in response.data
    assert b"Prof. Smith" in response.data

def test_course_search(client, sample_course):
    """Test searching courses by title query."""
    response = client.get('/courses/?q=DevOps')
    assert response.status_code == 200
    assert b"Introduction to DevOps" in response.data

    # Search with non-matching query
    response_empty = client.get('/courses/?q=NonExistentSkill')
    assert response_empty.status_code == 200
    assert b"No courses found" in response_empty.data

def test_course_filter_by_category(client, sample_course):
    """Test filtering courses by category."""
    response = client.get('/courses/?category=Cloud+%26+DevOps')
    assert response.status_code == 200
    assert b"Introduction to DevOps" in response.data

    response_other = client.get('/courses/?category=Cybersecurity')
    assert response_other.status_code == 200
    assert b"No courses found" in response_other.data

def test_course_details_page(client, sample_course):
    """Test course details page shows syllabus, instructor, objectives."""
    response = client.get(f'/courses/{sample_course}')
    assert response.status_code == 200
    assert b"Introduction to DevOps" in response.data
    assert b"Lesson 1: Git Essentials" in response.data
    assert b"Lesson 2: Docker Containers" in response.data

def test_course_details_not_found(client):
    """Test accessing a non-existent course returns 404."""
    response = client.get('/courses/9999')
    assert response.status_code == 404
    assert b"Resource Not Found" in response.data
