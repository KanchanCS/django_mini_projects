# Social Blog Project

This is a social blog project built using Django and Python, where users can follow each other and see recent posts from users they follow.

## Prerequisites

Before running the project, make sure you have the following installed on your system:

- Python (version 3.x)
- Django (version 3.x)

## Getting Started

Follow these instructions to set up and run the project on your local machine:

1. Clone the repository:

```bash
git clone <repository_url>
cd social-blog-project
```

2. Create a virtual environment (optional but recommended):

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install the project dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the database:

```bash
python manage.py migrate
```

5. Create a superuser (admin) account:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Access the application:

Open your web browser and go to `http://localhost:8000/` to access the project.

## Project Structure

Briefly explain the directory structure of your project, highlighting key files and directories.

- `app_name/`: Contains the main Django app (you can change "app_name" to your actual app name).
- `templates/`: Contains HTML templates for the views.
- `static/`: Contains CSS, JavaScript, and other static files.
- `manage.py`: Django's command-line utility for managing the project.
- `requirements.txt`: List of project dependencies.

## Features

Explain the main features of your social blog project here, like:

- User registration and login.
- User profiles and follow functionality.
- Displaying recent posts from followed users.
