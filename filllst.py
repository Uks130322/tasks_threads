from threading import Thread
from time import sleep


def odd_pos():
    """Add numbers on an odd position in list"""
    
    global lst
    value = 1
    for index in range(len(lst)):
        if index % 2:
            lst[index] = value
            value += 1
            sleep(0.3)


def even_pos():
    """Add letters on an even position in list"""
    
    global lst
    value = "A"
    for index in range(len(lst)):
        if not index % 2:
            lst[index] = value
            value = chr(ord(value) + 1)
            sleep(0.3)


size = 15
lst = ["*"] * 15
print("Before fill:", lst)

A = Thread(target=odd_pos)
B = Thread(target=even_pos)

A.start()
B.start()
A.join()
B.join()

print("After fill:", lst)
