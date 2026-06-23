# 🔐 SSL Setup Strategy (Full Production Guide)

---

# 🌍 Why SSL?

- Encrypts communication
- Prevents attacks
- Enables HTTPS
- Required for production systems

---

# ❌ WITHOUT DOMAIN

SSL cannot be issued without a domain using Let's Encrypt.

---

## 🟡 Option 1: Self-Signed SSL (Testing only)

openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
-keyout key.pem \
-out cert.pem

⚠ Browser will show warning

---

## 🟡 Option 2: Cloudflare SSL (Recommended without domain SSL)

Steps:
1. Add domain to Cloudflare
2. Point DNS to VPS
3. Enable proxy (orange cloud)
4. SSL mode:

Full (Strict)

✔ Cloudflare handles HTTPS externally

---

# 🌐 WITH DOMAIN (PRODUCTION METHOD)

---

## Step 1: DNS Setup

example.com → VPS_IP
www.example.com → VPS_IP

---

## Step 2: Install NGINX + Certbot

sudo apt update
sudo apt install nginx certbot python3-certbot-nginx -y

---

## Step 3: Basic NGINX Config

server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://web:8000;
    }
}

---

## Step 4: Issue SSL Certificate

sudo certbot --nginx -d example.com -d www.example.com

✔ Automatically configures SSL + redirect

---

## Step 5: Certificate Location

/etc/letsencrypt/live/example.com/

- fullchain.pem
- privkey.pem

---

## Step 6: Auto Renewal

sudo certbot renew --dry-run

Cron:
0 3 * * * certbot renew --quiet

---

# 🐳 DOCKER SSL INTEGRATION

---

## docker-compose volume

- /etc/letsencrypt:/etc/letsencrypt:ro

---

## NGINX SSL config

ssl_certificate     /etc/letsencrypt/live/example.com/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

---

# 🔁 FINAL FLOW

Client → HTTPS → NGINX → FastAPI → DB + Redis

---

# 💡 SUMMARY

- No domain → use Cloudflare or self-signed SSL
- Domain → use Certbot + NGINX
- Docker mounts certificates from host