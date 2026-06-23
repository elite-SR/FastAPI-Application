# 🔐 Security Measures

---

## 🔑 Authentication & Access

- SSH key-based authentication used for VPS
- Password login disabled (recommended)

---

## 🌐 Network Security

- NGINX used as reverse proxy
- Backend not directly exposed to internet
- Only port 80 exposed externally

---

## 🔒 Environment Security

- Sensitive data stored in `.env`
- No hardcoded credentials in code
- Database credentials secured via environment variables

---

## 🧱 Firewall (Recommended)

UFW rules:

ufw allow 22
ufw allow 80
ufw enable

---

## 🐳 Docker Security

- Services isolated in Docker network
- No direct DB exposure to external world