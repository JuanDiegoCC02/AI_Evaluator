# 📘 AI Evaluator

AI Evaluator is a backend system built with Django REST Framework that automatically evaluates text responses using Natural Language Processing (NLP). It combines grammatical analysis and semantic similarity to generate a final score and quality classification.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)
![Django REST Framework](https://img.shields.io/badge/DRF-API-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

---

# 🚀 Overview

This project analyzes a user response against a reference text and returns an objective evaluation based on:

- Grammar correctness
- Semantic similarity
- Text quality scoring

Each evaluation is stored for historical tracking and analytics.

---

# ⚙️ Tech Stack

- Django REST Framework
- PostgreSQL
- Sentence Transformers
- LanguageTool
- Cosine Similarity (scikit-learn)
- drf-spectacular (OpenAPI / Swagger)

---

# 🧠 Core Features

## NLP Processing
- Grammar correction using LanguageTool
- Semantic embeddings using Sentence Transformers
- Cosine similarity computation between texts

## Scoring System
- Automatic score generation based on NLP metrics
- Classification labels:
  - Excellent
  - Good
  - Average
  - Poor

## Backend Architecture
- Modular service-based structure (`services/`)
- Clean separation of concerns (views, serializers, services)
- RESTful API design

## Data Persistence
- PostgreSQL database
- Evaluation history storage
- Structured analytics support

---

# 📡 API Endpoints
- POST /api/evaluations/
- GET /api/evaluations/
- GET /api/stats/

# 📄 API Documentation
- Swagger UI: /api/docs/
- OpenAPI Schema: /api/schema/
- Redoc: /api/redoc/

---

# 🏗️ Project Structure

```text
evaluator/
│
├── evaluations/
│   ├── services/
│   │   ├── grammar_service.py
│   │   ├── similarity_service.py
│   │   └── scoring_service.py
│   │
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── evaluator/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🔧 Installation

## Clone Repository

```bash
git clone https://github.com/JuanDiegoCC02/AI-Evaluator.git
cd AI-Evaluator
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure PostgreSQL

Create a PostgreSQL database and update your database configuration in:

```python
settings.py
```

Example:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ai_evaluator",
        "USER": "postgres",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

## Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Run Development Server

```bash
python manage.py runserver
```

Application available at:

```text
http://127.0.0.1:8000/
```

## API Documentation

Swagger UI

```text
http://127.0.0.1:8000/api/docs/
```

OpenAPI Schema

```text
http://127.0.0.1:8000/api/schema/
```

Redoc

```text
http://127.0.0.1:8000/api/redoc/
```


---

# Credits
Juan Diego Corella Camacho
Backend Developer | Full Stack | Telecommunications & Systems Engineering

---
