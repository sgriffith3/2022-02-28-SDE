"""
This is the grader.py script.

This shows off try / except logic
"""

while True:
    try:
        score = int(input("How did you do on that test? "))

    except ValueError as err:
        print(err)
        print("Put in an integer, dummy")
        continue
    except KeyboardInterrupt:
        ans = input("\nDo you really want to quit? Y/N ")
        if ans.lower() == "y":
            break


    if score > 100:
        print("cheater")
    else:
        print("That's about what I expected from you")
