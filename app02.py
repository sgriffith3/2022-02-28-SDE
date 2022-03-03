#!/usr/bin/env python3

"""
This script shows the answer to the common question of what the following bit of code would do:

    if __name__ == "__main__":
       llamas() 
"""

def llamas():
    print(__name__)


if __name__ == "__main__":
    print("about to call on the llamas function")
    llamas()


