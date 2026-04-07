# 🤖 ARIA — AI Rule-Based Chatbot

A command-line AI chatbot built in Python that understands natural language patterns and responds intelligently — no external APIs required.

## 📸 Preview

```
==================================================
         🤖 ARIA — AI Chatbot v1.0
==================================================
  Type 'bye' to exit

You: hello
ARIA: Hey! How can I help you today?

You: tell me about cybersecurity
ARIA: Cybersecurity is all about protecting systems and data from attacks.

You: what time is it?
ARIA: The current time is 10:45 PM.

You: tell me a joke
ARIA: Why do programmers prefer dark mode? Because light attracts bugs! 🐛

You: bye
ARIA: Goodbye! Stay curious. 👋
```

## ⚙️ Features

- Natural language keyword matching
- 12 conversation categories (greetings, AI, cybersecurity, Python, jokes, and more)
- Real-time clock and date responses
- Random reply variation — doesn't feel repetitive
- Zero dependencies — runs on pure Python 3

## 🚀 How to Run

```bash
git clone https://github.com/yaqout-com1/aria-chatbot
cd aria-chatbot
python chatbot.py
```

No installations needed. Just Python 3.

## 🧠 How It Works

ARIA uses a **rule-based NLP approach**:

1. User input is converted to lowercase
2. Keywords are matched against a knowledge base
3. A random reply is selected from matching category
4. Dynamic responses (time/date) are generated live

| Category | Example Trigger |
|---|---|
| Greetings | "hello", "hey", "hi" |
| AI & ML | "machine learning", "neural network" |
| Cybersecurity | "hacking", "encryption", "password" |
| Jokes | "joke", "funny", "make me laugh" |
| Motivation | "tired", "give up", "inspire me" |
| Time & Date | "what time", "what day is today" |

## 📁 Project Structure

```
aria-chatbot/
│
├── chatbot.py    # Main chatbot script
└── README.md     # Project documentation
```

## 🛡️ AI Concepts Covered

- Rule-based Natural Language Processing (NLP)
- Keyword extraction and intent matching
- Response randomization
- Conversational state handling

## 👤 Author

**Alexander (Mo Rashad)**  
Interested in AI, cybersecurity, and building practical tools.  
[GitHub Profile](https://github.com/yaqout-com1)

---

> *"Intelligence is the ability to adapt to change."* — Stephen Hawking
