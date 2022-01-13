#20CS023 Jayraj Karelia
def tulength(tuple):
    length = 0
    for _ in tuple:
        length +=1
    return length


tuple = ("apple", 1, 3.333,"jayraj")

print(tulength(tuple))

print(len(tuple))