import random
import datetime
import json
import os

# ─────────────────────────────────────────
#  Config
# ─────────────────────────────────────────

MEMORY_FILE = "memory.json"
VERSION = "3.0"

# ─────────────────────────────────────────
#  Knowledge Base
# ─────────────────────────────────────────

built_in = {
    "greetings": {
        "keywords": ["hello", "hi", "hey", "sup", "greetings", "good morning", "good evening", "good afternoon", "wassup", "yo", "howdy"],
        "replies": [
            "Hey! Great to see you. What's on your mind?",
            "Hello! I'm ARIA. How can I help you today?",
            "Hi there! Ask me anything — I'm all ears.",
            "Hey! Ready to chat. What do you need?",
            "Yo! What's up?",
        ]
    },
    "farewell": {
        "keywords": ["bye", "goodbye", "see you", "cya", "later", "quit", "exit", "take care", "peace", "good night"],
        "replies": [
            "Goodbye! Stay curious. 👋",
            "See you later! Keep building. 🚀",
            "Take care! Come back anytime.",
            "Peace! ✌️",
            "Good night! Rest well.",
        ]
    },
    "how_are_you": {
        "keywords": ["how are you", "how r u", "you okay", "you good", "how do you feel", "you alright", "how's it going", "hows it going", "what's up"],
        "replies": [
            "I'm just code, but I'm running great! 😄",
            "Doing well, thanks for asking! How about you?",
            "Always good — no bad days when you're a bot!",
            "Running at 100%! What can I do for you?",
            "Better now that you're here! 😄",
        ]
    },
    "name": {
        "keywords": ["your name", "who are you", "what are you", "what's your name", "introduce yourself", "what should i call you"],
        "replies": [
            "I'm ARIA — Automated Response & Information Assistant. Nice to meet you!",
            "My name is ARIA. I'm a self-learning AI chatbot built in Python.",
            "Call me ARIA! I learn from every conversation.",
        ]
    },
    "creator": {
        "keywords": ["who made you", "who created you", "your creator", "who built you", "who programmed you", "who is your developer"],
        "replies": [
            "I was built by Mo Rashad — a developer passionate about AI and cybersecurity.",
            "Mo Rashad created me as part of his AI portfolio. Pretty cool, right?",
            "A developer named Mo Rashad — check out his GitHub!",
        ]
    },

    # ── Tech Topics ──────────────────────────────────
    "ai": {
        "keywords": ["artificial intelligence", "machine learning", "deep learning", "neural network", "ai", "nlp", "natural language"],
        "replies": [
            "AI is the science of making machines think, learn, and adapt.",
            "Machine learning lets computers learn from data without being explicitly programmed.",
            "Deep learning uses multi-layered neural networks inspired by the human brain.",
            "NLP (Natural Language Processing) is what allows me to understand your text!",
            "AI is transforming every industry — from healthcare to finance to cybersecurity.",
        ]
    },
    "cybersecurity": {
        "keywords": ["cybersecurity", "hacking", "security", "password", "encryption", "firewall", "malware", "phishing", "vulnerability", "exploit", "ctf"],
        "replies": [
            "Cybersecurity protects systems, networks, and data from digital attacks.",
            "Always use strong, unique passwords and enable 2FA on every account!",
            "Encryption converts readable data into an unreadable format — only the right key can decode it.",
            "Phishing is when attackers trick you into revealing sensitive info via fake emails or sites.",
            "A firewall monitors and controls incoming/outgoing network traffic based on security rules.",
            "CTF (Capture The Flag) competitions are a great way to practice ethical hacking!",
            "Zero-day vulnerabilities are unknown security flaws that hackers exploit before patches exist.",
        ]
    },
    "python": {
        "keywords": ["python", "coding", "programming", "code", "developer", "script", "function", "loop", "variable"],
        "replies": [
            "Python is one of the most versatile languages — used in AI, web dev, automation, and more.",
            "Python's clean syntax makes it perfect for beginners and experts alike.",
            "Keep coding consistently — even 30 minutes a day adds up fast.",
            "Functions in Python let you reuse code blocks efficiently.",
            "Python libraries like NumPy, Pandas, and TensorFlow make complex tasks simple.",
            "Loops in Python (for/while) let you automate repetitive tasks effortlessly.",
        ]
    },
    "internet": {
        "keywords": ["internet", "web", "network", "wifi", "browser", "http", "https", "dns", "ip address"],
        "replies": [
            "The internet is a global network of interconnected computers sharing data.",
            "HTTP transfers data over the web — HTTPS does the same but encrypted.",
            "DNS (Domain Name System) translates domain names like google.com into IP addresses.",
            "Your IP address is your device's unique identifier on a network.",
            "WiFi uses radio waves to provide wireless internet connectivity.",
        ]
    },
    "blockchain": {
        "keywords": ["blockchain", "bitcoin", "crypto", "cryptocurrency", "ethereum", "nft", "web3"],
        "replies": [
            "Blockchain is a decentralized ledger that records transactions across many computers.",
            "Bitcoin was the first cryptocurrency, created in 2009 by the anonymous Satoshi Nakamoto.",
            "Ethereum introduced smart contracts — self-executing agreements coded on the blockchain.",
            "NFTs (Non-Fungible Tokens) are unique digital assets verified on the blockchain.",
            "Crypto markets are highly volatile — always do your own research before investing.",
        ]
    },

    # ── Science Topics ────────────────────────────────
    "space": {
        "keywords": ["space", "universe", "galaxy", "planet", "star", "nasa", "black hole", "moon", "mars", "asteroid", "cosmos", "solar system"],
        "replies": [
            "The observable universe is about 93 billion light-years in diameter.",
            "Black holes are regions where gravity is so strong that nothing — not even light — can escape.",
            "Mars is the most likely candidate for future human colonization.",
            "The Moon is Earth's only natural satellite and stabilizes our planet's axial tilt.",
            "NASA's James Webb Telescope is revealing galaxies from the earliest moments of the universe.",
            "A light-year is the distance light travels in one year — about 9.46 trillion kilometers.",
            "There are more stars in the universe than grains of sand on all of Earth's beaches.",
        ]
    },
    "science": {
        "keywords": ["science", "physics", "chemistry", "biology", "atom", "molecule", "evolution", "gravity", "quantum", "relativity"],
        "replies": [
            "Physics studies matter, energy, and the fundamental forces of nature.",
            "Einstein's theory of relativity revolutionized our understanding of space and time.",
            "Quantum mechanics describes the behavior of particles at the subatomic scale.",
            "DNA carries the genetic instructions for the development of all living organisms.",
            "Gravity is the force of attraction between all objects that have mass.",
            "Chemistry is the study of matter and the changes it undergoes.",
        ]
    },
    "math": {
        "keywords": ["math", "mathematics", "algebra", "calculus", "geometry", "statistics", "equation", "number", "formula"],
        "replies": [
            "Mathematics is the language of the universe — everything follows patterns.",
            "Calculus was independently developed by Newton and Leibniz in the 17th century.",
            "Statistics helps us make sense of data and draw meaningful conclusions.",
            "The Pythagorean theorem: a² + b² = c² — a cornerstone of geometry.",
            "Pi (π) ≈ 3.14159 — the ratio of a circle's circumference to its diameter.",
            "Algebra uses symbols and letters to solve equations and represent relationships.",
        ]
    },

    # ── World & Culture ───────────────────────────────
    "history": {
        "keywords": ["history", "ancient", "war", "civilization", "empire", "revolution", "historical", "world war", "egypt history"],
        "replies": [
            "Ancient Egypt was one of the world's first great civilizations, lasting over 3,000 years.",
            "World War II (1939–1945) was the deadliest conflict in human history.",
            "The Roman Empire at its peak controlled around 5 million km² of territory.",
            "The Industrial Revolution transformed manufacturing and society in the 18th–19th centuries.",
            "The French Revolution (1789) reshaped political systems across the world.",
            "Ancient Egypt gave us hieroglyphics, the calendar, and incredible architectural feats.",
        ]
    },
    "egypt": {
        "keywords": ["egypt", "cairo", "nile", "pyramids", "egyptian", "pharaoh", "luxor", "alexandria"],
        "replies": [
            "Egypt is home to one of humanity's oldest and greatest civilizations.",
            "The Nile River is the longest river in the world and the lifeblood of Egypt.",
            "The Pyramids of Giza are the only surviving wonder of the ancient world.",
            "Cairo is Africa's largest city and one of the most vibrant in the world.",
            "Ancient Egyptians invented one of the earliest writing systems — hieroglyphics.",
            "Luxor contains some of the world's most impressive ancient temples and tombs.",
        ]
    },
    "health": {
        "keywords": ["health", "fitness", "exercise", "diet", "nutrition", "sleep", "mental health", "workout", "gym", "calories", "protein"],
        "replies": [
            "Regular exercise reduces the risk of heart disease, diabetes, and depression.",
            "Sleep is when your body repairs itself — aim for 7–9 hours per night.",
            "Protein is essential for muscle repair and growth — aim for 1.6–2.2g per kg of bodyweight.",
            "Mental health is just as important as physical health — don't neglect it.",
            "Staying hydrated improves focus, energy, and physical performance.",
            "Compound exercises (squats, deadlifts, bench press) give the best results per time spent.",
            "Consistency beats intensity — showing up every day matters more than occasional hard sessions.",
        ]
    },
    "sports": {
        "keywords": ["sports", "football", "soccer", "basketball", "tennis", "mma", "boxing", "cricket", "golf", "athlete"],
        "replies": [
            "Football (soccer) is the world's most popular sport with over 4 billion fans.",
            "MMA combines striking and grappling from multiple martial arts disciplines.",
            "Golf is a game of precision, patience, and strategy — popular in business networking.",
            "Michael Jordan is widely considered the greatest basketball player of all time.",
            "Tennis requires exceptional footwork, reflexes, and mental strength.",
            "Sport teaches discipline, resilience, and teamwork — skills that transfer to everything.",
        ]
    },

    # ── Business & Finance ────────────────────────────
    "business": {
        "keywords": ["business", "startup", "entrepreneur", "company", "ceo", "founder", "invest", "money", "finance", "stocks", "etf", "market"],
        "replies": [
            "The best businesses solve real problems that people actually have.",
            "Cash flow is more important than profit — a business can be profitable and still fail.",
            "ETFs (Exchange-Traded Funds) offer diversified exposure to markets at low cost.",
            "Compound interest is one of the most powerful forces in finance — start early.",
            "A founder's most important skill is learning fast and adapting under pressure.",
            "Most successful startups didn't succeed with their first idea — they pivoted.",
            "Financial independence = your passive income exceeds your monthly expenses.",
        ]
    },

    # ── Lifestyle ─────────────────────────────────────
    "philosophy": {
        "keywords": ["philosophy", "meaning", "life", "purpose", "truth", "existence", "stoic", "wisdom", "consciousness"],
        "replies": [
            "Stoicism teaches that you control your reactions, not external events.",
            "Socrates said: 'The unexamined life is not worth living.'",
            "Marcus Aurelius: 'You have power over your mind, not outside events. Realize this and you will find strength.'",
            "The search for meaning is itself a meaningful act.",
            "Nietzsche: 'He who has a why to live can bear almost any how.'",
            "Philosophy isn't just theory — it's a practical guide for navigating life.",
        ]
    },
    "music": {
        "keywords": ["music", "song", "artist", "album", "rap", "hip hop", "jazz", "classical", "playlist", "beat"],
        "replies": [
            "Music is one of the few things that can directly affect your emotions and mood.",
            "Jazz improvisation is considered one of the highest forms of musical intelligence.",
            "Hip-hop originated in the Bronx, New York in the early 1970s.",
            "Classical music has been shown to improve concentration and cognitive performance.",
            "Creating music and listening to it activate different parts of the brain.",
        ]
    },
    "movies": {
        "keywords": ["movie", "film", "cinema", "watch", "actor", "director", "netflix", "series", "show"],
        "replies": [
            "The Godfather (1972) is widely considered one of the greatest films ever made.",
            "The Social Network brilliantly captures ambition, betrayal, and the cost of success.",
            "Goodfellas is a masterclass in storytelling, pacing, and character development.",
            "Great films don't just entertain — they change how you see the world.",
            "Christopher Nolan is known for mind-bending narratives and stunning visuals.",
        ]
    },

    # ── Utilities ─────────────────────────────────────
    "time": {
        "keywords": ["time", "what time", "current time", "clock"],
        "replies": ["__TIME__"]
    },
    "date": {
        "keywords": ["date", "what date", "today", "what day", "day today"],
        "replies": ["__DATE__"]
    },
    "joke": {
        "keywords": ["joke", "funny", "make me laugh", "humor", "laugh"],
        "replies": [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why was the JavaScript developer sad? He didn't know how to 'null' his feelings.",
            "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
            "Why do Python programmers prefer snakes? Because they love the syntax! 🐍",
            "I told my computer I needed a break... it said: 'No, you need a reboot.'",
            "There are 10 types of people in the world: those who understand binary, and those who don't.",
        ]
    },
    "motivation": {
        "keywords": ["motivate", "motivation", "inspire", "give up", "tired", "help me", "cant do it", "hard", "struggle", "stuck"],
        "replies": [
            "Every expert was once a beginner. Keep going. 💪",
            "Small steps every day lead to massive results over time.",
            "The fact that you're trying already puts you ahead of most people.",
            "Difficulty is the price of progress. Pay it.",
            "You don't have to be great to start, but you have to start to be great.",
            "One more try. Just one more.",
            "Your future self is watching — make them proud.",
        ]
    },
    "thanks": {
        "keywords": ["thanks", "thank you", "thx", "ty", "appreciate", "helpful"],
        "replies": [
            "You're welcome! 😊",
            "Anytime! That's what I'm here for.",
            "Happy to help! Ask me anything else.",
            "Glad I could help! 🙌",
        ]
    },
}

# ─────────────────────────────────────────
#  Sentiment Detection
# ─────────────────────────────────────────

positive_words = ["happy", "great", "awesome", "love", "amazing", "fantastic", "excited", "good", "wonderful", "joy"]
negative_words = ["sad", "angry", "depressed", "hate", "terrible", "awful", "bad", "upset", "frustrated", "worried", "anxious"]

def detect_sentiment(text):
    text = text.lower()
    if any(w in text for w in positive_words):
        return "positive"
    if any(w in text for w in negative_words):
        return "negative"
    return "neutral"

def sentiment_response(sentiment):
    if sentiment == "positive":
        return random.choice([
            "That's great to hear! 😊 What's going on?",
            "Love the positive energy! ⚡ Tell me more.",
            "Awesome! Keep that energy going. 🔥",
        ])
    elif sentiment == "negative":
        return random.choice([
            "I'm sorry to hear that. Want to talk about it?",
            "That sounds tough. I'm here if you need to vent.",
            "It's okay to feel that way. Things get better. 💙",
        ])
    return None

# ─────────────────────────────────────────
#  Fuzzy Matching
# ─────────────────────────────────────────

def fuzzy_match(user_input, keyword):
    """Check if keyword words appear in user input even if not exact."""
    user_words = user_input.lower().split()
    keyword_words = keyword.lower().split()
    return all(any(kw in uw for uw in user_words) for kw in keyword_words)

# ─────────────────────────────────────────
#  Memory System
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
#  Core Response Engine
# ─────────────────────────────────────────

def get_response(user_input, memory):
    text = user_input.lower().strip()

    # 1. Check learned memory
    if text in memory:
        return random.choice(memory[text])

    # 2. Sentiment check (standalone emotional messages)
    if len(text.split()) <= 6:
        sentiment = detect_sentiment(text)
        if sentiment != "neutral":
            return sentiment_response(sentiment)

    # 3. Built-in knowledge with fuzzy matching
    for category, data in built_in.items():
        for keyword in data["keywords"]:
            if keyword in text or fuzzy_match(text, keyword):
                reply = random.choice(data["replies"])
                if reply == "__TIME__":
                    return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}."
                if reply == "__DATE__":
                    return f"Today is {datetime.datetime.now().strftime('%A, %B %d, %Y')}."
                return reply

    return None

# ─────────────────────────────────────────
#  Main
# ─────────────────────────────────────────

def main():
    memory = load_memory()

    print("=" * 52)
    print(f"    🤖 ARIA — Self-Learning Chatbot v{VERSION}")
    print("=" * 52)
    print(f"  Memory: {len(memory)} learned response(s) loaded.")
    print("  Topics: AI, Cybersecurity, Space, Health,")
    print("          History, Business, Philosophy & more.")
    print("  Type 'bye' to exit\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if any(w in user_input.lower() for w in ["bye", "goodbye", "exit", "quit", "good night", "peace"]):
            print("ARIA: Goodbye! Stay curious. 👋\n")
            break

        response = get_response(user_input, memory)

        if response:
            print(f"ARIA: {response}\n")
        else:
            print("ARIA: I don't know how to respond to that yet.")
            print("      Can you teach me? What should I say?")
            print("      (Press Enter to skip)\n")
            teach = input("You: ").strip()
            if teach:
                learn(user_input, teach, memory)
            else:
                print("ARIA: Okay, I'll figure it out eventually! 🤔\n")


if __name__ == "__main__":
    main()
