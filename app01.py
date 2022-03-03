#!/usr/bin/env python3

"""
This script shows the answer to the common question of what the following bit of code would do:

    if __name__ == "__main__":
        main()
"""

import app02
import app03


def find_dem_names():
    print("My __name__ is:")
    print(__name__)
    
    print("The llamas function from app02 says it has the __name__ of:")
    app02.llamas()
    
    print("The myname function from app03 says it has the __name__ of:")
    app03.myname()
    app03.tim()


if __name__ == '__main__':
    find_dem_names()

# Ctrl v (select block of chars) Shift i  (type your spaces in) Esc
