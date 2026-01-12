# ERPNext Docker - Quick Guide

## ✅ Setup Status

ERPNext is currently being installed in Docker containers!

The installation takes about 5-10 minutes total.

## 🚀 Access ERPNext

Once installation is complete, open your browser and go to:

**URL**: http://localhost:8080

**Login Credentials:**
- Username: `Administrator`
- Password: `admin`

## 📊 Check Installation Progress

To see the installation logs in real-time:

```bash
cd /c/Users/gcpat/repos_2/erpnext/frappe_docker
docker compose -f pwd.yml logs -f create-site
```

Press `Ctrl+C` to stop viewing logs.

## 🔧 Useful Docker Commands

### Check Container Status
```bash
cd /c/Users/gcpat/repos_2/erpnext/frappe_docker
docker compose -f pwd.yml ps
```

### View Logs
```bash
# All containers
docker compose -f pwd.yml logs

# Specific container
docker compose -f pwd.yml logs frontend
docker compose -f pwd.yml logs backend
docker compose -f pwd.yml logs db
```

### Stop ERPNext
```bash
docker compose -f pwd.yml stop
```

### Start ERPNext (after stopping)
```bash
docker compose -f pwd.yml start
```

### Restart ERPNext
```bash
docker compose -f pwd.yml restart
```

### Stop and Remove Everything
```bash
docker compose -f pwd.yml down
```

### Stop and Remove Everything Including Data (⚠️ CAUTION)
```bash
docker compose -f pwd.yml down -v
```

## 🛠️ ERPNext Commands

Once ERPNext is running, you can execute commands inside the container:

```bash
# Access Frappe console
docker compose -f pwd.yml exec backend bench --site frontend console

# Run migrations
docker compose -f pwd.yml exec backend bench --site frontend migrate

# Clear cache
docker compose -f pwd.yml exec backend bench --site frontend clear-cache

# Create backup
docker compose -f pwd.yml exec backend bench --site frontend backup

# List all sites
docker compose -f pwd.yml exec backend bench --site frontend list-apps
```

## 📂 Data Persistence

Your ERPNext data is stored in Docker volumes:
- `frappe_docker_db-data` - Database data
- `frappe_docker_sites` - Site files
- `frappe_docker_redis-queue-data` - Queue data

These persist even if you stop the containers!

## 🔄 Update ERPNext

To update to the latest version:

```bash
cd /c/Users/gcpat/repos_2/erpnext/frappe_docker
docker compose -f pwd.yml pull
docker compose -f pwd.yml down
docker compose -f pwd.yml up -d
```

## ⚡ Quick Start/Stop Commands

Create shortcuts for easy access:

**Start ERPNext:**
```bash
cd /c/Users/gcpat/repos_2/erpnext/frappe_docker && docker compose -f pwd.yml start
```

**Stop ERPNext:**
```bash
cd /c/Users/gcpat/repos_2/erpnext/frappe_docker && docker compose -f pwd.yml stop
```

**View Status:**
```bash
cd /c/Users/gcpat/repos_2/erpnext/frappe_docker && docker compose -f pwd.yml ps
```

## 🌐 Accessing from Other Devices

To access ERPNext from other devices on your network:
1. Find your computer's IP address: `ipconfig` (look for IPv4 Address)
2. Access from other device: `http://YOUR_IP:8080`

## 🆘 Troubleshooting

**Container won't start?**
```bash
docker compose -f pwd.yml logs <container-name>
```

**Port 8080 already in use?**
Edit `pwd.yml` and change the port:
```yaml
ports:
  - "8081:8080"  # Change 8080 to 8081
```

**Need to reset everything?**
```bash
docker compose -f pwd.yml down -v
docker compose -f pwd.yml up -d
```
(This will delete all data and start fresh)

**Database issues?**
```bash
docker compose -f pwd.yml restart db
docker compose -f pwd.yml restart backend
```

## 📱 Next Steps After Login

1. Complete the setup wizard
2. Set up your company
3. Explore ERPNext modules:
   - Accounting
   - Inventory
   - Sales
   - Purchase
   - HR
   - Manufacturing
   - CRM
   - And more!

## 📚 Resources

- ERPNext Documentation: https://docs.erpnext.com/
- Frappe Framework Docs: https://frappeframework.com/docs
- Community Forum: https://discuss.frappe.io/
- GitHub: https://github.com/frappe/erpnext

---

**Enjoy using ERPNext!** 🎉
