# 📄 DocMind - AI Document Assistant

DocMind is a full-stack AI-powered document assistant that allows users to upload PDF documents, extract their content, and ask natural language questions using **Google Gemini AI**.

The backend is built with **FastAPI**, **PostgreSQL**, **pgvector**, and **Retrieval-Augmented Generation (RAG)**, while the frontend is built with **Flutter**.

---

# ✨ Features

- 👤 User Registration & Login
- 🔐 JWT Authentication
- 📄 PDF Upload
- 📖 Automatic PDF Text Extraction
- 🤖 Google Gemini AI Integration
- 🧠 Retrieval-Augmented Generation (RAG)
- 💬 Persistent Chat History
- 🧠 Conversation Memory
- 🗂️ Document Management
- 🗑️ Delete Documents & Chat History
- 🛡️ User-specific Data Isolation
- ⚡ RESTful APIs
- 🗄️ PostgreSQL Database
- 🧬 pgvector Semantic Search
- 🐳 Docker & Docker Compose Support
- 📱 Clean Flutter UI

---

# 🏗️ Architecture

```text
Flutter App
      │
      ▼
 FastAPI Backend
      │
      ├──────────────► Google Gemini API
      │
      ▼
 PostgreSQL + pgvector
```

---

# 🛠 Tech Stack

## Frontend

- Flutter
- GetX
- Dio
- Flutter Markdown

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- pgvector
- Alembic
- JWT Authentication
- Docker
- Docker Compose

## AI

- Google Gemini API
- Retrieval-Augmented Generation (RAG)
- Vector Embeddings
- Semantic Search

---

# 📱 Screenshots

## Splash Screen

<img src="screenshots/splash.png" width="260">

---

## Login Screen

<img src="screenshots/login.png" width="260">

---

## Empty Library

<img src="screenshots/nodoc.png" width="260">

---

## Upload Document

<img src="screenshots/upload.png" width="260">

---

## Document Library

<img src="screenshots/docs.png" width="260">

---

## AI Chat

<img src="screenshots/chats.png" width="260">

---

# 📂 Project Structure

## Flutter

```text
lib/
├── core/
├── features/
│   ├── auth/
│   ├── documents/
│   ├── upload/
│   └── chat/
├── routes/
└── main.dart
```

## Backend

```text
app/
├── crud/
├── models/
├── routers/
├── schemas/
├── services/
├── oauth2.py
├── database.py
└── main.py
```

---

# 🔄 Request Flow

```text
User

↓

JWT Authentication

↓

Upload PDF

↓

Extract Text

↓

Store Document

↓

Generate Embeddings

↓

Store Vector in PostgreSQL (pgvector)

↓

User asks a question

↓

Retrieve relevant document chunks

↓

Load previous chat history

↓

Send context + chat history to Gemini

↓

Store AI response

↓

Return answer
```

---

# 🔒 Authentication

Protected endpoints require a JWT access token.

```http
Authorization: Bearer <access_token>
```

---

# 🐳 Running with Docker

## Clone the repository

```bash
git clone https://github.com/rishab0615/ai-document-assistant.git
cd ai-document-assistant
```

## Create environment file

```bash
cp .env.example .env
```

Fill in your Gemini API key and other environment variables.

## Start everything

```bash
docker compose up --build
```

This starts:

- FastAPI Backend
- PostgreSQL
- pgvector
- Docker Network
- Persistent Docker Volume

Backend:

```
http://localhost:8000
```

Swagger:

```
http://localhost:8000/docs
```

---

# 💻 Running Without Docker

## Backend

```bash
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

alembic upgrade head

uvicorn app.main:app --reload
```

---

# 📱 Flutter Client

```bash
git clone https://github.com/rishab0615/doc-ai-flutter.git

cd doc-ai-flutter

flutter pub get

flutter run
```

---

# 🚀 Future Improvements

- Streaming AI Responses
- OCR Support
- Citation Support
- Multiple AI Providers
- Refresh Tokens
- Redis Caching
- Background Workers
- CI/CD Pipeline
- Kubernetes Deployment

---

# 👨‍💻 Author

**Rishab Sharma**

Software Engineer | Flutter • Python • FastAPI • AI Applications

**GitHub**

https://github.com/rishab0615

**Portfolio**

https://rishabsharma.web.app

**LinkedIn**

https://www.linkedin.com/in/rishab-sharma-3ba404235/