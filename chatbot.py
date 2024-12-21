# Simple Rule-based Chatbot
import random
from datetime import datetime
def save_history(user,bot):
    with open("chat_history.txt","a") as file:
        datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        file.write(f"You: {user}\n")
        file.write(f"Chatbot: {bot}\n")
        file.write("-" * 20 + "\n")
        
def prosesses_input(user_input):
    synonyms = {
        "hi" : "hello",
        "hy" : "hello",
        "hey" : "hello",
        "oye" : "hello",
        "by" : "bye",
        "ok" : "bye",
        "oka" : "bye",
        "okay" : "bye",

    }
    return synonyms.get(user_input.lower(), user_input.lower())

def chatbot_response(user_input):
    responses = {
        "hello": ["Hi there! How can I help you?",
                  'hello2'],
        "how are you?": ["I'm just a bot, but I'm doing great! How about you?","hay2"],
        "bye": ["Goodbye! Have a great day!","bye2"],
        "what is your name" : ["i have no name, but you can call me Chatbot if you like","name2"],
    }
    fall_back_response = [
         "I'm sorry, I didn't catch that.",
        "Can you please rephrase?",
        "I'm still learning. Can you ask something else?",
    ]
    if user_input.lower() in responses:
        return random.choice(responses.get(user_input.lower()))
    else:
        return random.choice(fall_back_response)


# Chat loop
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    o_user_input = input("You: ")
    user_input = prosesses_input(o_user_input)
    if user_input.lower() == "bye":
        print("Chatbot: ",chatbot_response(user_input))
        break
    bot_res = chatbot_response(user_input)
    print("Chatbot:", bot_res)
    save_history(o_user_input,bot_res)
