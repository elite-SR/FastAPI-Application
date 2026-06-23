# 🏗 System Architecture

This project follows a container-based microservice architecture.

---

## 📌 Architecture Flow

GitHub
   ↓
GitHub Actions (CI/CD)
   ↓
VPS Server
   ↓
Docker Compose
   ↓
NGINX Reverse Proxy
   ↓
FastAPI Application
   ↓
PostgreSQL + Redis

---

## 🧩 Components

### 1. FastAPI
- Handles API requests
- Exposes endpoints (/ and /health)

### 2. PostgreSQL
- Stores application data
- Runs in Docker container

### 3. Redis
- Used for caching and fast access

### 4. NGINX
- Acts as reverse proxy
- Routes traffic to FastAPI
- Handles HTTP requests from users

---

## 🔄 Request Flow

User Request → Nginx → FastAPI → DB/Redis → Response