# Stress & Mood Check-In App

A web application designed to support daily stress and mood awareness through quick check-ins, guided regulation exercises, reflections, and simple trend visualization.

This project is currently in early development. Week 1 focuses on wireframes, UI/UX design, and building the frontend backbone using HTML, CSS, and JavaScript.

---

## Project Overview

### Core Features (MVP Scope)
- Daily stress/mood check-in (1–5 scale)
- Tag-based emotional context
- Text reflection entry
- Guided regulation exercises (box breathing, 5-4-3-2-1 grounding, short body scans)
- Simple stress trend visualization

### Out of Scope (Current Phase)
- Notifications
- AI-generated recommendations
- Social or sharing features
- Advanced analytics

---

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend (Planned)
- Python (FastAPI)

### Database (Planned)
- SQLite or Firebase

---

## Repository Structure

```
project-name/
│
├── frontend/
│   ├── css/
│   ├── js/
│   ├── components/
│   ├── index.html
│   ├── checkin.html
│   ├── exercises.html
│   └── trends.html
│
├── backend/
│
└── README.md
```

---

## Getting Started

### 1. Clone the Repository

```
git clone https://github.com/your-org/project-name.git
cd project-name
```

### 2. Open the Project

Using VS Code:

```
code .
```

### 3. Run the Frontend

During Week 1 development, the frontend can be run by opening:

```
frontend/index.html
```

in your browser.

Backend setup instructions will be added in later phases.

---

## Development Workflow

### Branching Rules

Do **not** commit directly to `main`.

Create a feature branch for all work:

```
git checkout -b feature/feature-name
```

Example:

```
git checkout -b feature/checkin-ui
```

After making changes:

```
git add .
git commit -m "Describe your change"
git push origin feature/feature-name
```

Open a Pull Request for review before merging.

---
## Contributing

1. Pull latest changes before starting work.
2. Create a new feature branch.
3. Keep commits focused and descriptive.
4. Open a Pull Request for review.

---
