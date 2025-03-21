################################################## ---------- Lists ----------- ##################################################
numbers = [78,68,94,34,23,32,12,1]
fruits = ["apple","mango","banana"]

print(numbers)
print(fruits)

numbers.sort()
fruits.sort()
numbers.insert(3,8)
fruits.pop()

print(numbers)
print(fruits)
################################################## ---- List Comprehension ---- ##################################################
lists = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
new_lists = [x**2 for x in lists if x % 3 == 0]
print(new_lists)



################################################## ---------- Tuples ---------- ##################################################

student = ("RM Muzammil",25,"BSSE")
print(student)

name,age,course = student
print(name,age,course)

################################################## ----------- Sets ----------- ##################################################

set1 = {2,4,4,6,8,10} # duplicate removed
set2 = {3,4,5,6,7}
print(set1)

union = set1.union(set2)
inter = set1.intersection(set2)
print(union,inter)

################################################## ------- Dictionaries ------- ##################################################\
    
staff = {
"employees" : {
    "emp1": {"name": "John", "age": 28, "salary": 50000},
    "emp2": {"name": "Emma", "age": 32, "salary": 60000},
    "emp3": {"name": "Mike", "age": 25, "salary": 45000},
},
"mangers" : {
    "emp1": {"name": "m-John", "age": 28, "salary": 50000},
    "emp2": {"name": "m-Emma", "age": 32, "salary": 60000},
    "emp3": {"name": "m-Mike", "age": 25, "salary": 45000},
},
"riders" : {
    "emp1": {"name": "r-John", "age": 28, "salary": 50000},
    "emp2": {"name": "r-Emma", "age": 32, "salary": 60000},
    "emp3": {"name": "r-Mike", "age": 25, "salary": 45000},
}
}


day_dict = {"Monday":30,"Tuesday":32,"Wednesday":12}

new_dict = {day:temp*(9/5) +32 for day,temp in day_dict.items()}
print(new_dict)

num_dict = {1:1,2:4,3:9,4:16,5:25}

new_num = {y : x**2  for x,y in num_dict.items()}
print(new_num)


# for practice 

numbers = [313,434,65,324,87,34,654,2345,54,22,1,0]
print(numbers)
temp = numbers
temp.sort()
print(f"Numbers in Ascending order : {temp}")
temp.sort(reverse = True)
print(f"Numbers in Deascending order : {temp}")

numbers.reverse()
print(f"Numbers in reverse order : {numbers}")
print(numbers)

sum = sum(numbers)
print(sum)
average = sum / len(numbers)
print(average)
numbers.remove(max(numbers))
numbers.remove(min(numbers))
print(numbers)


################################################## ------- Filter ------- ##################################################
num2 = []
for n in range(0,50):
    num2.append(n)
    
filterNum = list(filter(lambda x:x % 5 == 0,num2))
    
print(filterNum)






