from flask import Flask, request, jsonify
from services.gemini_api import generate_response
from utils.prompts import mood_prompt, crisis_prompt, summarize_prompt

app = Flask(__name__)

@app.route("/analyze_mood", methods=["POST"])
def analyze_mood():
    data = request.get_json()
    text = data.get("text", "")
    result = generate_response(mood_prompt(text))
    return jsonify({"emotion": result})

@app.route("/detect_crisis", methods=["POST"])
def detect_crisis():
    data = request.get_json()
    text = data.get("text", "")
    result = generate_response(crisis_prompt(text))
    result = result.lower().strip()
    return jsonify({"crisis_detected": result == "true"})

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data.get("text", "")
    result = generate_response(summarize_prompt(text))
    return jsonify({"summary": result})

if __name__ == "__main__":
    app.run(debug=True)
