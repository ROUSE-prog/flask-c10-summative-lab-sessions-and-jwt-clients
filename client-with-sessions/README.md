# Full Authentication Flask Backend – Productivity Tool

A full-stack productivity application built with **Flask**, **SQLAlchemy**, **React**, and **Flask Sessions**. This project demonstrates secure user authentication, session persistence, protected CRUD operations, pagination, and a React frontend connected to a Flask REST API.

---

## Features

### Authentication

* User registration (Sign Up)
* Secure login using Flask Sessions
* Logout functionality
* Password hashing with Flask-Bcrypt
* Session persistence using `/check_session`
* Protected routes for authenticated users

### Task Management

Each authenticated user manages their own tasks.

Features include:

* Create tasks
* View paginated tasks
* Update existing tasks
* Delete tasks
* Mark tasks complete/incomplete
* User-specific authorization

---

## Technologies Used

### Backend

* Python 3
* Flask
* Flask SQLAlchemy
* Flask Migrate
* Flask Bcrypt
* Flask CORS
* SQLAlchemy Serializer
* SQLite

### Frontend

* React
* JavaScript
* Fetch API

---

## Database Models

### User

* id
* username
* email
* password_hash

Relationships:

* One User has many Tasks

### Task

* id
* title
* description
* priority
* completed
* user_id

Relationships:

* Each Task belongs to one User

---

## Authentication Endpoints

| Method | Endpoint         | Description                       |
| ------ | ---------------- | --------------------------------- |
| POST   | `/signup`        | Create a new user                 |
| POST   | `/login`         | Login user                        |
| DELETE | `/logout`        | Logout current user               |
| GET    | `/check_session` | Verify active session             |
| GET    | `/me`            | Return current authenticated user |

---

## Task API

| Method | Endpoint      | Description            |
| ------ | ------------- | ---------------------- |
| GET    | `/tasks`      | Return paginated tasks |
| POST   | `/tasks`      | Create task            |
| GET    | `/tasks/<id>` | Return single task     |
| PATCH  | `/tasks/<id>` | Update task            |
| DELETE | `/tasks/<id>` | Delete task            |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ROUSE-prog/flask-c10-summative-lab-sessions-and-jwt-clients.git
cd flask-c10-summative-lab-sessions-and-jwt-clients
```

---

## Backend Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install flask flask-sqlalchemy flask-migrate flask-bcrypt flask-cors sqlalchemy-serializer
```

Run database migrations:

```bash
cd server

python -m flask --app app db upgrade
```

Seed the database:

```bash
python seed.py
```

Start the Flask server:

```bash
python -m flask --app app run --port 5555
```

---

## Frontend Setup

Open another terminal:

```bash
cd client-with-sessions

npm install
npm start
```

The React application will launch at:

```
http://localhost:4000
```

---

## Testing

The backend was tested using:

* Browser
* curl
* React Client

Verified functionality:

* User signup
* User login
* Logout
* Session persistence
* Protected routes
* Pagination
* Create task
* Read tasks
* Update task
* Delete task

---

## Project Structure

```
server/
│
├── app.py
├── config.py
├── models.py
├── seed.py
├── migrations/
│
client-with-sessions/
│
├── src/
│   ├── components/
│   ├── pages/
│   └── styles/
```

---

## Future Improvements

* Due dates
* Task categories
* Search and filtering
* Sorting
* Task reminders
* JWT authentication version
* Deployment to Render or Railway

---