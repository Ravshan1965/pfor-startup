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
