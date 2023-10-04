from threading import Thread
from time import sleep


def fill_list(first_symbol: int or float or str, length: int) -> list:
    """Fill list with symbols or numbers"""
    
    lst = []
    for index in range(length):
        lst.append(first_symbol)
        sleep(0.3)
        
        if isinstance(first_symbol, (int, float)):
            first_symbol += 1

        else:
            try:
                first_symbol = chr(ord(first_symbol) + 1)
            except TypeError:
                print(["Something wrong with first symbol"])
                return ["Something wrong with first symbol"]

    print(lst)
    return lst


threadWithSymbols = Thread(target=fill_list, args=["$", 7])
threadWithLetters = Thread(target=fill_list, args=["f", 10])
threadWithNumbers = Thread(target=fill_list, args=[17, 12])
threadWithStrNumbers = Thread(target=fill_list, args=["2", 6])
threadWithError = Thread(target=fill_list, args=["first", 5])

threadWithSymbols.start()
threadWithLetters.start()
threadWithNumbers.start()
threadWithStrNumbers.start()
threadWithError.start()

threadWithSymbols.join()
threadWithLetters.join()
threadWithNumbers.join()
threadWithStrNumbers.join()
threadWithError.join()
