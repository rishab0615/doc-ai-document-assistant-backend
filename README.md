# 📄 DocMind - AI Document Assistant


Backend API for **DocMind**, an AI-powered document assistant built with **FastAPI**, **PostgreSQL**, **Retrieval-Augmented Generation (RAG)** and **Google Gemini AI**.

The backend handles authentication, PDF upload & processing, document management, persistent chat history, Retrieval-Augmented Generation (RAG) and AI-powered question answering.

DocMind is a full-stack AI-powered document assistant that lets users upload PDF documents, extract their content, and ask natural language questions about them.

Built with **Flutter**, **FastAPI**, **PostgreSQL**, and **Google Gemini AI**.


---

## ✨ Features

- 📄 Upload PDF documents
- 🔍 Automatic text extraction
- 🤖 Ask questions about uploaded documents
- 💬 Persistent chat history
- 🧠 Context-aware conversations
- 🗑️ Delete documents with complete chat history
- 🔐 JWT Authentication
- 👤 User Registration & Login
- 📄 PDF Upload
- つ Retrieval-Augmented Generation (RAG)
- 📖 Automatic PDF Text Extraction
- 🤖 Google Gemini AI Integration
- 💬 Persistent Chat History
- 🧠 Conversation Memory
- 🗂️ Document Management
- 🗑️ Delete Documents & Chat History
- 🛡️ User-specific Data Isolation
- ⚡ RESTful APIs
- 🗄️ PostgreSQL Database

- 📱 Clean Flutter UI
- ⚡ FastAPI REST backend   
- 🗄 PostgreSQL database


---

## 🛠 Tech Stack

### Frontend
- Flutter
- GetX
- Dio
- Flutter Markdown

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- pgvector
- Alembic
- JWT Authentication

### AI
- Google Gemini API

---

# 📱 Screenshots

## Splash Screen

<img src="screenshots/splash.png" width="260">


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

## Project Structure

```
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

Backend

```
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

## Backend Features

- JWT Authentication
- Secure User Accounts
- PDF Upload
- Text Extraction
- Gemini AI Integration
- Conversation Memory
- Chat History
- PostgreSQL Storage
- REST APIs

---

## Future Improvements

- Vector embeddings (RAG)
- Semantic search
- Streaming AI responses
- Multiple AI providers
- Document summarization
- Citation support
- OCR for scanned PDFs

---

## Getting Started

### Frontend

```bash
git clone https://github.com/rishab0615/doc-ai-flutter.git

cd doc-ai-flutter

flutter pub get

flutter run
```

### Backend

```bash
git clone https://github.com/rishab0615/doc-ai-document-assistant-backend.git

cd doc-ai-document-assistant-backend

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

alembic upgrade head

uvicorn app.main:app --reload
```

---

<<<<<<< HEAD
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

Store in PostgreSQL

↓

Ask Question

↓

Load Previous Chat History

↓

Send Context + Document to Gemini

↓

Store AI Response

↓

Return Answer
```

---

# 🔒 Authentication

Protected endpoints require a JWT access token.

```
Authorization: Bearer <access_token>
```

---

# 🚀 Future Improvements

- Refresh Tokens
- Streaming AI Responses
- OCR Support
- Multiple AI Providers
- Docker
- CI/CD
- Unit Tests

---

# 📱 Frontend

Flutter Client

https://github.com/rishab0615/doc-ai-flutter

---
## Author
>>>>>>> a297bf4 (created dockerized containers for this app)

**Rishab Sharma**

Flutter Developer

GitHub:
https://github.com/rishab0615

Portfolio:
https://rishabsharma.web.app

LinkedIn:
https://www.linkedin.com/in/rishab-sharma-3ba404235/
>>>>>>> a297bf4 (created dockerized containers for this app)
