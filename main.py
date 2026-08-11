import requests
from flask import Flask, request, jsonify
from config import API_KEY, MODEL_NAME

app = Flask(__name__)

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
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": user_prompt}]
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        result = response.json()
        ai_answer = result["content"][0]["text"]
        return jsonify({"response": ai_answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
