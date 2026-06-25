# Full-Stack Productivity Tool

A full-stack productivity application built with **Flask**, **React**, **SQLAlchemy**, and **Flask Sessions**. The application provides secure user authentication, persistent login sessions, protected CRUD operations, pagination, and a responsive React frontend for managing personal tasks.

---

# Features

## Backend (Flask API)

* User Registration
* User Login
* User Logout
* Session Authentication
* Session Persistence (`/check_session`)
* Password Hashing with Flask-Bcrypt
* Protected Routes
* User Authorization
* Full REST API
* Pagination
* SQLite Database
* Alembic Migrations
* Seed Data

---

## Frontend (React)

The React client communicates directly with the Flask API using the Fetch API and browser sessions.

Users can:

* Sign Up
* Log In
* Stay logged in after refreshing
* View personal tasks
* Create new tasks
* Edit task completion status
* Delete tasks
* Log Out

The frontend automatically checks authentication status using the `/check_session` endpoint when the application loads.

---

# Technologies

## Backend

* Python 3
* Flask
* Flask SQLAlchemy
* Flask Migrate
* Flask Bcrypt
* Flask CORS
* SQLAlchemy Serializer
* SQLite

## Frontend

* React
* JavaScript
* Fetch API
* React Hooks
* Component-Based Architecture

---

# Database Models

## User

* id
* username
* email
* password_hash

Relationship

* One User has Many Tasks

---

## Task

* id
* title
* description
* priority
* completed
* user_id

Relationship

* Belongs to one User

---

# Authentication API

| Method | Endpoint         | Description                       |
| ------ | ---------------- | --------------------------------- |
| POST   | `/signup`        | Register a new user               |
| POST   | `/login`         | Authenticate user                 |
| DELETE | `/logout`        | End user session                  |
| GET    | `/check_session` | Verify active session             |
| GET    | `/me`            | Return current authenticated user |

---

# Task API

| Method | Endpoint      | Description            |
| ------ | ------------- | ---------------------- |
| GET    | `/tasks`      | Return paginated tasks |
| POST   | `/tasks`      | Create task            |
| GET    | `/tasks/<id>` | Return one task        |
| PATCH  | `/tasks/<id>` | Update task            |
| DELETE | `/tasks/<id>` | Delete task            |

---

# Installation

Clone the repository

```bash
git clone https://github.com/ROUSE-prog/flask-c10-summative-lab-sessions-and-jwt-clients.git

cd flask-c10-summative-lab-sessions-and-jwt-clients
```

---

# Backend Setup

Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install flask flask-sqlalchemy flask-migrate flask-bcrypt flask-cors sqlalchemy-serializer
```

Initialize the database

```bash
cd server

python -m flask --app app db upgrade
```

Seed the database

```bash
python seed.py
```

Start the Flask server

```bash
python -m flask --app app run --port 5555
```

---

# Frontend Setup

Open a second terminal.

```bash
cd client-with-sessions

npm install

npm start
```

The React application runs on:

```
http://localhost:4000
```

The Flask backend runs on:

```
http://localhost:5555
```

---

# User Workflow

1. Register a new account.
2. Login securely.
3. Session is stored using Flask Sessions.
4. Refreshing the page keeps the user logged in.
5. Create tasks.
6. Update task completion.
7. Delete tasks.
8. Logout.

---

# Testing

The application was tested by verifying:

* User Signup
* Login
* Logout
* Session Persistence
* Protected Routes
* Authorization
* CRUD Operations
* Pagination
* React Frontend Integration
* Flask API Integration

---

# Project Structure

```
server/
│
├── app.py
├── config.py
├── models.py
├── seed.py
├── migrations/

client-with-sessions/
│
├── src/
│   ├── components/
│   │   ├── App.js
│   │   ├── LoginForm.js
│   │   ├── SignUpForm.js
│   │   ├── TaskManager.js
│   │   └── NavBar.js
│   ├── pages/
│   └── styles/
```

---

# Future Improvements

* Task due dates
* Categories
* Search
* Sorting
* File attachments
* JWT Authentication version
* Cloud deployment
* Mobile responsive improvements

