# Employee Training Tracker

## Project Overview

A Django-based application to help HR and department heads manage employees, training programs, enrollments, and progress tracking.

## Setup Steps (Day 1)

1.  **Initialize Django Project:**
    ```bash
    # Assumes django is installed and in PATH, otherwise use python -m django
    django-admin startproject training_tracker .
    ```
2.  **Create Django App:**
    ```bash
    python manage.py startapp tracker
    ```
3.  **Define Models:** Added `Employee`, `TrainingProgram`, and `Enrollment` models in `tracker/models.py`.
4.  **Register App:** Added `'tracker'` to `INSTALLED_APPS` in `training_tracker/settings.py`.
5.  **Create Migrations:**
    ```bash
    python manage.py makemigrations tracker
    ```
6.  **Apply Migrations:**
    ```bash
    python manage.py migrate
    ```

## Features Implemented (Day 1)

*   Basic Django project and app structure.
*   Database models defined for:
    *   Employee (name, email, department, designation)
    *   TrainingProgram (title, description, start_date, end_date, trainer_name)
    *   Enrollment (employee, training_program, status)
*   Database schema created via migrations.

## Setup Steps (Day 2)

1.  **Register Models in Admin:** Registered `Employee`, `TrainingProgram`, and `Enrollment` in `tracker/admin.py`.
2.  **Create Superuser:**
    ```bash
    python manage.py createsuperuser
    ```
3.  **Seed Data:** Created a custom management command `tracker/management/commands/seed_data.py` and executed it:
    ```bash
    python manage.py seed_data
    ```

## Features Implemented (Day 2)

*   Django Admin interface configured for all models.
*   Superuser created for admin access.
*   Basic seed data added for Employees, Training Programs, and Enrollments.
