# for <iterator> in <iterable>:
#     do something

pets = ["cat", "dog", "hamster"]

for pet in pets:
    # print("I have a" + pet)
    print(f"I have a {pet}")

print(pet)

for num in range(3, 10):
    print(num)

p = pets.__iter__()
#print(p.__next__())
#print(p.__next__())
#print(p.__next__())
#print(p.__next__()) -> Raises StopIteration Exception

while True:
    try:
        next_item = p.__next__()
        print(next_item)
        # do whatever is inside of for loop
    except StopIteration:
        print("Ran out of stuff!")
        break
