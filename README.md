# Welcome to Regulate!

## Mission

Regulate is a web application that aims to help students build awareness of their stress levels and emotional wellbeing through quick daily check-ins, guided regulation exercises, and simple mood tracking tools.

---

## Project Overview

### Core Features (MVP Scope)
- Daily stress and mood check-in
- Tag-based emotional context
- Text reflection entry
- Guided regulation exercises
- Simple stress trend visualization

### Possible Additional Features
- Notifications
- AI-generated recommendations
- Social or sharing features
- Advanced analytics

---

## Project Management
- GitHub Issues for task tracking (sub-issues for longer tasks, detailed descriptions)
- GitHub Projects board for sprint planning and progress tracking
- Feature branches and pull requests required for contributions

Access and update the [Implementation Notes](https://docs.google.com/document/d/1vJt76NYQJLlQYggZ6SYqf23zeZDy0l3jy1elNEogdxA/edit?usp=sharing)

---

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python (FastAPI)

### Database
- SQLite

---

## Repository Structure

```
regulate/
├── README.md
├── html/
│   ├── index.html
│   ├── checkin.html
|   ├── exercises.html
|   ├── journals.html     ** not created yet **
│   └── charts.html       ** not created yet **
|    
├── css/
│   ├── template.css
│   ├── checkin.css
│   └── exercises.css
└── js/
    ├── checkin.js
    └── exercises.js
```

### Directory Overview

| Path | Purpose |
|--------|---------|
| `html/` | Frontend pages |
| `css/` | Stylesheets for each page |
| `js/` | Client-side JavaScript |
| `README.md` | Project documentation |


### Current Pages

| File | Description |
|--------|---------|
| `index.html` | Home page |
| `checkin.html` | Daily wellness check-in |
| `exercises.html` | Guided breathing and grounding exercises |
| `checkin.js` | Check-in page functionality |
| `exercises.js` | Exercise carousel functionality |

---
## Planned Future Structure

```
regulate/
├── frontend/
│   ├── html/
│   ├── css/
│   └── js/
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── routes/
│       ├── checkin.py
│       ├── journal.py
│       └── charts.py
└── database/
    └── regulate.db
```

### Planned Backend Components

| File | Purpose |
|--------|---------|
| `main.py` | FastAPI application entry point |
| `database.py` | SQLite connection management |
| `models.py` | Data models and schemas |
| `routes/checkin.py` | Check-in API endpoints |
| `routes/journal.py` | Journal API endpoints |
| `routes/charts.py` | Charts and analytics endpoints |
---

## Current Status (Summer 2026)

Completed:
- Project structure established
- Check-In UI
- Guided Exercises page
- Project management board
- Documentation and onboarding notes

Planned:
- Journal page
- Charts page
- FastAPI backend
- SQLite integration

Current Team Roles Needed:
- Frontend Developers
- Backend Developers
- UI/UX Designers

---

## Getting Started

### 1. Clone the Repository

```
git clone https://github.com/Project-Code-Regulate/regulate.git
cd regulate
```

### 2. Open the Project

Using VS Code:

```
code .
```

### 3. Run the Frontend

The frontend website can be opened by running:

```
python3 -m http.server 8000
```
in your terminal. Then enter this link in your browser:

```
http://localhost:8000/html/index.html
```

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
