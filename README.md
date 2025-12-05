# FastAPI Social Media API

A production-ready REST API built with FastAPI, PostgreSQL, SQLAlchemy, and JWT authentication.  
Includes automated testing, Dockerized deployment, and a full CI/CD pipeline using GitHub Actions.

---
## Live Deployment (AWS)

This API is deployed on **AWS EC2** using a Dockerized FastAPI application connected to an **AWS RDS PostgreSQL** database.

Public API:
http://16.16.68.130/docs

---
## Architecture Overview

FastAPI (Docker) → EC2 Instance  
FastAPI ↔ RDS PostgreSQL  
GitHub Actions → Docker Hub → EC2 (CI/CD auto-deploy)
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

---
## AWS Deployment Summary
On AWS EC2, the container exposes port **8000**, which is mapped to port **80** for public access.

The application is deployed on AWS using the following architecture:

- **AWS EC2** (Ubuntu) for hosting the FastAPI Docker container
- **AWS RDS PostgreSQL** for managed database
- **Docker Hub** to store built images
- **GitHub Actions CI/CD** to automatically:
  - Run tests
  - Build + push Docker image
  - SSH into EC2
  - Pull the latest image and restart the container

---

### Deployment Steps

1. Create an RDS PostgreSQL instance (free tier).  
2. Launch an EC2 Ubuntu instance and install Docker.  
3. Store environment variables in `.env` on EC2.  
4. Pull the Docker image from Docker Hub.  
5. Run the container exposing port 80 → 8000.  
6. Set up GitHub Actions to redeploy on every push to `main`.  

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
Note: The application runs on port **8005** in local development.

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
The FastAPI app inside the container listens on port **8000**, but we map it to **8005** on the host machine.

### Build the image locally

docker build -t fastapi .

### Run the container

docker run -p 8005:8000 fastapi
Port 8005 is exposed locally, while the FastAPI app inside the container runs on port 8000.

---

## CI/CD Pipeline (GitHub Actions → EC2)

On every push to the `main` branch:

1. Run all Pytest unit/integration tests  
2. Build a Docker image  
3. Push the image to Docker Hub  
4. SSH into the EC2 server  
5. Pull the new Docker image  
6. Stop the old container and run the updated one  

This creates a fully automated deployment pipeline.

---

## Credits

Based on the freeCodeCamp FastAPI course, extended with full CI/CD automation, Docker deployment and AWS deployment.

