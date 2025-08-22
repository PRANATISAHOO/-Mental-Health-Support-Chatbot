from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

resources = {
    "anxiety": "https://www.helpguide.org/articles/anxiety/anxiety-disorders-and-anxiety-attacks.htm",
    "depression": "https://www.helpguide.org/articles/depression/coping-with-depression.htm",
    "support": "https://www.mentalhealth.gov/get-help",
    "emergency": "Call the National Suicide Prevention Lifeline: 988 (USA)"
}

def generate_response(message):
    msg = message.lower()
    if "suicide" in msg or "suicidal" in msg or "end my life" in msg:
        return ("I'm really sorry you're feeling this way. "
                "Please know that you're not alone and there is help available. "
                f"{resources['emergency']}")
    elif "anxiety" in msg:
        return ("It sounds like you're experiencing anxiety. "
                "Here's a helpful resource: " + resources["anxiety"])
    elif "depression" in msg or "sad" in msg:
        return ("I'm sorry you're feeling down. "
                "Here's some information that might help: " + resources["depression"])
    elif "help" in msg or "support" in msg:
        return ("You can find mental health support here: " + resources["support"])
    else:
        return ("Thank you for sharing with me. Remember, it's okay to ask for help. "
                "Would you like some resources or to talk more?")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = generate_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000)
