"""
TASK 2: Basic Chatbot
Goal: Build a simple rule-based chatbot.
Scope:
Input from user like: "hello", "how are you", "bye".
Predefined replies like: "Hi!", "I'm fine, thanks!", "Goodbye!".
Key Concepts Used: if-elif, functions, loops, input/output.
"""

def chatbot_response(user_input):
    """Returns chatbot replies based on user input"""
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi! Nice to meet you 👋"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How about you?"
    elif user_input in ["what is your name", "who are you"]:
        return "I'm a simple chatbot created in Python 🤖"
    elif user_input in ["what can you do", "help", "commands"]:
        return "I can chat with you! Try asking: hello, how are you, your name, the time, or say bye."
    elif user_input in ["what is python", "python"]:
        return "Python is a popular programming language known for simplicity and versatility 🐍"
    elif user_input in ["what time is it", "time"]:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')} ⏰"
    elif user_input in ["thank you", "thanks"]:
        return "You're welcome! 😊"
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day 😊"
    else:
        return "Sorry, I don't understand that."

def run_chatbot():
    print("="*40)
    print("🤖 Welcome to the Basic Chatbot!")
    print("Type 'bye' to exit the chat.")
    print("="*40)

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)
        if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
            break

if __name__ == "__main__":
    run_chatbot()
