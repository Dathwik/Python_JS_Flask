# Contact Manager – Full Stack Web Application

A full-stack contact management application that allows users to **create, view, update, and delete contacts** through a responsive web interface.

The application is built using **React for the frontend and Flask for the backend**, with **PostgreSQL** used as the production database. The project demonstrates REST API design, database integration, and full-stack deployment.

---

## Live Demo

**Frontend**  
https://python-js-flask.onrender.com

**Backend API**  
https://contactlist-backend-f3pa.onrender.com

---

# Features

- Create new contacts
- View all saved contacts
- Update existing contacts
- Delete contacts
- RESTful API architecture
- Persistent PostgreSQL database
- Cross-origin communication using CORS
- Deployed full-stack application

---

# Tech Stack

## Frontend
- React
- JavaScript
- HTML5
- CSS3
- Vite

## Backend
- Python
- Flask
- Flask SQLAlchemy
- Flask CORS

## Database
- PostgreSQL (Production)
- SQLite (Local development)

## Deployment
- Render (Frontend + Backend Hosting)

---

# Project Structure

```
Python_JS_Flask
│
├── backend
│   ├── main.py
│   ├── config.py
│   ├── models.py
│   └── requirements.txt
│
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# API Endpoints

## Get All Contacts

```
GET /contacts
```

Example Response

```json
{
  "contacts": [
    {
      "id": 1,
      "firstName": "John",
      "lastName": "Doe",
      "email": "john@example.com"
    }
  ]
}
```

---

## Create Contact

```
POST /create_contact
```

Request Body

```json
{
  "firstName": "John",
  "lastName": "Doe",
  "email": "john@example.com"
}
```

---

## Update Contact

```
PATCH /update_contact/<id>
```

---

## Delete Contact

```
DELETE /delete_contact/<id>
```

---

# Running the Project Locally

## 1 Clone the Repository

```
git clone https://github.com/Dathwik/Python_JS_Flask.git
cd Python_JS_Flask
```

---

# Backend Setup

Create virtual environment

```
python -m venv venv
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run the Flask server

```
python main.py
```

Backend will run on

```
http://localhost:5000
```

---

# Frontend Setup

Navigate to frontend folder

```
cd frontend
```

Install dependencies

```
npm install
```

Run development server

```
npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# Environment Variables

The backend requires a database connection string.

Example:

```
DATABASE_URL=postgresql://user:password@host:port/database
```

In production this is configured inside **Render environment variables**.

---

# Deployment

The application is deployed using **Render**.

Deployment includes:

- Flask API service
- PostgreSQL database
- Static React frontend hosting

---

# What I Learned

Through this project I learned how to:

- Build REST APIs using Flask
- Connect backend services to a relational database
- Use SQLAlchemy ORM for database operations
- Handle CORS between frontend and backend
- Deploy full-stack applications to the cloud
- Manage environment variables securely in production

---

# Future Improvements

- Add authentication and user accounts
- Implement search and filtering for contacts
- Add pagination
- Improve UI design
- Add automated tests
- Containerize using Docker

---

# Author

**Dathwik Kollikonda**

GitHub  
https://github.com/Dathwik
