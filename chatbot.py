# Simple Rule-based Chatbot
import random

from fuzzywuzzy import process

def get_user_name():
    name = input("What's your name? :")
    print(f"Nice to meet you {name}")
    return name

def random_fact():
    facts = [
        "Did you know? The Eiffel Tower can be 15 cm taller during the summer.",
        "Fun fact: Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
        "Here's something cool: Octopuses have three hearts!",
    ]
    return random.choice(facts)


def detect_emotions(user_input):
    emotions = {
         "happy": ["That's great to hear!", "I'm glad you're feeling happy!"],
        "sad": ["I'm here for you.", "I'm sorry to hear that. Things will get better!"],
        "angry": ["Take a deep breath. It's going to be okay."],
    }
    for emotion, response in emotions.items():
        if emotion in user_input.lower():
            return random.choice(response)
        return None
        
    

def save_history(user,bot):
    with open("chat_history.txt","a") as file:

        file.write(f"{user_name}: {user}\n")
        file.write(f"Chatbot: {bot}\n")
        file.write("-" * 20 + "\n")
        
def fuzzy_response(user_input, responses):
    closest_match , score = process.extractOne(user_input,responses.keys())
    if score > 70:
        return closest_match
    return None
        
# def prosesses_input(user_input):
#     synonyms = {
#         "hi" : "hello",
#         "hy" : "hello",
#         "hey" : "hello",
#         "oye" : "hello",
#         "by" : "bye",
#         "ok" : "bye",
#         "oka" : "bye",
#         "okay" : "bye",

#     }
#     return synonyms.get(user_input.lower(), user_input.lower())

def chatbot_response(user_input):
    emotion_res = detect_emotions(user_input)
    if emotion_res:
        return emotion_res
    responses = {
        "tell me fact" : [random_fact()],
       "hello": ["Hi there!", "Hello! How can I help you?", "Hey! Good to see you!"],
        "how are you?": ["I'm doing great! How about you?", "I'm fine, thank you!", "Feeling awesome!"],
        "bye": ["Goodbye! Have a great day!", "Bye! Take care!", "See you next time!"],
    }
    fall_back_response = [
         "I'm sorry, I didn't catch that.",
        "Can you please rephrase?",
        "I'm still learning. Can you ask something else?",
    ]
    
    match = fuzzy_response(user_input.lower(),responses)
    if match:
        return random.choice(responses[match])
    else:
        return random.choice(fall_back_response)
user_name = get_user_name()

# Chat loop
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input(f"{user_name} : ")
    # user_input = prosesses_input(user_input)
    if user_input.lower() == "bye":
        print("Chatbot: ",chatbot_response(user_input))
        break
    bot_res = chatbot_response(user_input)
    print("Chatbot:", bot_res)
    save_history(user_input,bot_res)
