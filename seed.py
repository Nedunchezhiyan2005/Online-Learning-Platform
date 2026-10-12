import os
from datetime import datetime, timedelta, timezone
from app import create_app
from extensions import db
from models import User, Course, Lesson, Enrollment, LessonProgress

def seed_database():
    app = create_app('development')
    with app.app_context():
        now = datetime.now(timezone.utc)
        # Drop and re-create all tables for a clean seed
        print("Recreating database tables...")
        db.drop_all()
        db.create_all()

        print("Seeding users...")
        # 1. Admin account
        admin_email = os.environ.get('ADMIN_EMAIL', 'admin@platform.edu')
        admin_pass = os.environ.get('ADMIN_PASSWORD', 'AdminSecure2026!')
        admin_name = os.environ.get('ADMIN_NAME', 'Chief Administrator')

        admin = User(
            full_name=admin_name,
            email=admin_email,
            role='admin',
            is_active=True
        )
        admin.set_password(admin_pass)
        db.session.add(admin)

        # 2. Sample Students
        students = [
            User(full_name='Alice Johnson', email='alice@student.edu', role='student', is_active=True),
            User(full_name='Bob Smith', email='bob@student.edu', role='student', is_active=True),
            User(full_name='Catherine Lee', email='catherine@student.edu', role='student', is_active=True),
            User(full_name='David Brown', email='david@student.edu', role='student', is_active=True),
            User(full_name='Emily Davis', email='emily@student.edu', role='student', is_active=False),  # Inactive account demonstration
        ]

        for s in students:
            s.set_password('Student123!')
            db.session.add(s)

        db.session.commit()

        print("Seeding courses and lessons from courses_data.py...")
        from courses_data import COURSES_DATA

        created_courses = []
        for cdata in COURSES_DATA:
            course = Course(
                title=cdata['title'],
                category=cdata['category'],
                instructor=cdata['instructor'],
                duration=cdata['duration'],
                description=cdata['description'],
                learning_objectives=cdata['learning_objectives'],
                is_published=cdata['is_published']
            )
            db.session.add(course)
            db.session.flush()

            for idx, ldata in enumerate(cdata['lessons'], start=1):
                lesson = Lesson(
                    course_id=course.id,
                    lesson_order=idx,
                    title=ldata['title'],
                    content=ldata['content'],
                    resource_url=ldata.get('resource_url')
                )
                db.session.add(lesson)

            created_courses.append(course)

        # 43. Add draft/unpublished course for admin demonstration
        c_draft = Course(
            title='Quantum Computing & Cryptographic Algorithms (Draft)',
            category='Software Engineering',
            instructor='Dr. David Deutsch',
            duration='6 Weeks',
            description='Curriculum under review by university academic board.',
            learning_objectives='- Quantum gates and qubits\n- Shor and Grover algorithms',
            is_published=False
        )
        db.session.add(c_draft)
        db.session.commit()

        print(f"Successfully seeded {len(created_courses) + 1} courses into database!")

        print("Seeding enrollments and lesson progress...")
        # Alice is enrolled in Course 0 (DevOps - in progress)
        c_devops = created_courses[0]
        c_devops_lessons = c_devops.lessons.order_by(Lesson.lesson_order.asc()).all()
        e1 = Enrollment(
            user_id=students[0].id, # Alice
            course_id=c_devops.id,
            enrolled_at=now - timedelta(days=14),
            status='in_progress'
        )
        db.session.add(e1)
        db.session.flush()

        # Alice completed first 3 lessons in Course 0
        for l in c_devops_lessons[:3]:
            db.session.add(LessonProgress(enrollment_id=e1.id, lesson_id=l.id, is_completed=True, completed_at=now - timedelta(days=5)))

        # Alice completed ALL lessons in Course 8 (Flask & SQLite) -> Has Certificate!
        c_flask = created_courses[8]
        c_flask_lessons = c_flask.lessons.order_by(Lesson.lesson_order.asc()).all()
        e2 = Enrollment(
            user_id=students[0].id, # Alice
            course_id=c_flask.id,
            enrolled_at=now - timedelta(days=20),
            status='completed'
        )
        db.session.add(e2)
        db.session.flush()

        for l in c_flask_lessons:
            db.session.add(LessonProgress(enrollment_id=e2.id, lesson_id=l.id, is_completed=True, completed_at=now - timedelta(days=2)))

        # Bob enrolled in Course 0 (DevOps) with 1 completed lesson
        e3 = Enrollment(
            user_id=students[1].id, # Bob
            course_id=c_devops.id,
            enrolled_at=now - timedelta(days=5),
            status='in_progress'
        )
        db.session.add(e3)
        db.session.flush()
        db.session.add(LessonProgress(enrollment_id=e3.id, lesson_id=c_devops_lessons[0].id, is_completed=True, completed_at=now - timedelta(days=3)))

        # Catherine enrolled in Course 16 (Cloud Security) with completed course -> Has Certificate!
        c_sec = created_courses[16]
        c_sec_lessons = c_sec.lessons.order_by(Lesson.lesson_order.asc()).all()
        e4 = Enrollment(
            user_id=students[2].id, # Catherine
            course_id=c_sec.id,
            enrolled_at=now - timedelta(days=10),
            status='completed'
        )
        db.session.add(e4)
        db.session.flush()
        for l in c_sec_lessons:
            db.session.add(LessonProgress(enrollment_id=e4.id, lesson_id=l.id, is_completed=True, completed_at=now - timedelta(days=1)))

        # David enrolled in Course 24 (Data Science & ML)
        c_ds = created_courses[24]
        e5 = Enrollment(
            user_id=students[3].id, # David
            course_id=c_ds.id,
            enrolled_at=now - timedelta(days=1),
            status='in_progress'
        )
        db.session.add(e5)

        db.session.commit()
        print("\nSeed completed successfully!")
        print(f"-> Admin login: {admin_email} / {admin_pass}")
        print("-> Student login: alice@student.edu / Student123!")
        print("-> Student login: bob@student.edu / Student123!")

if __name__ == '__main__':
    seed_database()
