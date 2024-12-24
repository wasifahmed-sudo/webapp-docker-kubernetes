# Flask Application with Docker, Kubernetes, and Ingress

This project demonstrates the containerization and deployment of a Flask application using Docker and Kubernetes. The application interacts with a MySQL database to store and retrieve data.

## Table of Contents

- [Application Overview](#application-overview)
- [Prerequisites](#prerequisites)
- [Setup and Deployment](#setup-and-deployment)
  - [Using Docker Compose](#using-docker-compose)
  - [Using Kubernetes](#using-kubernetes)
- [Reasoning Behind the Approach](#reasoning-behind-the-approach)
  - [Configuring the Web Application to Communicate with the Database in K8s](#configuring-the-web-application-to-communicate-with-the-database-in-k8s)
  - [Exposing the Web Application to the Outside World in K8s](#exposing-the-web-application-to-the-outside-world-in-k8s)
  - [Configuring Auto-Scaling for the Application](#configuring-auto-scaling-for-the-application)
- [Next Steps](#next-steps)

## Application Overview

The Flask application provides a simple web interface to add and view data stored in a MySQL database. The application exposes the following endpoints:

- `/add_data`: Endpoint to handle form submissions.
- `/view_data`: Endpoint to view all data stored in the database.

## Prerequisites

1. **Docker**: Install Docker on your local machine.
2. **Kubernetes**: Install a local Kubernetes cluster (e.g., Minikube, Docker Desktop with Kubernetes enabled).
3. **kubectl**: Install `kubectl` to interact with your Kubernetes cluster.
4. **Docker Compose**: Install Docker Compose for local deployment.
5. **Git**: Install Git to clone the repository and manage version control.

## Setup and Deployment

### Using Docker Compose

1. **Clone the Repository**:

```bash
git clone git@github.com:wasifahmed-sudo/webapp-docker-kubernetes.git

cd git@github.com:wasifahmed-sudo/webapp-docker-kubernetes.git
```



2. **Build and Run the Application:**
```bash
docker-compose up --build
```
3. **Access the Application:**
```bash
http://localhost:35622/add_data
```
### Using Kubernetes
1.  ****Start Your Kubernetes Cluster**:**
```bash
kubectl config use-context docker-desktop
```

2. **Deploy the Application:**
```bash
kubectl apply -f k8s/
```
3. **Access the Application:**
```bash
http://localhost:35622/add_data
```
## Reasoning Behind the Approach

### Configuring the Web Application to Communicate with the Database in K8s

-   **Environment Variables**: The Flask application uses environment variables to connect to the MySQL database. These variables are defined in the Kubernetes Deployment manifest.
-   **Kubernetes Secrets**: Sensitive information like database credentials is stored in Kubernetes Secrets and injected into the application pods.

### Exposing the Web Application to the Outside World in K8s

-   **Ingress**: The application is exposed to the outside world using an Ingress resource. The Ingress routes traffic from `http://localhost:35622/add_data` to the Flask application.
-   **NGINX Ingress Controller**: The NGINX Ingress Controller is used to handle traffic routing.

### Configuring Auto-Scaling for the Application

-   **Horizontal Pod Autoscaler (HPA)**: The HPA is configured to scale the Flask application based on CPU utilization. It ensures that the application can handle increased traffic by automatically scaling the number of pods.

## Next Steps

1.  **Enable SSL**: Configure SSL for secure communication using Let’s Encrypt.
2.  **Monitor the Application**: Use monitoring tools like Prometheus and Grafana to monitor the application and Kubernetes cluster.

