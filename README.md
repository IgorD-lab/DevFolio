# DevSearch

**Status:** Completed and actively maintained
**Deployment:** Pending (moving to Supabase for production hosting)

---

## Overview

DevSearch is a full-stack web platform built with **Django** that enables developers to:

* Showcase their projects
* Receive feedback through comments and votes
* Build a profile highlighting skills and experience
* Search and connect with other developers

It is designed as a practical community hub for developers to share work and collaborate.

---

## Key Features

* **Authentication & Profiles**
  User registration, login, logout, and profile management with skills and bio.

* **Project Management**
  Create, edit, and delete projects, complete with descriptions and tags.

* **Community Interaction**
  Comment on projects and provide feedback through an integrated voting system.

* **Search & Discovery**
  Find developers and projects using search filters and pagination for easier navigation.

* **Responsive UI**
  Clean and user-friendly layout optimized for both desktop and mobile.

---

## Technical Highlights

* **Backend:** Django, Django REST Framework
* **Database:** PostgreSQL (with SQLite option for local testing)
* **Authentication:** Django’s built-in auth system with profile extensions
* **Project Structure:** Modular apps (`users`, `projects`, etc.)
* **Deployment:** Prepared for cloud hosting (migrating to Supabase)

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone <repo_url>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> ⚠ On Linux, `psycopg2` may fail. If so:
>
> ```bash
> pip install --upgrade wheel psycopg2
> ```

### 3. Configure Database

For quick local testing with **SQLite**:

* In `/devfolio/settings.py`, uncomment the SQLite `DATABASES` block
* Comment out the PostgreSQL configuration

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Future Development

While the core platform is complete, upcoming improvements include:

* **Community Board**: a simple discussion space for open developer conversations
* **Testing & CI/CD**: unit tests, API validation, automated workflows
* **Dockerization**: containerization for easier deployment and scaling
* **Expanded Documentation**: detailed guides for contributors and deployment

---

## Documentation

* **Guide (WIP):** `Guide.odt` provides an outline of the current functionality and development process
* Full developer documentation will follow after deployment
