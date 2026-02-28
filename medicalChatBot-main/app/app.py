import os
from flask import Flask, render_template, request, jsonify
from app.MedQuard import load_model_and_tokenizer, answer_query

app = Flask(__name__)

# ── Lazy model loading ────────────────────────────────────────────────────────
model = None
tokenizer = None

def get_model():
    global model, tokenizer
    if model is None:
        print("Loading model... this may take a moment.")
        model, tokenizer = load_model_and_tokenizer(
            os.environ.get("MODEL_PATH", "gpt2")
        )
        print("Model loaded successfully.")
    return model, tokenizer

# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/health")
def health():
    return "ok", 200

@app.route("/ask", methods=["POST"])
def ask():
    model, tokenizer = get_model()

    data = request.get_json(silent=True) or request.form
    question = data.get("question", "").strip()

    if not question:
        return jsonify(error="Question cannot be empty."), 400

    try:
        response = answer_query(model, tokenizer, question)
        return jsonify(answer=response)
    except Exception as e:
        app.logger.error(f"Error answering query: {e}")
        return jsonify(error="An internal error occurred. Please try again."), 500

# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)