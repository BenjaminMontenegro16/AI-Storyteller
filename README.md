# 📖 AI Storyteller CLI

A command-line storyteller powered by **Groq** and **LLaMA 3.3 70B**. Just describe what you want and get an AI-generated story instantly.

---

## 🚀 Features

- 🤖 Uses Groq's ultra-fast inference with LLaMA 3.3 70B
- 💬 Simple interactive CLI — just type and go
- 🔒 API key managed securely via `.env`

---

## 📦 Requirements

- Python 3.8+
- A [Groq API key](https://console.groq.com/)

---

## ⚙️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/ai-storyteller-cli
   cd ai-storyteller-cli
   ```

2. **Install dependencies**
   ```bash
   pip install groq python-dotenv
   ```

3. **Set up your `.env` file**
   ```
   GROQ_API_KEY=your_api_key_here
   ```

---

## ▶️ Usage

```bash
python storyteller.py
```

Then just type what you want your story to be about:

```
Make a story about: a lonely astronaut who finds a dog on Mars
AI: Chapter 1 — The Red Desert...
```

Type `exit` to quit.

---

## 📁 Project Structure

```
ai-storyteller-cli/
├── storyteller.py   # Main script
├── .env             # Your API key (never commit this!)
├── .gitignore       # Make sure .env is in here!
└── README.md
```

---

## 🛡️ Important

Make sure your `.gitignore` includes:
```
.env
```
**Never push your API key to GitHub.** 🔑

---

## 🧠 Model Used

| Model | Provider | Speed |
|---|---|---|
| `llama-3.3-70b-versatile` | Groq | ⚡ Ultra-fast |

---

## 📄 License

MIT — do whatever you want with it.
