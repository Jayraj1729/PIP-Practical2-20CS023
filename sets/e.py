#20CS023 Jayraj Karelia
def findcommon(items):
    tracker = {}
    for item in items:
        if item not in tracker.keys():
            tracker[item] = 0
        tracker[item]+=1
    maxitem = None
    max = -1
    for key in tracker.keys():
        if((tracker[key]) > max):
            max = tracker[key]
            maxitem = key
    return maxitem


l1 = [1,2,3,2,3,2,4,5,6]
tuple1 = ("apple","banana","apple","mango")


print(findcommon(l1))

print(findcommon(tuple1))