# 🚀 Production Deployment Manual

This guide describes how to deploy the FastAPI application stack onto a fresh Linux/Ubuntu Virtual Private Server (VPS). 

---

## 📋 Infrastructure & Server Requirements

Before executing the deployment, ensure your target host meets the following specifications:
* **Operating System:** Ubuntu 22.04 LTS (or any debian-based system).
* **Docker Engine:** Version 24.0.0 or higher.
* **Docker Compose:** Version 2.20.0 or higher (using the modern `docker compose` plugin syntax).
* **System Utilities:** `git`, `curl`, and `ufw` (Uncomplicated Firewall).

---

## 🛠️ Step-by-Step Server Setup

### Step 1: Clone the Application Repository
Log into your target VPS host via SSH and clone the repository. We recommend placing production services in the `/opt/` workspace directory:

```bash
# Navigate to the systems directory
cd /opt

# Clone the repository
git clone https://github.com/elite-SR/FastAPI-Application.git fastapi-app

# Enter the project directory
cd fastapi-app
```

---

### Step 2: Establish the Environment Configurations
Create a production `.env` file based on the provided template. Do not run the services using default/placeholder passwords:

```bash
# Duplicate the example config file
cp .env.example .env

# Open and customize environment secrets
nano .env
```

Ensure the database passwords inside `.env` are secure random strings.

---

### Step 3: Build the Container Images
Build the FastAPI application image. The multi-stage Docker build downloads runtime dependencies and caches them to ensure rapid deployment times on subsequent runs:

```bash
# Build the containers without using cached layers to ensure clean builds
docker compose build --no-cache
```

---

### Step 4: Launch the Microservices
Bring up the application stack in the background (detached mode). This starts NGINX, PostgreSQL, Redis, and FastAPI in their isolated bridge network:

```bash
# Start all services
docker compose up -d
```

---

### Step 5: Verify the Deployment
Verify that all containers are running successfully and check the container startup logs to ensure no runtime errors occurred:

```bash
# List all active containers and their uptime
docker compose ps

# Inspect logs from the application server
docker compose logs web --tail=50
```

---

## 📡 Deployment Validation & Health Verification

Once the containers are running, execute a health check command to verify that FastAPI can successfully connect to PostgreSQL and Redis:

```bash
# Ping the local health endpoint through NGINX
curl -i http://localhost/health
```

### Expected Healthy Response:
```json
HTTP/1.1 200 OK
Content-Type: application/json

{
  "status": "healthy",
  "database": "healthy",
  "redis": "healthy",
  "timestamp": 1718874635.421
}
```

---

## 🛠️ Deployment Troubleshooting Guide

If the system returns an unhealthy status, follow these steps to isolate the issue:

* **FastAPI is unreachable:**
  Ensure the container is running and check its logs:
  ```bash
  docker compose logs web
  ```
* **Database Connection Refused:**
  Verify that the PostgreSQL container is running and healthy:
  ```bash
  docker compose ps db
  ```
  Ensure the `DATABASE_URL` credentials in your `.env` file exactly match `POSTGRES_USER` and `POSTGRES_PASSWORD`.
* **Redis Connection Timeout:**
  Check if Redis is running and accepting connections:
  ```bash
  docker compose logs redis
  ```