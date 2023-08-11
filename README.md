# Hacker News V2.0 developed using Django

## Overview
This is a Django project for that consume Hacker News API, to create its own clone of the Hacker News Platform. Its uses Celery to automate connections to the API endpoints and save the data to its database. Items created from the API can't be edited, but item created from our its model can be edited. 

This project provide a complete (CRUD) API endpoints, for others users to be able to use our platform. The API Documentation can be found in a file in this same directory called API_DOC.md and also under api-documentation below


## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/programmerizak/hacker_news_docker.git
   cd your-django-project
   ```

2. Build the Docker container:
   ```
   docker-compose build
   ```

3. Run makemigrations:
   ```
   docker-compose run --rm web python manage.py makemigrations
   ```


4. Run migrate:
   ```
   docker-compose run --rm web python manage.py migrate
   ```

5. Run create super user that will login to the website:
   ```
   docker-compose run --rm web python manage.py createsuperuser
   ```

6. Rebuild and Run your container:
   ```
   docker-compose up --build
   ```

## Configuration
1. Create a `.env` file in the project root and add your environment variables, such as 
`SECRET_KEY`,`ALLOWED_HOSTS`,`DB_NAME`,`DB_USERNAME`,`DB_PASSWORD`,
`DB_HOSTNAME`,`DB_PORT`,`DEBUG`,`DJANGO_SETTINGS_MODULE=website.settings.development`,`CELERY_BROKER_URL`,
`REDIS_BACKEND`,`NGINX_PORT`



## Usage
1. Run the development server:
   ```
   docker-compose up --build
   ```

2. Access the application at http://localhost:8000/

## API Documentation
API endpoints are documented using [drf-yasg](https://drf-yasg.readthedocs.io/).

1. Run the development server:
   ```
   python manage.py runserver
   ```

2. Access the API documentation at http://localhost:8000/api/docs/


## Contributing
We welcome contributions! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and commit them.

4. Push the changes to your fork.

5. Submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


(`Hacker News V2.0 developed using Django, and also provides API endpoints for the public to use`, `https://github.com/programmerizak/hacker_news_docker.git`, etc.)