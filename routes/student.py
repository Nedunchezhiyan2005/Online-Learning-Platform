from datetime import datetime, timezone
from flask import Blueprint, render_template, redirect, url_for, flash, request, session, abort
from extensions import db
from models import User, Course, Lesson, Enrollment, LessonProgress
from forms import ProfileUpdateForm, ChangePasswordForm
from utils import student_required

student_bp = Blueprint('student', __name__, url_prefix='/student')

@student_bp.route('/dashboard')
@student_required
def dashboard():
    user_id = session['user_id']
    user = User.query.get_or_404(user_id)

    enrollments = Enrollment.query.filter_by(user_id=user_id).order_by(Enrollment.enrolled_at.desc()).all()
    total_enrolled = len(enrollments)

    in_progress_count = 0
    completed_count = 0
    total_progress_sum = 0

    recent_enrollments_data = []

    for enr in enrollments:
        done, total, pct = enr.calculate_progress()
        if enr.status == 'completed' or (total > 0 and done == total):
            completed_count += 1
        else:
            in_progress_count += 1
        
        total_progress_sum += pct
        
        recent_enrollments_data.append({
            'enrollment': enr,
            'completed_lessons': done,
            'total_lessons': total,
            'progress_percent': pct
        })

    overall_progress = int(round(total_progress_sum / total_enrolled)) if total_enrolled > 0 else 0

    return render_template(
        'student/dashboard.html',
        user=user,
        total_enrolled=total_enrolled,
        in_progress_count=in_progress_count,
        completed_count=completed_count,
        overall_progress=overall_progress,
        recent_enrollments=recent_enrollments_data[:5]
    )


@student_bp.route('/my-learning')
@student_required
def my_learning():
    user_id = session['user_id']
    enrollments = Enrollment.query.filter_by(user_id=user_id).order_by(Enrollment.enrolled_at.desc()).all()

    learning_data = []
    for enr in enrollments:
        done, total, pct = enr.calculate_progress()
        # Find next uncompleted lesson if any
        next_lesson = None
        for lesson in enr.course.lessons.order_by(Lesson.lesson_order.asc()):
            if not enr.is_lesson_completed(lesson.id):
                next_lesson = lesson
                break
        if not next_lesson and total > 0:
            next_lesson = enr.course.lessons.order_by(Lesson.lesson_order.asc()).first()

        learning_data.append({
            'enrollment': enr,
            'course': enr.course,
            'completed_lessons': done,
            'total_lessons': total,
            'progress_percent': pct,
            'next_lesson_id': next_lesson.id if next_lesson else None
        })

    return render_template('student/my_learning.html', learning_data=learning_data)


@student_bp.route('/certificate/<int:enrollment_id>')
@student_required
def view_certificate(enrollment_id):
    user_id = session['user_id']
    enrollment = Enrollment.query.filter_by(id=enrollment_id, user_id=user_id).first_or_404()
    
    done, total, pct = enrollment.calculate_progress()
    if pct < 100 or total == 0:
        flash('You must complete all lessons in this course to earn your certificate of completion.', 'warning')
        return redirect(url_for('student.my_learning'))
        
    user = User.query.get_or_404(user_id)
    course = enrollment.course
    
    # Get last completed lesson date or enrollment date
    last_progress = enrollment.lesson_progresses.filter_by(is_completed=True).order_by(LessonProgress.completed_at.desc()).first()
    completion_date = last_progress.completed_at if (last_progress and last_progress.completed_at) else enrollment.enrolled_at

    return render_template(
        'student/certificate.html',
        enrollment=enrollment,
        user=user,
        course=course,
        total_lessons=total,
        completion_date=completion_date
    )


@student_bp.route('/certificate/<int:enrollment_id>/download')
@student_required
def download_certificate(enrollment_id):
    from flask import Response
    user_id = session['user_id']
    enrollment = Enrollment.query.filter_by(id=enrollment_id, user_id=user_id).first_or_404()
    
    done, total, pct = enrollment.calculate_progress()
    if pct < 100 or total == 0:
        flash('You must complete all lessons to download the certificate.', 'warning')
        return redirect(url_for('student.my_learning'))
        
    user = User.query.get_or_404(user_id)
    course = enrollment.course
    last_progress = enrollment.lesson_progresses.filter_by(is_completed=True).order_by(LessonProgress.completed_at.desc()).first()
    completion_date = last_progress.completed_at if (last_progress and last_progress.completed_at) else enrollment.enrolled_at

    rendered_html = render_template(
        'student/certificate.html',
        enrollment=enrollment,
        user=user,
        course=course,
        total_lessons=total,
        completion_date=completion_date
    )

    safe_title = "".join(c for c in course.title if c.isalnum() or c in (' ', '_', '-')).rstrip().replace(' ', '_')
    filename = f"Certificate_{safe_title}_{user.full_name.replace(' ', '_')}.html"

    return Response(
        rendered_html,
        mimetype="text/html",
        headers={"Content-Disposition": f"attachment;filename={filename}"}
    )


@student_bp.route('/enroll/<int:course_id>', methods=['POST'])
@student_required
def enroll(course_id):
    user_id = session['user_id']
    course = Course.query.get_or_404(course_id)

    if not course.is_published:
        flash('This course is currently not accepting enrollments.', 'warning')
        return redirect(url_for('courses.list_courses'))

    # Check duplicate enrollment
    existing = Enrollment.query.filter_by(user_id=user_id, course_id=course_id).first()
    if existing:
        flash('You are already enrolled in this course!', 'info')
        return redirect(url_for('student.my_learning'))

    new_enrollment = Enrollment(
        user_id=user_id,
        course_id=course_id,
        status='in_progress'
    )
    db.session.add(new_enrollment)
    db.session.commit()

    flash(f'Successfully enrolled in "{course.title}"! Start learning now.', 'success')
    return redirect(url_for('student.my_learning'))


@student_bp.route('/course/<int:course_id>/lesson/<int:lesson_id>')
@student_required
def view_lesson(course_id, lesson_id):
    user_id = session['user_id']
    enrollment = Enrollment.query.filter_by(user_id=user_id, course_id=course_id).first()
    
    if not enrollment:
        flash('You must enroll in this course before accessing its lessons.', 'warning')
        return redirect(url_for('courses.course_details', course_id=course_id))

    course = Course.query.get_or_404(course_id)
    lesson = Lesson.query.filter_by(id=lesson_id, course_id=course_id).first_or_404()
    
    # Get all lessons for navigation sidebar
    all_lessons = course.lessons.order_by(Lesson.lesson_order.asc()).all()

    # Track completion map
    completed_ids = {
        lp.lesson_id for lp in enrollment.lesson_progresses.filter_by(is_completed=True).all()
    }

    # Find previous and next lessons
    prev_lesson = None
    next_lesson = None
    for idx, l in enumerate(all_lessons):
        if l.id == lesson.id:
            if idx > 0:
                prev_lesson = all_lessons[idx - 1]
            if idx < len(all_lessons) - 1:
                next_lesson = all_lessons[idx + 1]
            break

    is_completed = lesson.id in completed_ids
    done_count, total_count, pct = enrollment.calculate_progress()

    return render_template(
        'student/lesson.html',
        course=course,
        lesson=lesson,
        enrollment=enrollment,
        all_lessons=all_lessons,
        completed_ids=completed_ids,
        is_completed=is_completed,
        prev_lesson=prev_lesson,
        next_lesson=next_lesson,
        progress_percent=pct,
        done_count=done_count,
        total_count=total_count
    )


@student_bp.route('/course/<int:course_id>/lesson/<int:lesson_id>/toggle-progress', methods=['POST'])
@student_required
def toggle_progress(course_id, lesson_id):
    user_id = session['user_id']
    enrollment = Enrollment.query.filter_by(user_id=user_id, course_id=course_id).first_or_404()
    lesson = Lesson.query.filter_by(id=lesson_id, course_id=course_id).first_or_404()

    progress = LessonProgress.query.filter_by(enrollment_id=enrollment.id, lesson_id=lesson.id).first()

    if not progress:
        progress = LessonProgress(
            enrollment_id=enrollment.id,
            lesson_id=lesson.id,
            is_completed=True,
            completed_at=datetime.now(timezone.utc)
        )
        db.session.add(progress)
        flash(f'Lesson "{lesson.title}" marked as completed!', 'success')
    else:
        # Toggle status
        progress.is_completed = not progress.is_completed
        progress.completed_at = datetime.now(timezone.utc) if progress.is_completed else None
        if progress.is_completed:
            flash(f'Lesson "{lesson.title}" marked as completed!', 'success')
        else:
            flash(f'Lesson "{lesson.title}" marked as incomplete.', 'info')

    # Update enrollment status
    enrollment.update_completion_status()
    db.session.commit()

    return redirect(url_for('student.view_lesson', course_id=course_id, lesson_id=lesson_id))


@student_bp.route('/profile', methods=['GET', 'POST'])
@student_required
def profile():
    user_id = session['user_id']
    user = User.query.get_or_404(user_id)

    profile_form = ProfileUpdateForm(prefix='profile')
    password_form = ChangePasswordForm(prefix='password')

    if request.method == 'GET':
        profile_form.full_name.data = user.full_name

    # Check which form was submitted
    if 'profile-submit' in request.form and profile_form.validate_on_submit():
        user.full_name = profile_form.full_name.data.strip()
        db.session.commit()
        session['user_name'] = user.full_name
        flash('Profile name updated successfully.', 'success')
        return redirect(url_for('student.profile'))

    if 'password-submit' in request.form and password_form.validate_on_submit():
        if not user.check_password(password_form.current_password.data):
            flash('Current password entered is incorrect.', 'danger')
        else:
            user.set_password(password_form.new_password.data)
            db.session.commit()
            flash('Password changed successfully!', 'success')
            return redirect(url_for('student.profile'))

    return render_template(
        'student/profile.html',
        user=user,
        profile_form=profile_form,
        password_form=password_form
    )
