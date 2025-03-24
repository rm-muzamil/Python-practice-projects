import threading
import multiprocessing
import time
import requests


# def print_numbers():
#     for i in range(5):
#         print(f"Number : {i}")
#         time.sleep(1)
# def print_alphabets():
#     for letter in "ABCDE":
#         print(f"Alphabet : {letter}")
#         time.sleep(1.1)
        
# t1 = threading.Thread(target=print_numbers)
# t2 = threading.Thread(target=print_alphabets)
# t1.start() 
# t2.start()
# t1.join()
# print("Both threads are done!")

# def square(n):
#     print(f"Square of {n}: {n*n}")
#     time.sleep(1)
# if __name__ == "__main__":
#     numbers = [1, 2, 3, 4, 5]

#     # Creating a process for each number
#     processes = [multiprocessing.Process(target=square, args=(num,)) for num in numbers]

#     # Starting processes
#     for p in processes:
#         p.start()

#     # Waiting for all processes to finish
#     for p in processes:
#         p.join()

#     print("All processes are done!")

# for i in range(10):
# def downloadFiles(url, name):
#     print(f"Downloading {name}")
#     response = requests.get(url, stream=True)
#     open(f"files/file{name}.jpg","wb").write(response.content)
#     print(f"finished Downloading {name}")
    
# url = "https://picsum.photos/2100/1800"
# # downloadFiles(url,"file1")
# # 
# if __name__ == '__main__':
#     prop = []
#     for i in range(1,21):
#         t = threading.Thread(target=downloadFiles, args=[url,f"threading{i}"])
#         t.start()
#         prop.append(t)
#         time.sleep(2)
    
# if __name__ == '__main__':
#     props = []
#     for j in range(21,41):
#         p = multiprocessing.Process(target=downloadFiles,args=[url,f"proccessing{j}"])
#         p.start()
#         props.append(p)
        
def count():
    x = 67
    for _ in range(10**9):  # Large computation
        x *= 89

if __name__ == '__main__':
    # Multithreading test
    t1 = threading.Thread(target=count)
    t2 = threading.Thread(target=count)

    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print(f"Multithreading Time: {end - start:.2f} seconds")

    # Multiprocessing test
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=count)
    p2 = multiprocessing.Process(target=count)

    start = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print(f"Multiprocessing Time: {end - start:.2f} seconds")