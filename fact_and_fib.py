from threading import Thread


def factorial(n: int) -> int:
    """Calculate the factorial of the number"""
    
    result = 1
    for number in range(1, n + 1):
        result *= number

    print("Factorial:", result)
    return result


def double_fact(n: int) -> int:
    """Calculate double factorial of the number (over one)"""

    result = 1
    for number in range(n, 0, -2):
        result *= number

    print("Double factorial:", result)
    return result


def fibonacci(n: int) -> int:
    """Calculate Fibonacci number at n position"""

    first = 1
    second = 1
    if n <= 2:
        result = 1
    else:
        for number in range(3, n + 1):
            result = first + second
            first, second = second, result

    print("Fibonacci number:", result)
    return result


def all_at_once() -> None:
    """Do factorial, double_fact and fibonacci functions
    in different threads
    """

    thread1 = Thread(target=factorial, args=[6])
    thread2 = Thread(target=double_fact, args=[9])
    thread3 = Thread(target=fibonacci, args=[6])

    thread1.start()
    thread1.join()
    thread2.start()
    thread2.join()
    thread3.start()    
    thread3.join()


all_at_once()
    
