from threading import *
from time import sleep


def mysqsum() -> int:
    """Find sum of integer numbers' squares"""
    
    global num
    
    k = 1
    txt = f"{num}^2"

    while myevent.is_set():
        num += k ** 2
        txt += " + " + f"{k}^2"
        print(f"[{k}] {txt} = {num}")
        k += 1
        sleep(0.3)


print("Sum of integer numbers' squares")
t = Thread(target=mysqsum)
num = 0
myevent = Event()

myevent.set()
t.start()
sleep(2)
myevent.clear()

if t.is_alive():
    t.join()

print("Result:", num) 
        
