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

