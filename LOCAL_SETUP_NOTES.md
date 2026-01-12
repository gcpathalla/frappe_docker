# ERPNext Local Setup & Troubleshooting Log

## Objective
Launch a local instance of ERPNext using Docker on Windows (WSL2) for testing/demo purposes.

## Methodology & Steps Taken

### 1. Repository & Configuration selection
- Investigated `frappe_docker` repository.
- Identified **`pwd.yml`** (Play With Docker) as the most suitable configuration for a quick, disposable local setup. It contains:
  - `frontend`: NGINX
  - `backend`: ERPNext (application server)
  - `db`: MariaDB
  - `redis`: Redis Cache/Queue
  - `create-site`: A one-off container to initialize the site.

### 2. Execution & Issues Encountered

#### Issue A: Database Initialization Failure
- **Symptom**: `create-site` container failed to connect to the database. Frontend returned "502 Bad Gateway".
- **Logs**: MariaDB container showed errors related to `InnoDB` and potential data corruption.
- **Cause**: Existing Docker volumes from a previous (possibly different) installation were conflicting with the new container version.
- **Fix**:
  1. Stopped all containers:
     ```bash
     docker compose -f pwd.yml down
     ```
  2. **CRITICAL**: Pruned Docker volumes to remove the corrupted data:
     ```bash
     docker volume prune
     # OR specifically: docker volume rm frappe_docker_db-data
     ```
  3. Pruned networks (good practice): `docker network prune`.
  4. Restarted: `docker compose -f pwd.yml up -d`.

#### Issue B: Initial "Internal Server Error" (500)
- **Symptom**: After restarting, the `create-site` container was running, but accessing `localhost:8080` resulted in a 500 error.
- **Diagnosis**: Checked logs for `create-site`:
  ```bash
  docker logs -f frappe_docker-create-site-1
  ```
- **Finding**: The process was valid and running (`bench new-site`), but it is resource-intensive. The 500 error is a normal temporary state while the database is being populated.
- **Resolution**: Waited approximately 5-10 minutes for the process to complete from "Updating DocTypes" to "Complete".

## Final Working State
- **URL**: http://localhost:8080
- **Credentials**:
  - User: `Administrator`
  - Pass: `admin`

## Quick Start Command (Summary)
If re-deploying from scratch:

```bash
# 1. Clean up old volumes (WARNING: Deletes data)
docker compose -f pwd.yml down -v

# 2. Start containers
docker compose -f pwd.yml up -d

# 3. Wait for installation (Monitor logs)
docker logs -f frappe_docker-create-site-1
```
