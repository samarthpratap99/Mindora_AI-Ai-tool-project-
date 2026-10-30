# Mindora AI – Intelligent Chatbot Using Google Gemini API

Mindora AI is an AI-powered chatbot web application developed using **Python, Flask, HTML, CSS, JavaScript, and Google Gemini API**. It provides an interactive interface where users can ask questions, learn new concepts, generate code, and get AI-powered responses.

## 1. Project Overview

Mindora AI is designed to provide a simple and user-friendly chatbot experience. It uses Google's Gemini API to generate responses to user messages.

### Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **AI Model:** Google Gemini API
- **Environment Management:** Python Virtual Environment
- **API Key Security:** Python dotenv

## 2. Features

- AI-powered real-time chat.
- User-friendly ChatGPT-style interface.
- New chat creation.
- Multiple chat history stored in browser local storage.
- Python and programming assistance.
- Project ideas and educational explanations.
- Responsive chatbot interface.
- Secure API key configuration using `.env`.

## 3. Project Structure

```text
Mindora_AI/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## 4. Requirements

Before running the project, install:

- Python 3.10 or later
- Visual Studio Code
- Internet connection
- Google Gemini API key

## 5. Installation and Setup

### Step 1: Open the project

Open the Mindora AI project folder in Visual Studio Code.

### Step 2: Create a virtual environment

Open the VS Code terminal and execute:

```powershell
py -m venv .venv
```

### Step 3: Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

```powershell
py -m pip install -r requirements.txt
```

### Step 5: Configure the Gemini API key

Create a `.env` file in the main project folder and add:

```env
GEMINI_API_KEY=YOUR_NEW_GEMINI_API_KEY
GEMINI_MODEL=gemini-3.8-flash
```

Replace `YOUR_NEW_GEMINI_API_KEY` with your own valid API key.

Get your API key from:

https://aistudio.google.com/app/apikey

**Important:** Never share your API key publicly or upload your `.env` file to GitHub.

### Step 6: Run the application

Execute:

```powershell
py app.py
```

### Step 7: Open in browser

Visit:

```text
http://127.0.0.1:5000
```

Mindora AI will now be available in your browser.

## 6. How the Project Works

1. The user enters a message in the chatbot interface.
2. JavaScript sends the message to the Flask backend.
3. Flask receives the request through the `/api/chat` endpoint.
4. The backend sends the conversation to the Google Gemini API.
5. Gemini generates an AI response.
6. Flask returns the response to the frontend.
7. JavaScript displays the response in the chatbot interface.

## 7. API Endpoint

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Loads the chatbot homepage |
| POST | `/api/chat` | Sends messages to Gemini and receives AI responses |

## 8. Troubleshooting

**Problem: Python is not recognized**

Try:

```powershell
py --version
```

**Problem: Module not found**

Install the dependencies again:

```powershell
py -m pip install -r requirements.txt
```

**Problem: Gemini API key missing**

Check whether the `.env` file exists in the main project folder and contains a valid API key.

**Problem: 503 UNAVAILABLE**

This means the Gemini model may be experiencing high demand. Wait for some time and retry the request.

**Problem: Application is not opening**

Make sure Flask is running and open:

```text
http://127.0.0.1:5000
```

## 9. Security

- API keys are stored in the `.env` file.
- The `.env` file should not be uploaded to GitHub.
- The `.gitignore` file excludes sensitive environment files.
- API requests are handled through the Flask backend.

## 10. Future Enhancements

- User registration and login.
- Database-based chat history.
- Voice input and output.
- Image understanding.
- File upload and analysis.
- Improved mobile responsiveness.

## 11. Conclusion

Mindora AI demonstrates how artificial intelligence can be integrated into a web application using Python, Flask, and the Google Gemini API. It provides an interactive platform for learning, coding assistance, and general question answering. This project also provides practical experience in frontend development, backend programming, API integration, and secure configuration management.

---

**Project Name:** Mindora AI  
**Project Type:** AI-Powered Web Chatbot  
**Developed Using:** Python, Flask, HTML, CSS, JavaScript, and Google Gemini API
