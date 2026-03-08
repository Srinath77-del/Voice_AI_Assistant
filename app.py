from flask import Flask, render_template, request, jsonify
import llm

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    text = request.json["message"]
    reply = llm.generate_response(text)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)