import random

def simple_chatbot():
    print("Hello! I'm a Simple Chatbot. You can type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'bye':
            print("Chatbot: Goodbye! Have a great day.")
            break
        elif 'how are you' in user_input:
            print("Chatbot: I'm doing well, thank you!")
        elif 'your name' in user_input:
            print("Chatbot: I'm just a simple chatbot.")
        elif 'joke' in user_input:
            jokes = [
                "Why did the scarecrow win an award? Because he was outstanding in his field!",
                "What did one wall say to the other wall? I'll meet you at the corner.",
                "Why don't scientists trust atoms? Because they make up everything!"
            ]
            print(f"Chatbot: {random.choice(jokes)}")
        else:
            print("Chatbot: I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    simple_chatbot()