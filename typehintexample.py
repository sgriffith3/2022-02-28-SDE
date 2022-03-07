def reverser(words: list) -> list:
    result = words[-1::-1]
    return result



print(reverser("llamas in pajamas"))
print(reverser(["noodles", "pasta", "sghetti"]))
