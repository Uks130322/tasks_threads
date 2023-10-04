from threading import Thread
from time import sleep

matrix = []


def fill_list(number: int, length: int, lst=[]) -> list[int]:
    """Create list with numbers"""
    
    lst.append([n for n in range(number, length + number)])
    return lst


def create_matrix(length: int, hight: int) -> list[list[int]]:
    """Create matrix length * hight"""
    
    global matrix
    matrix = []
    allThreads = [Thread(target=fill_list, args=[string * length,
                                                 length, matrix])
                  for string in range(hight)]

    for one_thread in allThreads:
        one_thread.start()

    for one_thread in allThreads:
        one_thread.join()

    return matrix


create_matrix(4, 7)
print(matrix)

