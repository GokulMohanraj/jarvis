# JARVIS Prototype 🚀

A local-first AI assistant inspired by Ironman JARVIS.

## 🎯 Goal

Build a private offline AI assistant that can:
- Run local LLMs
- Work without internet
- Control applications
- Search local files
- Support voice interaction
- Automate tasks

---

# 🛠️ Tech Stack

- Python
- FastAPI
- Ollama
- Docker
- Git

---

# 📂 Project Structure

```text
jarvis/
│
├── api/
├── brain/
├── voice/
├── automation/
├── memory/
├── search/
├── ui/
├── config/
├── logs/
├── data/
├── docs/
│   └── progress/
│       ├── day-01.md
│       ├── day-02.md
│       └── ...
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ✅ Current Features

- Local AI integration using Ollama
- FastAPI backend
- Chat API endpoint
- Modular architecture
- Config-based settings
- Local LLM communication

---

# 🧠 Tested Local Models

```bash
ollama run phi4
```

```bash
ollama run llama3
```

---

# ⚙️ Run Backend

```bash
uvicorn api.main:app --reload
```

API Docs:

```text
http://127.0.0.1:8000/docs
```

---

# 🔥 Available API

## POST `/chat`

Example request:

```json
{
  "message": "Hello Jarvis"
}
```

---

# 📅 Progress Tracking

Detailed daily progress is maintained inside:

```text
docs/progress/
```

---

# 📈 Progress

```text
Day 2 / 30 ✅
```

---

# 🔒 Design Principles

- Local-first
- Offline capable
- Privacy focused
- Modular architecture

---

# 👨‍💻 Author

Gokul