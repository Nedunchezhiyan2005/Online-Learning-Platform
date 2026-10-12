from flask import Blueprint, render_template, request, session
from models import Course, Enrollment

courses_bp = Blueprint('courses', __name__, url_prefix='/courses')

@courses_bp.route('/')
def list_courses():
    query_text = request.args.get('q', '').strip()
    category = request.args.get('category', '').strip()

    query = Course.query.filter_by(is_published=True)

    if query_text:
        search_filter = f"%{query_text}%"
        query = query.filter(
            (Course.title.ilike(search_filter)) | 
            (Course.instructor.ilike(search_filter)) |
            (Course.description.ilike(search_filter))
        )

    if category:
        query = query.filter_by(category=category)

    courses = query.order_by(Course.created_at.desc()).all()

    # Get distinct categories for the filter dropdown
    categories = [cat[0] for cat in Course.query.with_entities(Course.category).distinct().all()]

    # If student is logged in, find enrolled course IDs to show enrollment state
    enrolled_course_ids = []
    if 'user_id' in session and session.get('user_role') == 'student':
        enrollments = Enrollment.query.filter_by(user_id=session['user_id']).all()
        enrolled_course_ids = [e.course_id for e in enrollments]

    return render_template(
        'student/courses.html',
        courses=courses,
        categories=categories,
        selected_category=category,
        query_text=query_text,
        enrolled_course_ids=enrolled_course_ids
    )


@courses_bp.route('/<int:course_id>')
def course_details(course_id):
    course = Course.query.get_or_404(course_id)
    
    # Check if logged in student is enrolled
    is_enrolled = False
    enrollment = None
    if 'user_id' in session and session.get('user_role') == 'student':
        enrollment = Enrollment.query.filter_by(user_id=session['user_id'], course_id=course.id).first()
        if enrollment:
            is_enrolled = True

    lessons = course.lessons.order_by(Course.lessons.property.mapper.class_.lesson_order.asc()).all()

    return render_template(
        'student/course_details.html',
        course=course,
        lessons=lessons,
        is_enrolled=is_enrolled,
        enrollment=enrollment
    )
