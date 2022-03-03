#!/usr/bin/env python3

"""
This script shows the answer to the common question of what the following bit of code would do:

    if __name__ == "__main__":
        main()
"""

import app02
import app03

print("My name is:")
print(__name__)

print("The llamas function from app02 says it has the __name__ of:")
app02.llamas()

print("The myname function from app03 says it has the __name__ of:")
app03.myname()
app03.tim()
