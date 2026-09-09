# Farm Korret Nig. — Python Web App

Premium agribusiness landing page for **Farm Korret Nig.** (RC-8163754).

Covers: Farm Produce · Livestock · Heavy Equipment · Veterinary Health · Farm Finance.

## Quick start

```bash
cd farm_korret
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5000**

## Project structure

```
farm_korret/
├── app.py                 # Flask application
├── requirements.txt
├── README.md
├── templates/
│   └── index.html         # Landing page
└── static/
    ├── styles.css         # Full theme
    ├── app.js             # Preloader, filters, cart, form
    └── logo.svg           # Brand mark
```

## Features

- Animated preloader and hero counters
- Responsive navigation (desktop + mobile)
- Produce catalogue with category filters and add-to-cart
- Livestock, equipment, vet health, and finance sections
- Contact form that posts to `/api/enquiry`
- Cart drawer with quantity controls
- Toast notifications

## API endpoints

| Method | Path            | Description                    |
|--------|-----------------|--------------------------------|
| GET    | `/`             | Landing page                   |
| POST   | `/api/enquiry`  | Submit contact / order enquiry |
| GET    | `/api/enquiries`| List stored enquiries (demo)   |
| GET    | `/health`       | Health check                   |

## Production notes

- Change `SECRET_KEY` and disable `debug=True`
- Persist enquiries to a database
- Wire email / WhatsApp notifications on new enquiries
- Serve behind gunicorn or similar: `gunicorn -b 0.0.0.0:5000 app:app`
