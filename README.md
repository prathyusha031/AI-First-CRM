# AI-First CRM – HCP Interaction Module

An AI-powered Healthcare CRM application that enables pharmaceutical field representatives to log Healthcare Professional (HCP) interactions using natural language. The application automatically extracts structured CRM data through a LangGraph-powered AI agent and populates the interaction form without manual data entry.

This project was developed as part of an AI-First CRM technical assessment.

---

# Features

## AI-Driven Interaction Logging

- Log HCP interactions using natural language.
- AI extracts structured CRM information automatically.
- Form fields are populated without manual editing.

Extracted fields include:

- HCP Name
- Interaction Type
- Date
- Time
- Attendees
- Topics Discussed
- Materials Shared
- Samples Distributed
- Sentiment
- Outcomes
- Follow-up Actions

---

## LangGraph AI Agent

The backend uses LangGraph to orchestrate AI workflows.

Implemented tools:

1. Log Interaction
   - Converts natural language into structured CRM JSON.

2. Edit Interaction
   - Updates selected interaction fields.

3. Search HCP History
   - Retrieves previous interaction information.

4. Generate Follow-up Suggestions
   - Generates recommended next actions.

5. Generate CRM Summary
   - Produces concise interaction summaries.

---

# Tech Stack

## Frontend

- React (Vite)
- Redux Toolkit
- React Router
- Axios
- CSS
- Google Inter Font

---

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic

---

## AI

- LangGraph
- LangChain
- Groq API
- Llama-3.3-70B-Versatile

---

# Project Architecture

```
User
        │
        ▼
React UI
        │
        ▼
Redux Store
        │
        ▼
FastAPI Backend
        │
        ▼
LangGraph Agent
        │
        ▼
Groq LLM
        │
        ▼
Structured JSON
        │
        ▼
PostgreSQL
        │
        ▼
Redux Store
        │
        ▼
Auto-populated CRM Form
```

---

# Project Structure

```
AI-First-CRM/

├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── redux/
│   │   ├── services/
│   │   ├── styles/
│   │   └── App.jsx
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── database/
│   │   ├── models/
│   │   ├── routers/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── graph.py
│   │   └── main.py
│   └── requirements.txt
│
└── README.md
```

---

# Database

The application uses PostgreSQL with SQLAlchemy ORM.

Tables include:

- HCP
- Interactions
- Materials
- Samples
- Follow-ups

Relationships are maintained between HCPs and their interaction records.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/prathyusha031/AI-First-CRM.git

cd AI-First-CRM
```

---

# Backend Setup

Navigate to backend.

```bash
cd backend
```

Create virtual environment.

```bash
python -m venv venv
```

Activate environment.

Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```
GROQ_API_KEY=your_api_key
DATABASE_URL=your_postgresql_connection_string
```

Run backend.

```bash
uvicorn app.main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

Swagger API

```
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

Open another terminal.

```bash
cd frontend
```

Install packages.

```bash
npm install
```

Run development server.

```bash
npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

# Example Interaction

Input

```
Met Dr. Sharma on 2024-04-16 at 2 PM.

Discussed Product X.

Shared one brochure and one sample.

Doctor was positive.

Outcome: Doctor agreed to try Product X.

Follow up on 2024-04-23.
```

Automatically Extracted

- HCP Name
- Meeting
- Date
- Time
- Topics
- Materials
- Samples
- Sentiment
- Outcomes
- Follow-up

The interaction form updates automatically through Redux.

---

# AI Workflow

1. User enters natural language.
2. Request is sent to FastAPI.
3. LangGraph selects the appropriate tool.
4. Groq LLM processes the request.
5. Structured JSON is returned.
6. Data is stored in PostgreSQL.
7. Redux updates the application state.
8. CRM form refreshes automatically.

---

# Screens Included

- AI Chat Assistant
- HCP Interaction Form
- Automatic CRM Population
- LangGraph AI Processing
- PostgreSQL Storage
- Five AI Tools

---

# Future Improvements

- Voice interaction support
- Database-backed HCP history retrieval
- Calendar integration for follow-ups
- Authentication and role-based access
- Multi-user CRM collaboration
- Advanced analytics dashboard

---

# Author

**Bailapudi Prathyusha**

GitHub

https://github.com/prathyusha031

LinkedIn

https://www.linkedin.com/in/bailapudiprathyusha

---

# Assignment Summary

This project demonstrates an AI-First CRM workflow where conversational AI replaces manual CRM data entry. By integrating React, Redux, FastAPI, PostgreSQL, LangGraph, LangChain, and Groq LLM, the application automatically converts natural language interactions into structured CRM records, providing an efficient and production-oriented healthcare CRM experience.
