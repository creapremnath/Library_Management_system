# Library_Management_system
Library Management System

How to run this application

git clone https://github.com/creapremnath/Library_Management_system.git

cd Library_Management_system


# Creating a virtual environment
python -m venv venv

# Activate the virtual environment
# For linux users:
source /venv/bin/activate

# For windows users:
activate

# For Windows Users Go back to the current working directory
cd ../../

pip install -r requirements.txt

# Run the Application

uvicorn --reload app.main:app



