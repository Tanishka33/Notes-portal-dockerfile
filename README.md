# Docker Notes Portal

A simple real-world Docker project to practice:

* Dockerfiles
* Multi-container setup
* Docker Networking
* Port Mapping
* Named Volumes
* Bind Mounts
* Container Communication
* Persistent Storage
* Docker Commands

This project contains:

* Frontend container (Nginx)
* Backend container (Python Flask)
* Persistent storage for employee notes

---

# Project Architecture

```text
Browser
   ↓
localhost:8080
   ↓
Frontend Container (Nginx)
   ↓
Docker Network
   ↓
Backend Container (Flask)
   ↓
/app/data
   ↓
Docker Volume OR Bind Mount
   ↓
Persistent Employee Notes
```

---

# Project Structure

```text
notes-portal/
│
├── frontend/
│   ├── index.html
│   └── Dockerfile.frontend
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile.backend
│
└── storage/
```

---

# Features

* Employee can enter name and note
* Backend creates employee text files
* Notes persist even after container restart
* Frontend and backend communicate using Docker network
* Bind mounts used for live storage visibility

---

# Step 1 — Build Frontend Image

```bash
cd frontend

docker build -f Dockerfile.frontend -t notes-frontend:v1 .
```

Verify image:

```bash
docker images
```

---

# Step 2 — Build Backend Image

```bash
cd ../backend

docker build -f Dockerfile.backend -t notes-backend:v1 .
```

Verify image:

```bash
docker images
```

---

# Step 3 — Create Docker Network

```bash
docker network create notes-network
```

Verify:

```bash
docker network ls
```

---

# Step 4 — Run Frontend Container

```bash
docker run -d \
--name frontend-container \
--network notes-network \
-p 8080:80 \
notes-frontend:v1
```

---

# Step 5 — Run Backend Container

## Using Bind Mount (Recommended for Learning)

Go to project root folder:

```bash
cd ~/notes-portal
```

Run backend:

```bash
docker run -d \
--name backend-container \
--network notes-network \
-p 5000:5000 \
-v $(pwd)/storage:/app/data \
notes-backend:v1
```

---

# Access Application

Frontend:

```text
http://localhost:8080
```

Backend:

```text
http://localhost:5000
```

---

# How Storage Works

Employee submits:

```text
Name: Tanushka
Note: Docker networking completed
```

Backend creates:

```text
storage/Tanushka.txt
```

This file is visible directly in VSCode because bind mount is used.

---

# Verify Running Containers

```bash
docker ps
```

---

# View Logs

Frontend logs:

```bash
docker logs frontend-container
```

Backend logs:

```bash
docker logs backend-container
```

---

# Enter Inside Containers

Frontend container:

```bash
docker exec -it frontend-container sh
```

Backend container:

```bash
docker exec -it backend-container sh
```

---

# Verify Network Communication

Enter frontend container:

```bash
docker exec -it frontend-container sh
```

Ping backend:

```bash
ping backend-container
```

---

# Stop Containers

```bash
docker stop frontend-container backend-container
```

---

# Start Existing Containers Again

```bash
docker start frontend-container backend-container
```

---

# Remove Containers

```bash
docker rm -f frontend-container backend-container
```

---

# Remove Images

```bash
docker rmi notes-frontend:v1 notes-backend:v1
```

---

# Remove Network

```bash
docker network rm notes-network
```

---

# Docker Concepts Practiced

## Dockerfile

* Building custom images
* Using official base images
* Copying application files
* Exposing ports

## Networking

* Custom bridge network
* Container-to-container communication
* Docker DNS

## Port Mapping

* Host port to container port mapping
* Browser access

## Volumes

* Bind mounts
* Persistent storage
* Host ↔ container file sync

## Containers

* Build, run, stop, remove
* Container lifecycle
* Inspecting running containers

---

# Important Learning

## Containers are Ephemeral

Deleting container removes container filesystem.

## Persistent Storage

Employee notes survive because storage is mounted outside container writable layer.

## Container Networking

Containers communicate using container names inside Docker network.

---

# Useful Docker Commands

## List Containers

```bash
docker ps
```

## List All Containers

```bash
docker ps -a
```

## List Images

```bash
docker images
```

## List Networks

```bash
docker network ls
```

## List Volumes

```bash
docker volume ls
```

## Inspect Container

```bash
docker inspect backend-container
```

## Inspect Network

```bash
docker network inspect notes-network
```

---

# Future Improvements

* Docker Compose
* MySQL Database
* Multi-stage Dockerfiles
* Nginx Reverse Proxy
* AWS ECR Push
* Kubernetes Deployment

---

# Author

Tanishka Borade
