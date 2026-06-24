# 🚀 FastAPI Production Deployment Project

> [!NOTE]  
> **Deployment Status Notice:**  
> This project is currently not deployed on an active VPS. Consequently, the GitHub Actions deployment workflow stage (`deploy`) will show as failed until valid SSH secrets (`VPS_HOST`, `VPS_SSH_KEY`, etc.) are configured in the repository's Settings. The pipeline's automated tests (`test`) execute and complete successfully in the runner environment.

This project demonstrates a complete production-grade backend deployment using FastAPI, Docker, Nginx, PostgreSQL, Redis, and GitHub Actions CI/CD pipeline.

---

## 📌 Project Overview

This system is designed to simulate real-world production infrastructure with:

- Backend API (FastAPI)
- Database (PostgreSQL)
- Cache layer (Redis)
- Reverse proxy (NGINX)
- Containerization (Docker)
- CI/CD automation (GitHub Actions)
- VPS deployment via SSH

---

## 🏗️ System Architecture

GitHub → GitHub Actions → VPS → Docker Compose → Nginx → FastAPI → PostgreSQL + Redis

---

## ⚙️ Key Features

- Fully containerized microservice architecture
- Automated CI/CD pipeline
- Health check monitoring endpoint
- Centralized logging system
- Secure environment variable management
- Reverse proxy configuration using Nginx
- Production-ready deployment workflow

---

## 📡 API Endpoints

### Root Endpoint
GET /

Returns service status.

### Health Check
GET /health

Checks:
- API status
- Database connection
- Redis connection

---

## 📁 Documentation Structure

All detailed system documentation is available inside `/docs`:

- ARCHITECTURE.md → System design
- DEPLOYMENT.md → Deployment steps
- CICD_PIPELINE.md → CI/CD pipeline automation
- SECURITY.md → Security practices
- SSL_SETUP.md → SSL configuration
- BACKUP_STRATEGY.md → Backup system

---

## 🚀 How It Works

1. Code pushed to GitHub
2. GitHub Actions runs tests
3. Docker image built
4. SSH connection to VPS
5. Docker containers updated
6. Health check validation

---
