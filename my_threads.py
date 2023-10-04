from threading import Thread
from time import sleep

def one_and_half_second():
    for number in range(5):
        sleep(1.5)
        print("First function", number + 1)

def one_second():
    for number in range(5):
        print("Second function", number + 1)
        sleep(1)

t = Thread(target=one_second)

t.start()
one_and_half_second()
