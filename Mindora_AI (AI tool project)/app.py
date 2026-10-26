import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from google import genai
from google.genai import types

load_dotenv()

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 64 * 1024

API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash").strip()

client = genai.Client(api_key=API_KEY) if API_KEY else None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    if client is None:
        return jsonify({
            "error": "API key missing. Add GEMINI_API_KEY to your .env file."
        }), 500

    data = request.get_json(silent=True) or {}
    messages = data.get("messages", [])

    if not isinstance(messages, list) or not messages:
        return jsonify({"error": "Please enter a message."}), 400

    contents = []

    for message in messages[-20:]:
        if not isinstance(message, dict):
            return jsonify({"error": "Invalid message format."}), 400

        role = message.get("role")
        content = message.get("content", "")

        if role not in ("user", "model") or not isinstance(content, str):
            return jsonify({"error": "Invalid message format."}), 400

        content = content.strip()

        if not content:
            continue

        contents.append(
            types.Content(
                role=role,
                parts=[types.Part(text=content[:4000])]
            )
        )

    if not contents or contents[-1].role != "user":
        return jsonify({"error": "Your latest message is missing."}), 400

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=(
                    "You are Mindora AI, a helpful and friendly AI assistant. "
                    "Answer clearly and accurately. "
                    "Use the same language as the user. "
                    "Explain things simply when appropriate."
                ),
                temperature=0.7,
                max_output_tokens=2048
            )
        )

        answer = response.text

        if not answer:
            return jsonify({
                "error": "AI returned an empty response. Please try again."
            }), 502

        return jsonify({"reply": answer})

    except Exception as error:
        print(f"Gemini API error: {type(error).__name__}: {error}")

        return jsonify({
            "error": (
                f"Gemini request failed ({type(error).__name__}). "
                "Check the VS Code terminal for details."
            )
        }), 502


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
