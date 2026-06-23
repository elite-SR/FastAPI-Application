# 🚀 Deployment Guide

---

## 🖥️ VPS Setup Requirements

- Ubuntu Server
- Docker installed
- Docker Compose installed
- Nginx installed
- Git installed

---

## 📁 Project Location

/opt/fastapi-app

---

## 🚀 Deployment Process

### Step 1: Clone Repository
git clone https://github.com/elite-SR/FastAPI-Application.git

---

### Step 2: Build Containers
docker compose build

---

### Step 3: Start Services
docker compose up -d

---

### Step 4: Verify Services

Check running containers:
docker ps

---

### Step 5: Health Check
curl http://localhost/health

---

## 🔄 CI/CD Deployment Flow

1. Push code to GitHub
2. GitHub Actions triggers pipeline
3. Tests executed
4. SSH into VPS
5. Pull latest code
6. Restart Docker containers
7. Validate health check