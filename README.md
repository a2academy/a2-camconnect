# Cam Connect (Django)

Web prototype for **Cam Connect**: a four-step guided workflow to explore multi-brand camera requirements, run a **compatibility engine** against a mock manufacturer matrix, and preview a **unified dashboard**. The UI follows the design brief: **blue theme** with **crisp black outlines** on cards and controls.

## What’s included

1. **Welcome** — Introduction and “Start Builder”.
2. **Feature overview** — Toggle requirements across video, night vision, AI, motion/zones, storage, connectivity, audio, smart home, performance, and privacy (aligned with the product document).
3. **Compatible brands** — Filtered brand cards with **Fully compatible**, **Partial support**, or **Requires bridge** (demo logic in `workflow/compatibility.py`).
4. **Unified dashboard preview** — Mock grid, alerts, timeline, integrations, and edge AI copy; optionally driven by brands you tick on step 3.

Selections are stored in the **session** so you can move between steps without a database for app data.

## Requirements

- Python **3.10+** (3.11 or 3.12 recommended)
- pip

## How to run locally

From the project root (`a2-camconnect`):

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

Use **Reset session** in the nav bar to clear chosen features.

## Production notes

- Change `SECRET_KEY` and set `DEBUG = False` in `camconnect/settings.py`.
- Configure `ALLOWED_HOSTS` and serve static files with your reverse proxy or `collectstatic`.

## Project layout

| Path | Purpose |
|------|--------|
| `camconnect/settings.py` | Django settings |
| `workflow/views.py` | Step views and session handling |
| `workflow/compatibility.py` | Feature definitions, brand matrix, compatibility engine |
| `workflow/templates/workflow/` | HTML templates |
| `static/css/style.css` | Blue / black-outline styling |
