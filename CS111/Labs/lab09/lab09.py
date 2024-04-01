import random


def in_range1(n):
    """Write a function that checks to see if n is
    within the range of 1-100 and have it return False if not
    #>>> in_range1(9)
    True
    #>>> in_range1(-4)
    False
    """
    "*** YOUR CODE HERE ***"
    return 1 <= n <= 100


def main():
    """Write code in the main function that generates 1000
    random numbers between 1 and 101 and calls the generated
    function to validate the number generated."""
    "*** YOUR CODE HERE ***"
    for i in range(1000):
        random_number = random.randint(1,101)
        result = in_range1(random_number)
        print(f"{random_number}: {result}")


def in_range2(num):
    """Redo in_range1, but throw an exception instead of
    throwing false
    """
    "*** YOUR CODE HERE ***"
    if not (1 <= num <= 100):
        raise ValueError(f"{num} is not in the range of 1-100")


