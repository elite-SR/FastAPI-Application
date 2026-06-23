# 📦 Backup Strategy (Manual + Automated Combined)

---

# 🎯 Why Backup is Important?

In a production system, data is the most critical part.

We use backups to protect against:

- Server crash
- Database failure
- Human mistakes
- Deployment issues

This ensures we can always restore the system quickly.

---

# 🗄 1. Manual Backup (On-Demand)

This method is used when we want to take backup instantly.

---

## 📌 Create Backup

Run this command on VPS:

```bash
docker exec -t fastapi-application-db-1 pg_dump -U postgres production_db > backup.sql

📌 Restore Backup

If something goes wrong, restore using:

cat backup.sql | docker exec -i fastapi-application-db-1 psql -U postgres production_db

2. Automated Backup (Recommended)

This runs automatically every day without manual effort.

📌 Step 1: Create backup script
sudo nano /opt/backup.sh
📌 Step 2: Add script content
#!/bin/bash

DATE=$(date +%Y-%m-%d_%H-%M-%S)
BACKUP_DIR=/opt/backups

mkdir -p $BACKUP_DIR

# Take database backup from container
docker exec fastapi-application-db-1 pg_dump -U postgres production_db > $BACKUP_DIR/db_$DATE.sql

# Keep only last 7 days backups
find $BACKUP_DIR -type f -mtime +7 -delete
📌 Step 3: Give execution permission
chmod +x /opt/backup.sh
📌 Step 4: Schedule automatic backup (Cron Job)
crontab -e

Add this line:

0 2 * * * /opt/backup.sh

👉 This means:

Backup runs every day at 2:00 AM automatically

Recovery Process (Important)

If system fails:

docker compose down
docker compose up -d

Then restore database:

cat backup.sql | docker exec -i fastapi-application-db-1 psql -U postgres production_db
🔐 Security Notes
Backup folder must NOT be public
Restrict permissions:
chmod 700 /opt/backups