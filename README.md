# FastAPI Social Media API

A production-ready REST API built with FastAPI, PostgreSQL, SQLAlchemy, and JWT authentication.  
Includes automated testing, Dockerized deployment, and a full CI/CD pipeline using GitHub Actions.

---

## Features

- User authentication with JWT
- CRUD operations for posts
- Voting/like system
- PostgreSQL database with SQLAlchemy ORM
- Unit and integration testing with Pytest
- Dockerized application
- CI/CD pipeline with GitHub Actions
- Automatic Docker image build and push to Docker Hub

---

## Tech Stack

- **Backend:** FastAPI, Python 3.10  
- **Database:** PostgreSQL  
- **ORM:** SQLAlchemy  
- **Authentication:** JWT (OAuth2)  
- **Testing:** Pytest  
- **CI/CD:** GitHub Actions  
- **Containerization:** Docker  
- **Reverse Proxy / Server:** (add later if you deploy)

---

## Environment Variables

Create a `.env` file in the project root with the following:
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=postgres
DATABASE_NAME=fastapi
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

---

## Running Locally

### 1. Clone the repository
git clone https://github.com/junan318/fastapi.git

cd fastapi


### 2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows


### 3. Install dependencies

pip install -r requirements.txt


### 4. Start PostgreSQL and run the app

uvicorn app.main:app --reload


API will be available at:


http://127.0.0.1:8005


Swagger UI:


http://127.0.0.1:8005/docs

---

##  Running Tests

pytest

---

## Docker

### Build the image locally

docker build -t fastapi .

### Run the container

docker run -p 8000:8000 fastapi

---

## CI/CD Pipeline

This project uses **GitHub Actions** to:

- Run automated tests on every push and pull request
- Build and push Docker images to Docker Hub automatically after successful tests

---

## What I Learned

- Building REST APIs with FastAPI
- PostgreSQL and SQLAlchemy ORM
- JWT authentication and security
- Automated testing with Pytest
- CI/CD with GitHub Actions
- Docker containerization and image publishing

---

## Credits

Based on the freeCodeCamp FastAPI course, extended with full CI/CD automation and Docker deployment.

---

## Author

**Junan**  
GitHub: https://github.com/junan318  

