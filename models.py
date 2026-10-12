from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db

def utc_now():
    return datetime.now(timezone.utc)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='student')  # 'student' or 'admin'
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=utc_now, nullable=False)

    # Relationships
    enrollments = db.relationship('Enrollment', backref='user', cascade='all, delete-orphan', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return f"<User {self.email} ({self.role})>"


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructor = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(50), nullable=False)  # e.g., "8 Weeks", "15 Hours"
    learning_objectives = db.Column(db.Text, nullable=True)  # Markdown or newline separated list
    is_published = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=utc_now, nullable=False)

    # Relationships
    lessons = db.relationship('Lesson', backref='course', cascade='all, delete-orphan', order_by='Lesson.lesson_order', lazy='dynamic')
    enrollments = db.relationship('Enrollment', backref='course', cascade='all, delete-orphan', lazy='dynamic')

    def get_lesson_count(self):
        return self.lessons.count()

    def get_objectives_list(self):
        if not self.learning_objectives:
            return []
        lines = [line.strip().lstrip('-*• ') for line in self.learning_objectives.splitlines()]
        return [line for line in lines if line]

    def __repr__(self):
        return f"<Course {self.title}>"


class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    resource_url = db.Column(db.String(500), nullable=True)
    lesson_order = db.Column(db.Integer, default=1, nullable=False)
    created_at = db.Column(db.DateTime, default=utc_now, nullable=False)

    # Relationships
    progress_records = db.relationship('LessonProgress', backref='lesson', cascade='all, delete-orphan', lazy='dynamic')

    def __repr__(self):
        return f"<Lesson #{self.lesson_order}: {self.title}>"


class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    __table_args__ = (
        db.UniqueConstraint('user_id', 'course_id', name='uq_user_course_enrollment'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id', ondelete='CASCADE'), nullable=False)
    enrolled_at = db.Column(db.DateTime, default=utc_now, nullable=False)
    status = db.Column(db.String(20), default='in_progress', nullable=False)  # 'in_progress', 'completed'

    # Relationships
    lesson_progresses = db.relationship('LessonProgress', backref='enrollment', cascade='all, delete-orphan', lazy='dynamic')

    def calculate_progress(self):
        total_lessons = self.course.lessons.count()
        if total_lessons == 0:
            return 0, 0, 0  # completed_count, total_lessons, percentage
        completed_count = self.lesson_progresses.filter_by(is_completed=True).count()
        percent = int(round((completed_count / total_lessons) * 100))
        return completed_count, total_lessons, percent

    def is_lesson_completed(self, lesson_id):
        record = self.lesson_progresses.filter_by(lesson_id=lesson_id, is_completed=True).first()
        return record is not None

    def update_completion_status(self):
        completed, total, pct = self.calculate_progress()
        if total > 0 and completed == total:
            self.status = 'completed'
        else:
            self.status = 'in_progress'

    def __repr__(self):
        return f"<Enrollment User:{self.user_id} Course:{self.course_id} Status:{self.status}>"


class LessonProgress(db.Model):
    __tablename__ = 'lesson_progress'
    __table_args__ = (
        db.UniqueConstraint('enrollment_id', 'lesson_id', name='uq_enrollment_lesson_progress'),
    )

    id = db.Column(db.Integer, primary_key=True)
    enrollment_id = db.Column(db.Integer, db.ForeignKey('enrollments.id', ondelete='CASCADE'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id', ondelete='CASCADE'), nullable=False)
    is_completed = db.Column(db.Boolean, default=False, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<LessonProgress Enrollment:{self.enrollment_id} Lesson:{self.lesson_id} Completed:{self.is_completed}>"
