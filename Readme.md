  Python Data Processing Application

Python Data Processing Application
==================================

This project is a Python-based application that processes data from a CSV file, performs computations, and prints results. The project includes unit tests to verify the application's functionality. It uses Docker, Docker Compose, Docker Swarm, Kubernetes, and GitHub Actions for CI/CD.

Tech Stack
----------

*   Python
*   Docker
*   Docker Compose
*   Docker Swarm
*   Kubernetes
*   GitHub Actions

Project Structure
-----------------

        .
        ├── app
        │   ├── \_\_init\_\_.py
        │   ├── main.py
        │   ├── utils.py
        ├── tests
        │   ├── \_\_init\_\_.py
        │   ├── test\_main.py
        ├── data
        │   ├── orders.csv
        ├── Dockerfile
        ├── docker-compose.yml
        ├── requirements.txt
        ├── README.md
    

Prerequisites
-------------

*   Docker: [Install Docker](https://docs.docker.com/get-docker/)
*   Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)
*   GitHub account with a repository

Installation
------------

1.  **Clone the repository**:

            `git clone https://github.com/saiaryansahoo/DevOps-End-To-End-Basics-Project.git                 cd DevOps-End-To-End-Basics-Project`
            
        

3.  **Build and run the Docker containers**:

            `docker-compose up --build`
        

Running the Application
-----------------------

To run the application, use the following command:

        `docker-compose up app`
    

Running the Tests
-----------------

To run the tests, use the following command:

        `docker-compose run test`
    

Docker and Docker Compose
-------------------------

The project uses a multi-stage Docker build and Docker Compose for orchestration. Below are the details:

### Dockerfile

        `# Use an official Python runtime as a parent image FROM python:3.8-slim  # Set the working directory in the container WORKDIR /app  # Copy the current directory contents into the container at /app COPY . /app  # Install any needed packages specified in requirements.txt RUN pip install --no-cache-dir -r requirements.txt  # Set the PYTHONPATH environment variable ENV PYTHONPATH=/app  # Run the application CMD ["python", "app/main.py"]`
        
    

### docker-compose.yml

        `version: '3.8'  services:   app:     build:       context: .     environment:       - PYTHONPATH=/app     command: python app/main.py     volumes:       - .:/app    test:     build:       context: .     environment:       - PYTHONPATH=/app     command: python tests/test_main.py     volumes:       - .:/app`
        
    

CI/CD with GitHub Actions
-------------------------

This project uses GitHub Actions for Continuous Integration and Continuous Deployment (CI/CD).

### GitHub Actions Workflow

Create a file `.github/workflows/main.yml` with the following content:

        `name: CI/CD Pipeline  on:   push:     branches:       - main   pull_request:     branches:       - main  jobs:   build:     runs-on: ubuntu-latest      steps:     - name: Checkout code       uses: actions/checkout@v2      - name: Set up Python       uses: actions/setup-python@v2       with:         python-version: 3.8      - name: Install dependencies       run: |         python -m pip install --upgrade pip         pip install -r requirements.txt      - name: Run tests       run: python tests/test_main.py      - name: Log in to Docker Hub       uses: docker/login-action@v2       with:         username: ${{ secrets.DOCKER_USERNAME }}         password: ${{ secrets.DOCKER_PASSWORD }}      - name: Build and push Docker image       run: |         docker build -t task-python:latest .         docker tag task-python:latest ${{ secrets.DOCKER_USERNAME }}/task-python:latest         docker push ${{ secrets.DOCKER_USERNAME }}/task-python:latest      - name: Deploy with Docker Compose       run: docker-compose up -d`
        
    

Secrets Configuration
---------------------

In your GitHub repository, add the following secrets:

*   `DOCKER_USERNAME`: Your Docker Hub username
*   `DOCKER_PASSWORD`: Your Docker Hub password

Conclusion
----------

This project demonstrates how to build, test, and deploy a Python application using Docker, Docker Compose, Docker Swarm, Kubernetes, and GitHub Actions for CI/CD. Follow the instructions above to set up and run the application locally and in a CI/CD pipeline.