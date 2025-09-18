# DevSearch

**Release Date:** TBD (AWS deployment pending)

## Description

DevSearch is a web platform built with **Django** that allows developers to:

* Share their projects
* Comment on other projects
* Vote on each other’s work

The platform is designed to make it easier for developers to showcase their skills and connect with peers.

---

## Project Status

This project is actively being developed. Daily progress is made toward reaching a fully functional and production-ready state.

### Completed Features

* User authentication (register, login, logout)
* Profile creation and editing
* Project creation, editing, and deletion
* Commenting on projects
* Voting system for projects
* Search functionality (find developers and projects)
* Pagination for project lists

### In Progress

* Messaging system (direct user-to-user communication)
* Ratings & reviews improvements
* Deployment to AWS (currently resolving issues)
* Expanded documentation (Guide + full README)

---

## Getting Started

### 1. Clone the Repository

```bash
git clone <repo_url>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> ⚠ On Linux, the `psycopg2` package may cause issues. If installation fails:
>
> * Remove it from `requirements.txt`
> * Install manually with:
>
>   ```bash
>   pip install --upgrade wheel psycopg2
>   ```

### 3. Configure Database

For quick testing with **SQLite**:

* Open `/devfolio/settings.py`
* Uncomment the `DATABASES = {... sqlite3 ...}` block
* Comment out the PostgreSQL `DATABASES` block

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Documentation

* **Guide (WIP):** `Guide.odt` contains a draft overview of site functionality.
* A full documentation release will follow once AWS deployment is resolved.
