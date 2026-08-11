# PFOR: Operational Solutions Platform

## Multi-Agent Pipeline

A single **Google Gemini** model (`gemini-1.5-flash`) is used with four distinct role-based prompts executed sequentially:

| Agent | Role |
| :--- | :--- |
| **Director** | Strategic goals and solution concept |
| **Marketer** | Positioning, sales funnels, acquisition channels |
| **Financier** | Unit economics, budget, financial risks |
| **Editor** | Consolidates all outputs into a 5-page structured report |

If `GEMINI_API_KEY` is not set, the system falls back to a **Mock Generator** that produces a realistic sample report so the UI is always functional.

## Quick Start

### 1. Clone the repository
```bash
git clone [https://github.com/Ravshan1965/pfor-startup.git](https://github.com/Ravshan1965/pfor-startup.git)
cd pfor-startup
2. Create virtual environment and install dependencies

python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
3. Configure environment (optional)
# Copy the example env file and add your Gemini API key
cp .env.example .env
# Edit .env and set GEMINI_API_KEY=your_key_here
4. Run the backend
cd src
uvicorn pfor.main:app --reload --port 8000
Method,Path,Description
POST,/api/auth/register,Register a new user
POST,/api/auth/login,Login and receive JWT token
POST,/api/strategy/generate,Generate a strategic report
GET,/api/strategy/reports,List reports for current user

Variable,Required,Description
GEMINI_API_KEY,No,Google Gemini API key. Falls back to mock if not set.
SECRET_KEY,No,JWT signing secret (defaults to a random key)
DATABASE_URL,No,SQLite URL (defaults to sqlite:///./pfor_local.db)
Variable,Required,Description
GEMINI_API_KEY,No,Google Gemini API key. Falls back to mock if not set.
SECRET_KEY,No,JWT signing secret (defaults to a random key)
DATABASE_URL,No,SQLite URL (defaults to sqlite:///./pfor_local.db)























































