# -Mental-Health-Support-Chatbot
This is a simple web-based chatbot designed to provide basic mental health support, resource suggestions, and emergency escalation.

## Features

- Anonymous chat
- Supportive, empathetic responses
- Resource suggestions (articles, hotlines)
- Emergency escalation for crisis keywords

## Getting Started

1. **Install dependencies:**
   ```
   pip install flask flask-cors
   ```

2. **Run the server:**
   ```
   python app.py
   ```

3. **Open `index.html` in your browser.**
   - For local testing, you may need to serve `index.html` with a local web server (e.g., via VS Code Live Server or Python’s `http.server`).

## How It Works

- The chat UI sends user messages to the Flask backend.
- The backend processes the message, detects keywords, and responds empathetically.
- If crisis keywords are detected, the bot suggests emergency resources.

## How to Expand

- Integrate a smarter NLP model for more natural conversation.
- Connect to a database for anonymous chat logs or analytics.
- Add more resources or support for multiple languages.
- Improve the user interface and accessibility.
