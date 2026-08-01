# 📄 DocMind - AI Document Assistant

DocMind is a full-stack AI-powered document assistant that allows users to upload PDF documents, extract their content, and ask natural language questions using **Google Gemini AI**.

The backend is built with **FastAPI**, **PostgreSQL (pgvector)**, and **Retrieval-Augmented Generation (RAG)**, while the frontend is built with **Flutter**.

---

# ✨ Features

- 👤 User Registration & Login
- 🔐 JWT Authentication
- 📄 PDF Upload
- 📖 Automatic PDF Text Extraction
- 🤖 Google Gemini AI Integration
- 🧠 Retrieval-Augmented Generation (RAG)
- 🧬 Gemini Embedding API
- 🔍 Semantic Search using pgvector
- 💬 Persistent Chat History
- 🗂️ Document Management
- 🗑️ Delete Documents & Associated Chat History
- 🛡️ User-specific Data Isolation
- ⚡ RESTful APIs
- 🗄️ PostgreSQL Database
- 🐳 Docker & Docker Compose Support

---

# 🏗️ Architecture

```text
                PDF Upload
                     │
                     ▼
          Extract Text (PyMuPDF)
                     │
                     ▼
             Text Chunking
                     │
                     ▼
      Generate Gemini Embeddings
                     │
                     ▼
      PostgreSQL + pgvector Storage
                     │
                     ▼
         Semantic Similarity Search
                     │
                     ▼
          Relevant Document Chunks
                     │
                     ▼
      Previous Conversation History
                     │
                     ▼
             Google Gemini AI
                     │
                     ▼
              AI Generated Answer
```

---

# 🛠 Tech Stack

## Frontend

- Flutter
- GetX
- Dio
- Flutter Markdown
- Flutter Secure Storage

## Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- pgvector
- Alembic
- PyMuPDF
- JWT Authentication
- Docker
- Docker Compose

## AI

- Google Gemini API
- Gemini Embedding API
- Retrieval-Augmented Generation (RAG)
- Semantic Search

## Deployment

- Render
- Neon PostgreSQL

---

# 📱 Screenshots

## Swagger API

<img src="screenshots/swagger.png" width="900">

---

# 📂 Project Structure

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
├── config.py
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

Extract Text (PyMuPDF)

↓

Chunk Document

↓

Generate Gemini Embeddings

↓

Store Embeddings in PostgreSQL (pgvector)

↓

User asks a question

↓

Similarity Search

↓

Retrieve Relevant Chunks

↓

Load Previous Chat History

↓

Send Context + Chat History to Gemini

↓

Store AI Response

↓

Return Answer
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

Fill in the required environment variables:

```env
DB_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080
GEMINI_API_KEY=your_gemini_api_key
```

## Start the application

```bash
docker compose up --build
```

Services started:

- FastAPI Backend
- PostgreSQL
- pgvector
- Docker Network
- Persistent Docker Volume

Backend:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

---

# 💻 Running Without Docker

```bash
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

alembic upgrade head

uvicorn app.main:app --reload
```

Backend:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

---

# 🚀 Future Improvements

- Streaming AI Responses
- OCR Support for Scanned PDFs
- Citation Support
- Multi-document Conversations
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

**LinkedIn**

https://www.linkedin.com/in/rishab-sharma-3ba404235/