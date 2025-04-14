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
