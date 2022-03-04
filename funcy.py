#def basic(x, y):
#    answer = x * y + 3
#    # print(answer)
#    # return f"{x} * {y} + 3 = {answer}"
#    return answer
#
#
#print(basic(7, 10))
#grade = 25 + basic(7, 10)
#print(grade)
#
#
#def more_advanced(x, y, store_data=True, save_file="myanswer.txt"):
#    ans = x ** (y-3)
#    if store_data:
#        with open(save_file, "w") as f:
#            f.write(str(ans))
#    return ans
#
#
#print(more_advanced(7, 10, store_data=False))
## print(more_advanced(3, store_data=False))
#print(more_advanced(3, 7, store_data=False))
#

#       star args = *args
def solar_args(*objects):
    print(objects)
    s = sum(objects)
    #s = 0
    #for num in objects:
    #    s += num
    print(s)


solar_args(4, 8, 15, 16, 23, 42)


# star kwargs   =  **kwargs
def whiteboard(**kwargs):
    print(kwargs)
    for kw in kwargs.keys():
        print(kw, kwargs[kw])

whiteboard(instructor="Sam", lunch="awesome", eod="6:30")


def full(x, y, *args, washer_cycle="normal", **kwargs):
    pass












