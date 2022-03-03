#!/usr/bin/env python3

"""
This script shows the answer to the common question of what the following bit of code would do:

    if __name__ == "__main__":
       llamas() 
"""

def myname():
    print(__name__)

def yourname():
    print("Is silly")

def tim():
    print("we should make fun of the new guy")

def main():
    myname()
    yourname()
    tim()


if __name__ == "__main__":
    print("about to call on the myname function")
    myname()
    yourname()
    tim()


