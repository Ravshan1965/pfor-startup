import requests
from flask import Flask, request, jsonify
from config import API_KEY, MODEL_NAME

app = Flask(__name__)

# Полный набор ролей из материалов Даурена
SYSTEM_ROLES = (
    "Ты — мультиагентная система платформы ПФОР. "
    "Обработай задачу, задействуя следующие роли: "
    "1. Директор (определяет глобальную цель и стратегию). "
    "2. Замдиректор (разбивает задачу на пошаговый план). "
    "3. Таргетолог (прописывает маркетинговые инструменты и конверсии). "
    "4. Критик (проводит жесткий аудит плана, находит слабые места, риски и архитектурные ошибки). "
    "Выдай итоговый структурированный отчет с учетом правок критика."
)

@app.route('/api/ask', methods=['POST'])
def ask_cloud():
    user_data = request.json
    user_prompt = user_data.get("text", "")
    
    if not user_prompt:
        return jsonify({"error": "Пустой запрос"}), 400

    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    payload = {
        "model": MODEL_NAME,
        "max_tokens": 2048,
        "system": SYSTEM_ROLES,
        "messages": [{"role": "user", "content": user_prompt}]
    }
    
    response = requests.post(url, json=payload, headers=headers)
    result = response.json()
    ai_answer = result["content"][0]["text"]
    return jsonify({"response": ai_answer})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
@app.route('/')
def home():
    return "PFOR Platform is running!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
