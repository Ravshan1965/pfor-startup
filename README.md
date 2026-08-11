## API Endpoints

| Method | Path | Description |
| :--- | :--- | :--- |
| **POST** | `/api/auth/register` | Register a new user |
| **POST** | `/api/auth/login` | Login and receive JWT token |
| **POST** | `/api/strategy/generate` | Generate a strategic report |
| **GET** | `/api/strategy/reports` | List reports for current user |

## Environment Variables

| Variable | Required | Description |
| :--- | :--- | :--- |
| **GEMINI_API_KEY** | No | Google Gemini API key. Falls back to mock if not set. |
| **SECRET_KEY** | No | JWT signing secret (defaults to a random key) |
| **DATABASE_URL** | No | SQLite URL (defaults to `sqlite:///./pfor_local.db`) |

## Tech Stack

* **Backend**: Python 3.11+, FastAPI, SQLAlchemy, Pydantic v2
* **Database**: SQLite (via SQLAlchemy ORM)
