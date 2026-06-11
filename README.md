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
evaluator/
├── models/
├── serializers/
├── views/
├── services/
│   ├── grammar_service.py
│   ├── similarity_service.py
│   ├── scoring_service.py
└── urls.py

---

# Credits
Juan Diego Corella Camacho
Backend Developer | Full Stack | Telecommunications & Systems Engineering

---
