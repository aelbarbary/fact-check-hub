    #!/bin/bash

# Shell script to create a new Django project for fact-checking political facts

# Step 1: Define variables
PROJECT_NAME="political_factcheck"
APP_NAME="factcheck"
VENV_NAME="venv"

echo "Starting setup for Django project: $PROJECT_NAME"

# Step 2: Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv $VENV_NAME

# Step 3: Activate the virtual environment
source $VENV_NAME/bin/activate

# Step 4: Upgrade pip and install Django and Django REST Framework
echo "Upgrading pip and installing dependencies..."
pip install --upgrade pip
pip install django djangorestframework

# Step 5: Create the Django project
echo "Creating Django project..."
django-admin startproject $PROJECT_NAME .

# Step 6: Navigate into the project directory and create an app
echo "Creating Django app: $APP_NAME"
python3 manage.py startapp $APP_NAME

# Step 7: Update settings.py to include the new app and REST framework
echo "Updating settings.py..."
SETTINGS_FILE="$PROJECT_NAME/settings.py"

# Add the app and REST framework to INSTALLED_APPS
sed -i "/INSTALLED_APPS = \[/a\ \ \ \ '$APP_NAME',\n\ \ \ \ 'rest_framework'," $SETTINGS_FILE

# Step 8: Create a requirements.txt file
echo "Generating requirements.txt..."
pip freeze > requirements.txt

# Step 9: Apply initial migrations
echo "Applying initial migrations..."
python3 manage.py migrate

# Step 10: Notify user of completion
echo "Setup complete! Your Django project '$PROJECT_NAME' with the app '$APP_NAME' is ready."
echo "To start the server, run the following commands:"
echo "source $VENV_NAME/bin/activate"
echo "python3 manage.py runserver"
