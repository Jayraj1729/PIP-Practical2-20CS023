#20CS023 Jayraj Karelia
def additem(t,item):
    l = list(t)
    l.append(item)
    t = tuple(l)
    return t

t = (1,2,3,4,5,6)
item = "Apple"

t = additem(t,item)

print(t)