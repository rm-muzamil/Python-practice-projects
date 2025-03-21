from collections import deque
lists = [1,2,3]
dq = deque([1,2,3])

lists.append(4)
dq.append(4)
# lists.appendleft(4)  not possible
dq.appendleft(0)

print(lists)
print(dq)

lists.pop()
# lists.popleft()  not possible 
dq.pop()
dq.popleft()

print(lists)
print(dq)



################################################## ------- Heap ------- ##################################################

import heapq
numbers = [3,2,54,23,22,43]
heapq.heapify(numbers)  
heapq.heappush(numbers,40)
print(numbers)

min_val = heapq.heappop(numbers)  # Remove smallest element
print(min_val)  # 1

top_3 = heapq.nlargest(3, numbers)  # Get 3 largest numbers
print(top_3)  # [8, 5, 4]

################################################## ------- queue ------- ##################################################

from queue import Queue

q = Queue()

q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)


q.get()
q.get()
q.get()
q.get()
print(q.get())

st = deque()

st.append(1)
st.append(2)
st.append(3)
st.append(4)

print(st.pop())


################################################## ------- stack ------- ##################################################

stack = []
st = stack

st.append(1)
st.append(2)
st.append(3)
st.append(4)
st.append(5)

output = st.pop()
print(output)


from collections import deque

class TextEditor:
    def __init__(self):
        self.content = ""
        self.undo_state = deque()
        self.redo_state = deque()
    def write(self,text):
        self.undo_state.append(self.content)
        self.content += text
        self.redo_state.clear()
        print(f"Written : {text}")
    def undo(self):
        if self.undo_state:
            self.redo_state.append(self.content)
            self.content = self.undo_state.pop()
            print(f"Reverted last change")
        else:
            print(f"Nothing to Undo ")
    def redo(self):
        if self.redo_state:
            self.undo_state.append(self.content)
            self.content = self.redo_state.pop()
            print("↪️ Redo: Restored last change")
        else:
            print("❌ Nothing to redo!")
    def show_content(self):
        """Display current text content"""
        print(f"\n📄 Current Content: {self.content}\n")

editor = TextEditor()

editor.write("My Name is")
editor.show_content()

editor.write("Muzzamil")
editor.show_content()

editor.undo()
editor.show_content()

editor.write("Muzammil")
editor.show_content()

editor.undo()
editor.show_content()

editor.redo()
editor.show_content()
        
editor.undo()
editor.show_content()

editor.undo()
editor.show_content()
        