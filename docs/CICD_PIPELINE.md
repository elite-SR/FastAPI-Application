# 🤖 GitHub Actions CI/CD Pipeline Workflow

> [!NOTE]  
> **Deployment Status Notice:**  
> This project has **not** been linked to a live Virtual Private Server (VPS) host yet. As a result, the `deploy` stage of the GitHub Actions workflow will fail (or skip) because the connection variables (`VPS_HOST`, `VPS_SSH_KEY`, etc.) are not configured as secrets in the repository. The testing stage (`test`), however, runs inside GitHub's container environment and passes successfully.

This project implements a fully automated Continuous Integration and Continuous Deployment (CI/CD) pipeline via **GitHub Actions**. Every time code is pushed to the `main` branch, the pipeline automatically tests the codebase and deploys it to the remote VPS host.

---

## 🔄 The CI/CD Pipeline Workflow

```mermaid
graph TD
    Push[Push to main branch] --> TestJob[Job 1: Run Test Suite]
    
    subgraph GitHub Runner [GitHub Actions Virtual Environment]
        TestJob --> SetupPython[Setup Python 3.11]
        SetupPython --> StartDBs[Start Temp Postgres & Redis Service Containers]
        StartDBs --> RunPytest[Run pytest Validation Suite]
    end
    
    RunPytest -->|Passed| DeployJob[Job 2: Deploy to VPS]
    RunPytest -->|Failed| StopPipeline[❌ Stop Pipeline & Alert Developer]
    
    subgraph Production Server [Virtual Private Server Host]
        DeployJob --> SSH[SSH Connection via Key]
        SSH --> GitPull[Pull Latest code from GitHub]
        GitPull --> DockerBuild[docker compose build --no-cache]
        DockerBuild --> DockerUp[docker compose up -d]
        DockerUp --> HealthCheck[Wait & Run Health Check Validation]
        HealthCheck --> Prune[Prune Obsolete Images]
    end
```

---

## 🛠️ Pipeline Stages Explained

### 1. The Validation Stage (`test`)
This stage runs in a clean, ephemeral Ubuntu environment on GitHub's runners. It guarantees that code changes do not break core APIs before touching production.
* **Service Containers:** Rather than mocking database layers, GitHub Actions spins up real, isolated instances of PostgreSQL and Redis.
* **Testing:** Installs dependencies (`fastapi`, `psycopg2-binary`, `redis`, etc.) and runs `pytest` against the application endpoints to verify health checks and system responses.

### 2. The Deployment Stage (`deploy`)
If and only if the test suite completes with a passing grade, the deployment pipeline triggers:
* **Secure Handshake:** Connects to the host VPS using SSH keys.
* **Graceful Rebuild:** Fetches the updated code, rebuilds the application containers, and restarts the services.
* **Uptime Validation:** Executes a loop pinging the `/health` endpoint to ensure the system is up and functioning correctly post-deployment.
* **Disk Housekeeping:** Runs a prune command to clean up older build cache layers and unused images, preventing the host disk from filling up over time.

---

## 🔑 Required GitHub Secrets Configuration

To run this pipeline successfully, you must register your server credentials as **Encrypted Secrets** in your GitHub Repository. 

1. Go to your repository on GitHub.
2. Navigate to **Settings** ➔ **Secrets and variables** ➔ **Actions**.
3. Create the following four secrets:

| Secret Name | Description | Example Value |
| :--- | :--- | :--- |
| `VPS_HOST` | The public IP address of your VPS. | `192.168.1.100` |
| `VPS_USER` | The user account used to SSH into the server. | `ubuntu` or `root` |
| `VPS_SSH_KEY` | The private SSH key (matching the public key in your server's `authorized_keys`). | `-----BEGIN OPENSSH PRIVATE KEY----- ...` |
| `VPS_PORT` | The custom SSH port configured on your server (defaults to 22). | `22` |

---

## 🔍 How to Monitor Builds
* Every run can be reviewed under the **Actions** tab of your repository.
* Detailed step-by-step stdout/stderr output is available for both the runner tests and remote SSH commands to make debugging deployment errors straightforward.
