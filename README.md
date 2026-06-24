# FastAPI Production Deployment Project

> [!NOTE]  
> **Deployment Status Notice**  
> This project is currently not deployed on an active VPS. Consequently, the GitHub Actions deployment workflow stage (deploy) will show as failed until valid SSH secrets (VPS_HOST, VPS_SSH_KEY, etc.) are configured in the repository's Settings. The pipeline's automated tests (test) execute and complete successfully in the runner environment.

This repository demonstrates a complete, production-grade backend deployment using FastAPI, Docker, Nginx, PostgreSQL, Redis, and a GitHub Actions CI/CD pipeline.

---

## Project Overview

This system is designed to simulate real-world production infrastructure with:

- Backend API (FastAPI)
- Database (PostgreSQL)
- Cache layer (Redis)
- Reverse proxy (NGINX)
- Containerization (Docker)
- CI/CD automation (GitHub Actions)
- VPS deployment via SSH

---

## System Architecture

GitHub -> GitHub Actions -> VPS -> Docker Compose -> Nginx -> FastAPI -> PostgreSQL + Redis

---

## Key Features

- Fully containerized microservice architecture
- Automated CI/CD pipeline
- Health check monitoring endpoint
- Centralized logging system
- Secure environment variable management
- Reverse proxy configuration using Nginx
- Production-ready deployment workflow

---

## API Endpoints

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

## Documentation Structure

All detailed system documentation is available inside the `/docs` directory:

- ARCHITECTURE.md: Detailed system design and request routing
- DEPLOYMENT.md: Step-by-step server deployment instructions
- CICD_PIPELINE.md: CI/CD automation workflow and secrets configuration
- SECURITY.md: Host security and container isolation practices
- SSL_SETUP.md: SSL certificate configuration guide
- BACKUP_STRATEGY.md: Automated backup policies and recovery plans
- FAIL2BAN.md: Intrusion prevention system configuration

---

## Deployment Flow

1. Code pushed to GitHub
2. GitHub Actions runs tests
3. Docker image built
4. SSH connection to VPS
5. Docker containers updated
6. Health check validation


---
