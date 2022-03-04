f = open("myfile.txt", "r")
print(f)
txt = f.read()
print(txt)
f.close()

print("\nOPTION #2: with context")
with open("myfile.txt") as f2:
    print(f2)
    words = f2.read()
    print(words)















#print("lines var:")
#lines = txt.split("\n")
#print(lines)
#
#print("txt2 var:")
#txt2 = f.readlines() # cursor already at end of file so nothing more to read
#print(txt2)
#f.close()
#print(f)
# txt_again = f.read() -> ValueError: I/O operation on closed file
# print(txt_again)


