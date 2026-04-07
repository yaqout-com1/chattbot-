import random
import datetime
import json
import os

# ─────────────────────────────────────────
#  Knowledge Base (built-in)
# ─────────────────────────────────────────

MEMORY_FILE = "memory.json"

built_in = {
    "greetings": {
        "keywords": ["hello", "hi", "hey", "sup", "greetings", "good morning", "good evening"],
        "replies": [
            "Hey! How can I help you today?",
            "Hello! What's on your mind?",
            "Hi there! Ask me anything.",
        ]
    },
    "farewell": {
        "keywords": ["bye", "goodbye", "see you", "cya", "later", "quit", "exit"],
        "replies": [
            "Goodbye! Stay curious. 👋",
            "See you later!",
            "Take care!",
        ]
    },
    "how_are_you": {
        "keywords": ["how are you", "how r u", "you okay", "you good", "how do you feel"],
        "replies": [
            "I'm just code, but I'm running great! 😄",
            "Doing well, thanks for asking!",
        ]
    },
    "name": {
        "keywords": ["your name", "who are you", "what are you", "what's your name"],
        "replies": [
            "I'm ARIA — Automated Response & Information Assistant.",
        ]
    },
    "creator": {
        "keywords": ["who made you", "who created you", "your creator", "who built you"],
        "replies": [
            "I was built by Mo Rashad — a developer interested in AI and cybersecurity.",
        ]
    },
    "ai": {
        "keywords": ["artificial intelligence", "machine learning", "deep learning", "neural network", "ai"],
        "replies": [
            "AI is fascinating! It's the science of making machines think and learn.",
            "Machine learning is a subset of AI where systems learn from data.",
        ]
    },
    "cybersecurity": {
        "keywords": ["cybersecurity", "hacking", "security", "password", "encryption", "firewall"],
        "replies": [
            "Cybersecurity is all about protecting systems and data from attacks.",
            "Always use strong, unique passwords and enable 2FA!",
        ]
    },
    "python": {
        "keywords": ["python", "coding", "programming", "code", "developer"],
        "replies": [
            "Python is one of the most versatile languages out there — great choice!",
            "Keep coding consistently and you'll improve fast!",
        ]
    },
    "time": {
        "keywords": ["time", "what time", "current time"],
        "replies": ["__TIME__"]
    },
    "date": {
        "keywords": ["date", "what date", "today", "what day"],
        "replies": ["__DATE__"]
    },
    "joke": {
        "keywords": ["joke", "funny", "make me laugh", "humor"],
        "replies": [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        ]
    },
    "motivation": {
        "keywords": ["motivate", "motivation", "inspire", "give up", "tired", "help me"],
        "replies": [
            "Every expert was once a beginner. Keep going. 💪",
            "Small steps every day lead to massive results over time.",
        ]
    },
}

# ─────────────────────────────────────────
#  Memory System (self-learning)
# ─────────────────────────────────────────

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def learn(user_input, correct_response, memory):
    key = user_input.lower().strip()
    if key not in memory:
        memory[key] = []
    if correct_response not in memory[key]:
        memory[key].append(correct_response)
    save_memory(memory)
    print("ARIA: Got it! I'll remember that. 🧠\n")

# ─────────────────────────────────────────
#  Core Logic
# ─────────────────────────────────────────

def get_response(user_input, memory):
    text = user_input.lower().strip()

    # Check learned memory first
    if text in memory:
        return random.choice(memory[text])

    # Check built-in knowledge
    for category, data in built_in.items():
        for keyword in data["keywords"]:
            if keyword in text:
                reply = random.choice(data["replies"])
                if reply == "__TIME__":
                    return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}."
                if reply == "__DATE__":
                    return f"Today is {datetime.datetime.now().strftime('%A, %B %d, %Y')}."
                return reply

    return None  # Unknown input


def main():
    memory = load_memory()
    learned_count = len(memory)

    print("=" * 50)
    print("      🤖 ARIA — Self-Learning Chatbot v2.0")
    print("=" * 50)
    print(f"  Loaded {learned_count} learned response(s) from memory.")
    print("  Type 'bye' to exit\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        # Exit
        if any(w in user_input.lower() for w in ["bye", "goodbye", "exit", "quit"]):
            print("ARIA: Goodbye! Stay curious. 👋\n")
            break

        response = get_response(user_input, memory)

        if response:
            print(f"ARIA: {response}\n")
        else:
            # Self-learning mode
            print("ARIA: I don't know how to respond to that yet.")
            print("      Can you teach me? What should I say?")
            print("      (Press Enter to skip)\n")
            teach = input("You: ").strip()

            if teach:
                learn(user_input, teach, memory)
            else:
                print("ARIA: Okay, I'll figure it out eventually!\n")


if __name__ == "__main__":
    main()