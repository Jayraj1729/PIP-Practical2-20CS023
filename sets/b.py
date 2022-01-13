#20CS023 Jayraj Karelia
def removeitem(set,item):
    set.discard(item)
    return set



set = {1,2,3,4,5,6,7}

set = removeitem(set,6)

print(set)
set = removeitem(set,100)

print(set)