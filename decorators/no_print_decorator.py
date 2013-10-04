import os
import sys

def no_print(func):
    """
    Turn off printing for duration of the function call
    """
    def wrapper(*arg):
        sys.stdout = open(os.devnull, 'w')
        res = func(*arg)
        sys.stdout = sys.__stdout__
        return res
    return wrapper
