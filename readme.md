## Description

Sample web application for the Python Community in Endava Bogota; It allows a person to showcase and manage his/her portfolio, work experience, technologies, etc.

## Repository

repository_url

## Setup

1. Project Setup
    1. Pipenv package manager
        - CD into the project's root directory
        - Run `pipenv install`
    2. Pip package manager
        - CD into the project's root directory
        - Run `pip install -r requirements.txt`
2. Database Setup
    - CD into the docker/ directory
    - Run `docker build -t <image_name> .`
    - Run `docker run -d -p 5432:5432 --name <container_name> <image_name>`

## Run the development server

After setting up the project and database:

- CD into the 'project' directory
- Activate the virtual environment (`pipenv shell` if you're using pipenv as package manager)
- Run `python [manage.py](http://manage.py) runserver localhost:9999`
- Navigate to `localhost:9999/resume/`