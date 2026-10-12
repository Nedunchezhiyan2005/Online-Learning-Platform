# Centralized Online Learning Platform

A full-stack web application designed for engineering education, continuous skill tracking, and DevOps automated testing pipelines. Built with **Python Flask**, **Flask-SQLAlchemy**, **SQLite**, **WTForms / CSRF Protection**, **Bootstrap 5**, and **Chart.js**.

---

## 1. Project Overview & Features

- **Public Landing Page:** Overview of learning curriculum, search courses, real-time counters, and featured courses.
- **Student Portal:**
  - Secure registration and session authentication.
  - Interactive course catalog with keyword search and category filtering.
  - Course enrollment with duplicate-enrollment prevention.
  - **My Learning** workspace with real-time completion tracking.
  - Sequential lesson viewer with reading material, external documentation references, and completion toggles.
  - Student profile management with name updates and secure password change.
- **Administrator Console:**
  - Live statistics calculated directly from SQLite database records (Students, Courses, Enrollments, Lessons).
  - Category distribution and enrollment completion status charts using **Chart.js**.
  - Complete Course CRUD (Create, Edit, Delete, Publish/Draft status).
  - Lesson curriculum builder (Add, Edit, Reorder, Delete lessons).
  - Student governance directory with account search and deactivation/reactivation toggling.
  - Comprehensive enrollment audit reports with course and status filters.
- **Enterprise Security & Architecture:**
  - Passwords hashed using Werkzeug (`scrypt`/`pbkdf2`).
  - Strict server-side Role-Based Access Control (`@student_required`, `@admin_required`).
  - Forms protected against Cross-Site Request Forgery (CSRF).
  - Modular Application Factory and Blueprint pattern (`auth`, `courses`, `student`, `admin`).
  - Prepared for Jenkins CI/CD, Pytest JUnit XML test exports, Docker, and Ansible automation.

---

## 2. Technology Stack

- **Backend:** Python 3.10+ / Flask 3.x
- **ORM & Database:** Flask-SQLAlchemy / SQLite
- **Security & Forms:** Flask-WTF, WTForms, Werkzeug, email-validator
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla ES6), Bootstrap 5.3, Bootstrap Icons, Chart.js
- **Testing:** Pytest, Pytest-Cov

---

## 3. Project Structure

```text
centralized-learning-platform/
├── app.py                     # Application factory and CLI entry points
├── config.py                  # Environment and database configuration
├── extensions.py              # SQLAlchemy and CSRFProtect instances
├── models.py                  # Database entities (User, Course, Lesson, Enrollment, LessonProgress)
├── forms.py                   # CSRF-protected WTForms
├── utils.py                   # Role-based access control decorators
├── requirements.txt           # Python package dependencies
├── seed.py                    # Database seeding script with demo courses and users
├── .env.example               # Template environment variables
├── .gitignore                 # Version control exclusions
├── README.md                  # Comprehensive documentation
├── routes/
│   ├── auth.py                # Login, registration, and logout
│   ├── courses.py             # Public catalog and course details
│   ├── student.py             # Student dashboard, my learning, lessons, and profile
│   └── admin.py               # Admin metrics, course/lesson CRUD, and student management
├── static/
│   ├── css/
│   │   └── style.css          # Blue-and-white theme, cards, progress bars, layout
│   └── js/
│       └── main.js            # Alerts dismissal, tooltips, confirmation dialogs
├── templates/
│   ├── base.html              # Core layout with top navbar, flash messages, and footer
│   ├── index.html             # Landing page with hero banner and featured courses
│   ├── auth/
│   │   ├── login.html         # Login form
│   │   └── register.html      # Student registration form
│   ├── student/
│   │   ├── dashboard.html     # Student metrics and active courses
│   │   ├── courses.html       # Searchable and filterable course catalog
│   │   ├── course_details.html# Syllabus, objectives, and enrollment button
│   │   ├── my_learning.html   # Enrolled courses with progress bars
│   │   ├── lesson.html        # Unit reader with previous/next and complete toggle
│   │   └── profile.html       # Profile name and password change
│   ├── admin/
│   │   ├── dashboard.html     # Admin dashboard with Chart.js analytics
│   │   ├── courses.html       # Course management directory
│   │   ├── course_form.html   # Course create/edit form
│   │   ├── lessons.html       # Lesson sequence and resource manager
│   │   ├── students.html      # Student directory and account toggling
│   │   └── enrollments.html   # Enrollment report tables and filters
│   └── errors/
│       ├── 404.html           # Resource not found error page
│       └── 500.html           # Internal server error page
└── tests/
    ├── conftest.py            # Isolated in-memory SQLite fixtures
    ├── test_auth.py           # Registration, login, and RBAC tests
    ├── test_courses.py        # Catalog search and filter tests
    ├── test_enrollments.py    # Enrollment and duplicate checks
    ├── test_progress.py       # Lesson access and progress calculations
    └── test_admin.py          # Admin CRUD, student toggling, and reports
```

---

## 4. Setup and Execution Instructions

### Step 1: Create and Activate a Python Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
*(On Windows Command Prompt / PowerShell, run `copy .env.example .env`)*

### Step 4: Initialize and Seed the Database
Populate the database with sample courses, lessons, students, and enrollment history:
```bash
python seed.py
```

Or initialize an empty database and create an admin interactively via Flask CLI:
```bash
flask init-db
flask create-admin
```

### Step 5: Start the Flask Development Server
```bash
python app.py
```
The server will start at: `http://127.0.0.1:5000`

> **Note for Docker / Remote Hosts:** To bind to all network interfaces, set `FLASK_RUN_HOST=0.0.0.0` or run:
> `python -c "from app import create_app; create_app().run(host='0.0.0.0', port=5000)"`

---

## 5. Development Credentials

The seed script (`seed.py`) provisions the following accounts:

| Role | Email | Password | Access Area |
| :--- | :--- | :--- | :--- |
| **Administrator** | `admin@platform.edu` | `AdminSecure2026!` | Admin Dashboard & Console (`/admin/dashboard`) |
| **Student** | `alice@student.edu` | `Student123!` | Student Portal & My Learning (`/student/dashboard`) |
| **Student** | `bob@student.edu` | `Student123!` | Student Portal (`/student/dashboard`) |
| **Student** | `emily@student.edu` | `Student123!` | *Deactivated Account Demo* |

---

## 6. Running Automated Tests & CI/CD Readiness

### Running Pytest Locally
Execute the test suite across all modules:
```bash
pytest -v
```

### Pytest with Code Coverage
```bash
pytest --cov=. --cov-report=term-missing
```

### Jenkins CI/CD JUnit XML Report Export
When running in automated Jenkins pipelines, export test results directly to XML:
```bash
pytest --junitxml=junit.xml
```
Jenkins can archive and publish test trends using the `junit 'junit.xml'` pipeline step.
