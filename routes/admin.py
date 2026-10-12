from flask import Blueprint, render_template, redirect, url_for, flash, request, session, abort
from sqlalchemy import func
from extensions import db
from models import User, Course, Lesson, Enrollment, LessonProgress
from forms import CourseForm, LessonForm
from utils import admin_required

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
@admin_required
def dashboard():
    total_students = User.query.filter_by(role='student').count()
    total_courses = Course.query.count()
    total_enrollments = Enrollment.query.count()
    total_lessons = Lesson.query.count()

    recent_students = User.query.filter_by(role='student').order_by(User.created_at.desc()).limit(5).all()

    # Most popular courses (count of enrollments per course)
    popular_courses_query = db.session.query(
        Course, func.count(Enrollment.id).label('enrollment_count')
    ).outerjoin(Enrollment, Course.id == Enrollment.course_id)\
     .group_by(Course.id)\
     .order_by(func.count(Enrollment.id).desc())\
     .limit(5).all()

    # Category distribution for charts
    category_counts = db.session.query(
        Course.category, func.count(Course.id)
    ).group_by(Course.category).all()
    categories_labels = [c[0] for c in category_counts]
    categories_data = [c[1] for c in category_counts]

    # Enrollment status distribution
    status_counts = db.session.query(
        Enrollment.status, func.count(Enrollment.id)
    ).group_by(Enrollment.status).all()
    status_labels = [s[0].replace('_', ' ').title() for s in status_counts]
    status_data = [s[1] for s in status_counts]

    return render_template(
        'admin/dashboard.html',
        total_students=total_students,
        total_courses=total_courses,
        total_enrollments=total_enrollments,
        total_lessons=total_lessons,
        recent_students=recent_students,
        popular_courses=popular_courses_query,
        categories_labels=categories_labels,
        categories_data=categories_data,
        status_labels=status_labels,
        status_data=status_data
    )


# --- COURSE MANAGEMENT ---

@admin_bp.route('/courses')
@admin_required
def list_courses():
    query_text = request.args.get('q', '').strip()
    category = request.args.get('category', '').strip()

    query = Course.query
    if query_text:
        search_filter = f"%{query_text}%"
        query = query.filter(
            (Course.title.ilike(search_filter)) | 
            (Course.instructor.ilike(search_filter))
        )
    if category:
        query = query.filter_by(category=category)

    courses = query.order_by(Course.created_at.desc()).all()
    categories = [cat[0] for cat in Course.query.with_entities(Course.category).distinct().all()]

    return render_template(
        'admin/courses.html',
        courses=courses,
        categories=categories,
        selected_category=category,
        query_text=query_text
    )


@admin_bp.route('/courses/new', methods=['GET', 'POST'])
@admin_required
def create_course():
    form = CourseForm()
    if form.validate_on_submit():
        course = Course(
            title=form.title.data.strip(),
            category=form.category.data,
            instructor=form.instructor.data.strip(),
            duration=form.duration.data.strip(),
            description=form.description.data.strip(),
            learning_objectives=form.learning_objectives.data.strip() if form.learning_objectives.data else None,
            is_published=form.is_published.data
        )
        db.session.add(course)
        db.session.commit()
        flash(f'Course "{course.title}" was created successfully!', 'success')
        return redirect(url_for('admin.manage_lessons', course_id=course.id))

    return render_template('admin/course_form.html', form=form, title="Create New Course", course=None)


@admin_bp.route('/courses/<int:course_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    form = CourseForm(obj=course)

    if form.validate_on_submit():
        course.title = form.title.data.strip()
        course.category = form.category.data
        course.instructor = form.instructor.data.strip()
        course.duration = form.duration.data.strip()
        course.description = form.description.data.strip()
        course.learning_objectives = form.learning_objectives.data.strip() if form.learning_objectives.data else None
        course.is_published = form.is_published.data
        db.session.commit()

        flash(f'Course "{course.title}" updated successfully.', 'success')
        return redirect(url_for('admin.list_courses'))

    return render_template('admin/course_form.html', form=form, title=f"Edit Course: {course.title}", course=course)


@admin_bp.route('/courses/<int:course_id>/delete', methods=['POST'])
@admin_required
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    title = course.title
    db.session.delete(course)
    db.session.commit()
    flash(f'Course "{title}" and all related lessons and enrollments were deleted.', 'info')
    return redirect(url_for('admin.list_courses'))


# --- LESSON MANAGEMENT ---

@admin_bp.route('/courses/<int:course_id>/lessons', methods=['GET', 'POST'])
@admin_required
def manage_lessons(course_id):
    course = Course.query.get_or_404(course_id)
    form = LessonForm()

    if form.validate_on_submit():
        lesson = Lesson(
            course_id=course.id,
            title=form.title.data.strip(),
            lesson_order=form.lesson_order.data,
            content=form.content.data.strip(),
            resource_url=form.resource_url.data.strip() if form.resource_url.data else None
        )
        db.session.add(lesson)
        db.session.commit()
        flash(f'Lesson "{lesson.title}" added to course!', 'success')
        return redirect(url_for('admin.manage_lessons', course_id=course.id))

    # Pre-populate next lesson order
    next_order = (db.session.query(func.max(Lesson.lesson_order)).filter_by(course_id=course.id).scalar() or 0) + 1
    if request.method == 'GET':
        form.lesson_order.data = next_order

    lessons = course.lessons.order_by(Lesson.lesson_order.asc()).all()
    return render_template('admin/lessons.html', course=course, lessons=lessons, form=form, editing_lesson=None)


@admin_bp.route('/courses/<int:course_id>/lessons/<int:lesson_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_lesson(course_id, lesson_id):
    course = Course.query.get_or_404(course_id)
    lesson = Lesson.query.filter_by(id=lesson_id, course_id=course.id).first_or_404()
    form = LessonForm(obj=lesson)

    if form.validate_on_submit():
        lesson.title = form.title.data.strip()
        lesson.lesson_order = form.lesson_order.data
        lesson.content = form.content.data.strip()
        lesson.resource_url = form.resource_url.data.strip() if form.resource_url.data else None
        db.session.commit()
        flash(f'Lesson "{lesson.title}" updated successfully!', 'success')
        return redirect(url_for('admin.manage_lessons', course_id=course.id))

    lessons = course.lessons.order_by(Lesson.lesson_order.asc()).all()
    return render_template('admin/lessons.html', course=course, lessons=lessons, form=form, editing_lesson=lesson)


@admin_bp.route('/courses/<int:course_id>/lessons/<int:lesson_id>/delete', methods=['POST'])
@admin_required
def delete_lesson(course_id, lesson_id):
    course = Course.query.get_or_404(course_id)
    lesson = Lesson.query.filter_by(id=lesson_id, course_id=course.id).first_or_404()
    title = lesson.title
    db.session.delete(lesson)
    db.session.commit()
    flash(f'Lesson "{title}" deleted successfully.', 'info')
    return redirect(url_for('admin.manage_lessons', course_id=course.id))


# --- STUDENT MANAGEMENT ---

@admin_bp.route('/students')
@admin_required
def list_students():
    query_text = request.args.get('q', '').strip()
    status_filter = request.args.get('status', '').strip()

    query = User.query.filter_by(role='student')
    if query_text:
        search_filter = f"%{query_text}%"
        query = query.filter(
            (User.full_name.ilike(search_filter)) | 
            (User.email.ilike(search_filter))
        )
    if status_filter == 'active':
        query = query.filter_by(is_active=True)
    elif status_filter == 'inactive':
        query = query.filter_by(is_active=False)

    students = query.order_by(User.created_at.desc()).all()
    return render_template('admin/students.html', students=students, query_text=query_text, status_filter=status_filter)


@admin_bp.route('/students/<int:student_id>/toggle-status', methods=['POST'])
@admin_required
def toggle_student_status(student_id):
    student = User.query.filter_by(id=student_id, role='student').first_or_404()
    student.is_active = not student.is_active
    db.session.commit()
    state = "activated" if student.is_active else "deactivated"
    flash(f'Student "{student.full_name}" has been {state}.', 'info')
    return redirect(url_for('admin.list_students'))


# --- ENROLLMENT REPORTS ---

@admin_bp.route('/enrollments')
@admin_required
def list_enrollments():
    status_filter = request.args.get('status', '').strip()
    course_id = request.args.get('course_id', type=int)

    query = Enrollment.query
    if status_filter:
        query = query.filter_by(status=status_filter)
    if course_id:
        query = query.filter_by(course_id=course_id)

    enrollments = query.order_by(Enrollment.enrolled_at.desc()).all()
    courses = Course.query.order_by(Course.title.asc()).all()

    report_data = []
    for enr in enrollments:
        done, total, pct = enr.calculate_progress()
        report_data.append({
            'enrollment': enr,
            'student_name': enr.user.full_name,
            'student_email': enr.user.email,
            'course_title': enr.course.title,
            'enrolled_at': enr.enrolled_at,
            'completed_lessons': done,
            'total_lessons': total,
            'progress_percent': pct,
            'status': enr.status
        })

    return render_template(
        'admin/enrollments.html',
        enrollment_reports=report_data,
        courses=courses,
        selected_status=status_filter,
        selected_course_id=course_id
    )
