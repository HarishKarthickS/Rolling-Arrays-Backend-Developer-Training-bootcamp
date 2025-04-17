# Employee Training Tracker

## Project Overview

A Django-based application to help HR and department heads manage employees, training programs, enrollments, and progress tracking. This system allows organizations to maintain records of employees, the training programs offered, and track the progress of employees enrolled in these programs.

![Dashboard Screenshot](screenshots/dashboard.png)

## Features Implemented

* **Employee Management**
  * Create, view, and manage employee records
  * Track employee information including name, email, department, and designation

* **Training Program Management**
  * Create and manage training programs
  * Set program details including title, description, dates, and trainer

* **Enrollment Management**
  * Enroll employees in training programs
  * Track enrollment status (Enrolled, In Progress, Completed)
  * Filter enrollments by status and department

* **Dashboard and Analytics**
  * Overview of employees, programs, and enrollments
  * Visual representation of enrollment status distribution
  * Department distribution analytics
  * Recent enrollment activity

* **Admin Interface**
  * Full CRUD operations via Django admin panel
  * Batch operations for admin users

## Setup Steps

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser for admin access**
   ```bash
   python manage.py createsuperuser
   ```

6. **Load sample data (optional)**
   ```bash
   python manage.py seed_data
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   * Main application: http://127.0.0.1:8000/
   * Admin interface: http://127.0.0.1:8000/admin/

### Deployment to Render

1. **Create a Render account** at https://render.com/

2. **Create a new Web Service**
   * Connect to your GitHub repository
   * Use the following settings:
     * Build Command: `./build.sh`
     * Start Command: `gunicorn training_tracker.wsgi:application`

3. **Set environment variables**
   * `SECRET_KEY`: A secure random string for Django
   * `DEBUG`: Set to 'False' for production
   * `DATABASE_URL`: Your database connection string (Render PostgreSQL)

4. **Deploy the application**
   * Render will automatically deploy your application

## Day-by-Day Progress

### Day 1: Project Setup
* Initialized Django project and app
* Defined models for Employee, TrainingProgram, and Enrollment
* Created database schema via migrations

### Day 2: Admin & Migrations
* Configured Django admin interface for all models
* Created a superuser for admin access
* Added basic seed data using custom management command
* Set up database relationships and model validation

### Day 3: Views / API / Forms
* Implemented class-based views for listing and creating records
* Created templates for viewing and adding data
* Set up URL routing and navigation
* Added form validation and success messages

### Day 4: Filters & UI Enhancement
* Added filtering capability for enrollments by status and department
* Implemented form for adding new enrollments
* Enhanced UI with better styling (CSS variables, responsive design)
* Improved user experience with clearer navigation and visual feedback

### Day 5: Dashboard & Polish
* Created a dashboard with key statistics and visualizations
* Added dynamic charts for enrollment status and department distribution
* Improved overall code structure and organization
* Updated documentation and deployment configuration
* Added final polish to UI and user flows

## Project Structure

```
training_tracker/
├── manage.py           # Django management script
├── db.sqlite3          # SQLite database (development)
├── requirements.txt    # Project dependencies
├── build.sh            # Build script for deployment
├── render.yaml         # Render deployment configuration
├── README.md           # Project documentation
├── training_tracker/   # Main project settings
│   ├── __init__.py
│   ├── settings.py     # Project settings
│   ├── urls.py         # Main URL configuration
│   ├── asgi.py         # ASGI configuration
│   └── wsgi.py         # WSGI configuration
└── tracker/            # Main application
    ├── __init__.py
    ├── admin.py        # Admin configuration
    ├── apps.py         # App configuration
    ├── forms.py        # Form definitions
    ├── models.py       # Data models
    ├── urls.py         # App URL configuration
    ├── views.py        # View controllers
    ├── migrations/     # Database migrations
    ├── management/     # Custom management commands
    │   └── commands/
    │       └── seed_data.py
    ├── templatetags/   # Custom template filters
    │   ├── __init__.py
    │   └── custom_filters.py
    └── templates/      # HTML templates
        └── tracker/
            ├── base.html
            ├── dashboard.html
            ├── employee_list.html
            ├── employee_form.html
            ├── program_list.html
            ├── program_form.html
            ├── enrollment_list.html
            └── enrollment_form.html
```

## Technologies Used

* **Backend**: Django 5.1.6 (Python web framework)
* **Database**: SQLite (development), PostgreSQL (production)
* **Frontend**: HTML, CSS, Django Templates
* **Deployment**: Render (PaaS)
* **Version Control**: Git, GitHub

## Future Enhancements

* User authentication and role-based permissions
* Email notifications for enrollment status changes
* Training completion certificates
* Advanced reporting and analytics
* Calendar integration for training schedules
* Mobile-responsive UI improvements

## Live Demo

Access the live application at: [https://employee-training-tracker.onrender.com](https://employee-training-tracker.onrender.com)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
