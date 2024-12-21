# Simple Rule-based Chatbot
import random

def chatbot_response(user_input):
    responses = {
        "hello"or"hy": "Hi there! How can I help you?",
        "how are you?": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!",
        "what is your name" : "i have no name, but you can call me Chatbot if you like"
    }
    fall_back_response = [
         "I'm sorry, I didn't catch that.",
        "Can you please rephrase?",
        "I'm still learning. Can you ask something else?",
    ]
    return responses.get(user_input.lower(), random.choice(fall_back_response))

# Chat loop
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: ",chatbot_response(user_input))
        break
    print("Chatbot:", chatbot_response(user_input))
