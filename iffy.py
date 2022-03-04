# if <expression> is True:
#     indent 4 spaces and put code here
x = 15
if not x < 10:
    print(x)

    if x < 2:
        print(x)
        if x > 2:
            print("bigger than dos")

print("done")
# =    ASSIGNMENT OPERATOR - NOT FOR CONDITIONALS
# ==   is equal to
# <    less than
# >    greater than
# <=   less than or equal to
# >=   greater than or equal to
# !=   not equal to

# not
# in   
info = "This is an information kiosk"
if "kiosk" not in info:
    print("Not the right spot!")
elif "info" in info:
    print("We are getting close")
else:
    print("Better find a sign")

