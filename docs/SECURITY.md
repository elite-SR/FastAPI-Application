# 🔐 Production Security Hardening Plan

Securing a VPS in a production environment requires a multi-layered approach. Below is the security hardening plan configured for this application stack.

---

## 🛡️ Host Server Level Hardening

### 1. Secure SSH Access
By default, standard passwords can be targeted by brute-force attacks. We disable password authentication entirely, allowing only cryptographic SSH keys.

* **Disable Password Logins:**
  Edit the SSH daemon configuration on the VPS:
  ```bash
  sudo nano /etc/ssh/sshd_config
  ```
  Ensure the following properties are configured:
  ```text
  PasswordAuthentication no
  PubkeyAuthentication yes
  PermitRootLogin no
  ```
  Restart the SSH daemon to apply changes:
  ```bash
  sudo systemctl restart ssh
  ```

### 2. Configure Host Firewall (UFW)
A firewall blocks all ports that are not explicitly whitelisted. We configure the Uncomplicated Firewall (UFW) to only expose SSH (port `22`), HTTP (port `80`), and HTTPS (port `443`):

```bash
# Set default rules to deny all incoming traffic
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow required ports
sudo ufw allow 22/tcp   # SSH
sudo ufw allow 80/tcp   # HTTP
sudo ufw allow 443/tcp  # HTTPS

# Enable the firewall
sudo ufw enable

# Check active status
sudo ufw status verbose
```

---

## 🐳 Docker and Container Level Isolation

### 1. Network Boundary Isolation
Our databases (`db` and `redis`) handle sensitive persistent data. They are configured on a private bridge network (`production_network`).
* **Zero Direct Exposure:** PostgreSQL and Redis containers do not expose ports to the public internet (`0.0.0.0`). Their port configuration in `docker-compose.yml` maps to local loopback interface `127.0.0.1`:
  ```yaml
  ports:
    - "127.0.0.1:5432:5432"
  ```
* This ensures that only local processes on the VPS host or containers inside `production_network` can communicate with the databases.

### 2. Non-Root Container Execution
Running containers as `root` is a security risk. If a container is compromised, the attacker could gain root privileges on the host system.
* Our `Dockerfile` addresses this by generating a specific user account:
  ```dockerfile
  RUN useradd -u 8888 appuser && chown -R appuser:appuser /app
  USER appuser
  ```
* The application runs with restricted permissions.

---

## 🔑 Environment Secrets Protection

* **Strict gitignore rules:** All system passwords, database URLs, and environment configuration profiles are excluded from git tracking via `.gitignore`.
* **Zero Hardcoded Secrets:** Credentials are dynamically resolved at runtime from the local host system environment variables.