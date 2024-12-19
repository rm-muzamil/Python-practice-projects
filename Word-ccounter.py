# def wordCounter(str):
#     words = str.split()
#     word_count = {}
#     for word in words:
#         word = word.lower()
#         word = word.strip(".,?!")
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return word_count
# str = "hello, hello my name is muzammil and people called me rm muzammil but name doesn't matter the thing that matter is behavior"
# result = wordCounter(str)
# print(result)    

import tkinter as tk

def wordCounter():
    str = sentenceEntry.get()
    words = str.split()
    word_count = {}
    for word in words:
        word = word.lower()
        word = word.strip(".,?!")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    result.insert(0,word_count)

app = tk.Tk()
app.title = "word counter"

sentenceEntry = tk.Entry(app,width=120)
sentenceEntry.pack(pady=5)

add_button = tk.Button(app, text="Add Task", width=15, command=wordCounter)
add_button.pack(pady=5)

result = tk.Listbox(app, width=120, height=15)
result.pack(pady=10)

app.mainloop()
