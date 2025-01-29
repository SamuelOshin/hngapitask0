# HNG Stage 0 - Public API

## Overview
This is a simple public API built using Django that returns basic information in JSON format as required for the HNG Internship Stage 0 task.

## Features
- Returns registered email address.
- Returns the current date and time in ISO 8601 format (UTC).
- Provides a link to the project's GitHub repository.
- Deployed on Render with CORS enabled.

## API Endpoint
- **URL:** `https://hngapitask.onrender.com/api/`
- **Method:** `GET`
- **Response Format:** JSON

### Example Response
```json
{
  "email": "samuelt.oshin@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/SamuelOshin/hngapitask0"
}
```

## Technologies Used
- **Backend Framework:** Django & Django REST Framework
- **Deployment:** Render
- **Database:** SQLite (for local development)
- **Production Server:** Gunicorn

## Installation & Setup
### Prerequisites
Ensure you have Python installed. Then, create a virtual environment and install dependencies.
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### Running Locally
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/api/` to test the API locally.

## Deployment on Render
1. Push the project to a public GitHub repository.
2. Create a new **Web Service** on [Render](https://render.com/).
3. Set the **Build Command**: `pip install -r requirements.txt`.
4. Set the **Start Command**: `gunicorn hngapitask0.wsgi`.
5. Deploy and retrieve the public URL.

## Links
- [Live API](https://hngapitask.onrender.com/api/)
- [GitHub Repository](https://github.com/SamuelOshin/hngapitask0)

## References
- [HNG Backend Developers](https://hng.tech/hire/python-developers)

