# Simple Rule-based Chatbot
import tkinter as tk
import random
import requests

from textblob import TextBlob
from fuzzywuzzy import process


user_data = {}

def analyze_sentiment(user_input):
    analysis = TextBlob(user_input)
    if analysis.sentiment.polarity > 0:
        return "You seem happy! 😊"
    elif analysis.sentiment.polarity < 0:
        return "I'm sorry to hear that. 😟"
    else:
        return "That's interesting! Tell me more."

# Use in the chatbot


def send_message():
    user_message = user_input.get()
    chat_log.insert(tk.END, f"You: {user_message}\n")
    response = chatbot_response(user_message)
    chat_log.insert(tk.END, f"Chatbot: {response}\n")
    user_input.delete(0, tk.END)
    save_history(user_message,response)
    
root = tk.Tk()
root.title("Chatbot")

chat_log = tk.Text(root, height=20, width=50)
chat_log.pack()

user_input = tk.Entry(root, width=40)
user_input.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# def get_user_name():
#     name = input("What's your name? :")
#     print(f"Nice to meet you {name}")
#     return name

def random_fact():
    facts = [
        "Did you know? The Eiffel Tower can be 15 cm taller during the summer.",
        "Fun fact: Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
        "Here's something cool: Octopuses have three hearts!",
    ]
    return random.choice(facts)

def get_weather(city):
    api_key = "135f82dfd6a2a2217651464425566c59"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"The weather in {city} is {weather} with a temperature of {temp}°C."
    else:
        return "Sorry, I couldn't fetch the weather for that city."



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

        file.write(f"you: {user}\n")
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
    global user_data
    
    

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
    
    
    sentiment = analyze_sentiment(user_input)
    return sentiment

    
     
    
    
    
root.mainloop()