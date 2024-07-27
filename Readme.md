<div align="center">

# 📊 Python Data Processing Application 📊

This project is a Python-based application that processes data from a CSV file, performs computations, and prints results. The project includes unit tests to verify the application's functionality. It uses Docker, Docker Compose, Docker Swarm, Kubernetes, and GitHub Actions for CI/CD.

</div>

## 🌟 Features 🌟

### Data Processing
- 📈 Reads data from a CSV file.
- 📊 Computes monthly revenue, product revenue, and customer revenue.
- 🏆 Identifies top customers.

### Docker and Docker Compose
- 🐳 Multi-stage Docker build with an Ubuntu base image.
- 🛡️ Usage of distroless images for minimal attack surface.
- ⚙️ Docker Compose setup for multi-container environments.

### Docker Swarm
- 🐝 Deployment using Docker Swarm for scaling and orchestration.

### CI/CD with GitHub Actions
- 🤖 Automated testing pipeline triggered on each push and pull request.
- 🔍 Linting and unit tests executed in the pipeline.
- 📋 Results are displayed in the GitHub Actions interface.

## 💻 Tech Stack 💻
- **Programming Language**: Python 🐍
- **Libraries**: pandas 🐼
- **Containerization**: Docker, Docker Compose 🐳
- **Orchestration**: Docker Swarm (implemented) 🐝, Kubernetes (planned) ☸️
- **CI/CD**: GitHub Actions 🤖

## 📁 Project Structure 📁

    .
    ├── app
    │   ├── __init__.py
    │   ├── main.py
    │   ├── utils.py
    ├── tests
    │   ├── __init__.py
    │   ├── test_main.py
    ├── data
    │   ├── orders.csv
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    ├── README.md

## 🛠️ Prerequisites 🛠️

* Docker: [Install Docker](https://docs.docker.com/get-docker/)
* Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)
* GitHub account with a repository

## 📜 Instructions 📜

### Running the Application
1. Clone the repository:
    ```sh
    git clone https://github.com/saiaryansahoo/tanX.fi-Task-DevOps.git
    cd tanX.fi-Task-DevOps
    ```
2. Build and run the Docker container:
    ```sh
    docker-compose up --build
    ```

### Running the Tests
1. Ensure Docker is running.
2. Use Docker Compose to run the tests:
    ```sh
    docker-compose run test
    ```

### Getting the Output
1. The application and tests will output their results to the terminal.
2. For application output, you can check the logs:
    ```sh
    docker-compose logs app
    ```
3. For test output, you can check the logs:
    ```sh
    docker-compose logs test
    ```

### Using Docker Swarm
1. Initialize Docker Swarm:
    ```sh
    docker swarm init
    ```
2. Deploy the stack to Docker Swarm:
    ```sh
    docker stack deploy -c docker-compose.yml task-stack
    ```
3. To check the status of the services:
    ```sh
    docker stack services task-stack
    ```

### CI/CD Pipeline
- The CI/CD pipeline is configured in `.github/workflows/ci-cd.yml`.
- It includes steps for setting up Python, installing dependencies, and running tests.
- The pipeline is triggered on every push and pull request.

### Secrets Configuration
In your GitHub repository, add the following secrets:

- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password

## 🎯 Conclusion 🎯
This project demonstrates how to build, test, and deploy a Python application using Docker, Docker Compose, Docker Swarm, Kubernetes, and GitHub Actions for CI/CD. Follow the instructions above to set up and run the application locally and in a CI/CD pipeline.

## 📞 Contact Me 📞
If you have any questions or need further assistance, feel free to contact me:

- **Email**: [saiaryan.sahoo@gmail.com](mailto:saiaryan.sahoo@gmail.com)
- **GitHub**: [saiaryansahoo](https://github.com/saiaryansahoo)
